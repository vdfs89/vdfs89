# -*- coding: utf-8 -*-
"""Regressão do pipeline de build do vitorsilva.page.

Cada teste aqui trava um bug que já aconteceu de verdade neste repositório.
Sem dependência externa: roda com `python -m unittest discover tests`.
"""

import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INDEX = {
    "index.html": "en",
    "index.en.html": "en",
    "index.pt.html": "pt-BR",
    "index.es.html": "es",
}

DASHBOARD = {
    "dashboard.html": "en",
    "dashboard.en.html": "en",
    "dashboard.pt.html": "pt-BR",
    "dashboard.es.html": "es",
}

GENERATED = list(INDEX) + list(DASHBOARD)

# fontes editadas à mão; o resto é gerado a partir delas
SOURCES = ["index.en.html", "dashboard.en.html"]

BUILDERS = ["build_langs.py", "build_dashboard_langs.py"]


def read(path):
    with io.open(path, encoding="utf-8", newline="") as f:
        return f.read()


def read_root(name):
    return read(os.path.join(ROOT, name))


class GeneratedFiles(unittest.TestCase):
    """As páginas existem e não estão vazias."""

    def test_all_generated_files_exist(self):
        for name in GENERATED:
            path = os.path.join(ROOT, name)
            self.assertTrue(os.path.isfile(path), name + " não existe")
            self.assertGreater(os.path.getsize(path), 10_000, name + " está pequeno demais")

    def test_line_endings_are_lf(self):
        """O repositório é LF. Os geradores já gravaram CRLF uma vez, e isso
        transformava cada build num diff de arquivo inteiro."""
        for name in GENERATED:
            self.assertNotIn("\r\n", read_root(name), name + " tem CRLF")


class LanguageAttributes(unittest.TestCase):
    """Os quatro dashboards já saíram todos com lang=pt-BR, inclusive o inglês."""

    def test_html_lang_matches_the_variant(self):
        for name, lang in list(INDEX.items()) + list(DASHBOARD.items()):
            html = read_root(name)
            found = re.search(r'<html lang="([^"]+)"', html)
            self.assertIsNotNone(found, name + " não declara lang")
            self.assertEqual(found.group(1), lang, name + " declara o idioma errado")


class RootServesEnglish(unittest.TestCase):
    """A raiz servia português e o README mira recrutador internacional."""

    def test_root_pages_are_english(self):
        for name in ("index.html", "dashboard.html"):
            self.assertIn('<html lang="en"', read_root(name), name + " não está em inglês")

    def test_root_pages_detect_browser_language(self):
        for name, pt, es in (
            ("index.html", "index.pt.html", "index.es.html"),
            ("dashboard.html", "dashboard.pt.html", "dashboard.es.html"),
        ):
            html = read_root(name)
            self.assertIn("langChosen", html, name + " perdeu a detecção de idioma")
            self.assertIn(pt, html, name + " não aponta para a variante em português")
            self.assertIn(es, html, name + " não aponta para a variante em espanhol")

    def test_detection_script_comes_after_charset(self):
        """Antes do charset, o navegador pode reinterpretar a página."""
        for name in ("index.html", "dashboard.html"):
            html = read_root(name)
            self.assertLess(
                html.index('<meta charset="UTF-8">'),
                html.index("langChosen"),
                name + ": o script de detecção está antes do charset",
            )


class LanguageToggle(unittest.TestCase):
    """O build do dashboard marcava EN como ativo nas páginas PT e ES."""

    def _check(self, page, expected_active, family):
        html = read_root(page)
        for target in family:
            found = re.search(r'<a href="' + re.escape(target) + r'" class="([^"]*)"', html)
            self.assertIsNotNone(found, page + " não linka " + target)
            active = "active-lang" in found.group(1)
            if target == expected_active:
                self.assertTrue(active, page + ": " + target + " deveria estar ativo")
            else:
                self.assertFalse(active, page + ": " + target + " não deveria estar ativo")

    def test_index_toggle(self):
        family = ["index.en.html", "index.pt.html", "index.es.html"]
        self._check("index.en.html", "index.en.html", family)
        self._check("index.pt.html", "index.pt.html", family)
        self._check("index.es.html", "index.es.html", family)
        self._check("index.html", "index.en.html", family)

    def test_dashboard_toggle(self):
        family = ["dashboard.en.html", "dashboard.pt.html", "dashboard.es.html"]
        self._check("dashboard.en.html", "dashboard.en.html", family)
        self._check("dashboard.pt.html", "dashboard.pt.html", family)
        self._check("dashboard.es.html", "dashboard.es.html", family)
        self._check("dashboard.html", "dashboard.en.html", family)


class Translation(unittest.TestCase):
    """A tabela é chaveada por frase inteira, mas o HTML quebrava frases em
    literais concatenados: nenhuma dessas chaves batia, e o assistente inteiro
    ia para o ar em inglês nas páginas PT e ES."""

    ENGLISH_LEFTOVERS = [
        "portfolio assistant",
        "View Projects",
        "AI projects",
        "Self-hosted automation platform",
        "Two-Tower Neural Network built on PyTorch",
        'aria-label="Overview"',
        'aria-label="Filter projects"',
    ]

    def test_no_english_leftovers_in_translated_pages(self):
        for name in ("index.pt.html", "index.es.html", "dashboard.pt.html", "dashboard.es.html"):
            html = read_root(name)
            for phrase in self.ENGLISH_LEFTOVERS:
                self.assertNotIn(phrase, html, name + ' ficou com "' + phrase + '" sem traduzir')

    def test_no_unjoined_string_concatenation(self):
        """Se um literal voltar a ser quebrado em duas linhas, a tradução
        silenciosamente para de funcionar naquela frase."""
        for name in ("dashboard.pt.html", "dashboard.es.html"):
            html = read_root(name)
            self.assertIsNone(
                re.search(r'"[ \t]*\+\s*\n\s*"', html),
                name + " tem literal concatenado: a tradução vai falhar nele",
            )


PROJECT_METRIC = re.compile(
    r'mcell-num">(\d+)</div><span class="mcell-lbl">'
    r'(?:AI projects shipped|Projetos de IA entregues|Proyectos de IA entregados)'
)


class ProjectCount(unittest.TestCase):
    """README dizia 5, dashboard dizia 7, o site mostrava 8 cards."""

    def test_hero_count_is_the_same_everywhere(self):
        counts = set()
        for name in INDEX:
            found = PROJECT_METRIC.search(read_root(name))
            self.assertIsNotNone(found, name + " perdeu o contador do topo")
            counts.add(found.group(1))
        self.assertEqual(len(counts), 1, "as páginas divergem no número de projetos: " + str(counts))

    def test_dashboard_counter_matches_the_hero(self):
        hero = PROJECT_METRIC.search(read_root("index.en.html")).group(1)
        # ancorado no rótulo: o primeiro `valor:` do dashboard é o de anos de
        # operação, não o de projetos
        counter = re.compile(
            r'valor:\s*(\d+),\s*sufixo:\s*"",\s*label:\s*'
            r'"(?:AI projects|Projetos de IA|Proyectos de IA)"'
        )
        for name in DASHBOARD:
            found = counter.search(read_root(name))
            self.assertIsNotNone(found, name + " perdeu o contador de projetos")
            self.assertEqual(found.group(1), hero, name + " diverge do contador do topo")

    def test_project_cards_match_the_counter(self):
        cards = len(re.findall(r'class="bc-title"', read_root("index.en.html")))
        hero = int(PROJECT_METRIC.search(read_root("index.en.html")).group(1))
        self.assertEqual(cards, hero, "o número anunciado não bate com os cards na página")


class Seo(unittest.TestCase):
    """As três variantes apontavam canonical para a raiz: só a raiz indexava."""

    def test_each_variant_is_canonical_to_itself(self):
        expected = {
            "index.html": "https://vitorsilva.page/",
            "index.en.html": "https://vitorsilva.page/",
            "index.pt.html": "https://vitorsilva.page/index.pt.html",
            "index.es.html": "https://vitorsilva.page/index.es.html",
        }
        for name, url in expected.items():
            found = re.search(r'<link rel="canonical" href="([^"]+)"', read_root(name))
            self.assertIsNotNone(found, name + " não tem canonical")
            self.assertEqual(found.group(1), url, name + " tem canonical errado")

    def test_hreflang_covers_every_language(self):
        for name in INDEX:
            html = read_root(name)
            for lang in ("en", "pt-BR", "es", "x-default"):
                self.assertIn('hreflang="' + lang + '"', html, name + " não declara hreflang " + lang)

    def test_sitemap_is_valid_and_complete(self):
        path = os.path.join(ROOT, "sitemap.xml")
        tree = ET.parse(path)
        ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
        locs = [el.text for el in tree.getroot().iter(ns + "loc")]
        for expected in (
            "https://vitorsilva.page/",
            "https://vitorsilva.page/index.pt.html",
            "https://vitorsilva.page/index.es.html",
            "https://vitorsilva.page/dashboard.html",
        ):
            self.assertIn(expected, locs, "sitemap não lista " + expected)
        for el in tree.getroot().iter(ns + "lastmod"):
            self.assertRegex(el.text, r"^\d{4}-\d{2}-\d{2}$", "lastmod fora do formato")


class BuildIsReproducible(unittest.TestCase):
    """O build gravava CRLF e acumulava uma linha em branco a cada rodada:
    rodar duas vezes produzia arquivos diferentes."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="vsbuild-")
        os.makedirs(os.path.join(self.tmp, "scripts"))
        for name in SOURCES:
            shutil.copy2(os.path.join(ROOT, name), os.path.join(self.tmp, name))
        for name in BUILDERS:
            shutil.copy2(os.path.join(ROOT, "scripts", name), os.path.join(self.tmp, "scripts", name))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _run_builders(self):
        for name in BUILDERS:
            result = subprocess.run(
                [sys.executable, os.path.join(self.tmp, "scripts", name)],
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, name + " falhou: " + result.stderr)

    def _snapshot(self):
        return {n: read(os.path.join(self.tmp, n)) for n in GENERATED if os.path.exists(os.path.join(self.tmp, n))}

    def test_second_run_changes_nothing(self):
        self._run_builders()
        first = self._snapshot()
        self.assertTrue(first, "o build não gerou nenhum arquivo")
        self._run_builders()
        second = self._snapshot()
        for name in first:
            self.assertEqual(first[name], second[name], name + " muda a cada build")

    def test_committed_output_matches_a_fresh_build(self):
        """Se falhar, alguém editou um arquivo gerado à mão — e a edição vai
        sumir no próximo build."""
        self._run_builders()
        for name, built in self._snapshot().items():
            self.assertEqual(
                built,
                read_root(name),
                name + " no repositório difere do que o build produz",
            )


if __name__ == "__main__":
    unittest.main()
