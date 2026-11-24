# -*- coding: utf-8 -*-
"""Página de case do VITORIUM: build reprodutível e links no ar.

Roda com `python -m unittest discover tests`, sem dependência externa.
"""

import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASE = os.path.join(ROOT, "vitorium")
PAGES = {"index.html": "en", "index.pt.html": "pt-BR"}


def read(path):
    with io.open(path, encoding="utf-8", newline="") as f:
        return f.read()


class CasePages(unittest.TestCase):

    def test_pages_render_completely(self):
        for name, lang in PAGES.items():
            html = read(os.path.join(CASE, name))
            self.assertIn('<html lang="' + lang + '"', html, name)
            self.assertNotIn("{{", html, name + " tem placeholder sem texto")
            self.assertNotIn("\r\n", html, name + " tem CRLF")

    def test_committed_pages_match_a_fresh_build(self):
        """Se falhar, alguém editou vitorium/*.html à mão: edite o template
        ou o scripts/build_vitorium.py e rode o build."""
        tmp = tempfile.mkdtemp(prefix="vscase-")
        try:
            os.makedirs(os.path.join(tmp, "scripts", "vitorium_case"))
            shutil.copy2(os.path.join(ROOT, "scripts", "build_vitorium.py"), os.path.join(tmp, "scripts"))
            shutil.copy2(os.path.join(ROOT, "scripts", "vitorium_case", "template.html"),
                         os.path.join(tmp, "scripts", "vitorium_case"))
            r = subprocess.run([sys.executable, os.path.join(tmp, "scripts", "build_vitorium.py")],
                               capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            for name in PAGES:
                self.assertEqual(read(os.path.join(tmp, "vitorium", name)), read(os.path.join(CASE, name)), name)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def test_local_assets_exist(self):
        for name in PAGES:
            html = read(os.path.join(CASE, name))
            for ref in re.findall(r'(?:src|href)="((?!https?:|#|mailto:)[^"]+)"', html):
                target = os.path.normpath(os.path.join(CASE, ref.split("#")[0]))
                if os.path.isdir(target):
                    target = os.path.join(target, "index.html")
                self.assertTrue(os.path.exists(target), name + " aponta para " + ref + ", que não existe")

    def test_model_weights_are_consistent(self):
        m = json.loads(read(os.path.join(CASE, "model.json")))
        self.assertEqual(m["classes"], ["atencao", "normal", "urgente"])
        n = len(m["terms"])
        self.assertEqual(len(m["idf"]), n)
        self.assertEqual([len(r) for r in m["coef"]], [n, n, n])
        self.assertEqual(len(m["intercept"]), 3)


class HomeLinksToTheCase(unittest.TestCase):

    def test_each_home_variant_links_to_its_case_page(self):
        expected = {
            "index.html": 'href="vitorium/"',
            "index.en.html": 'href="vitorium/"',
            "index.pt.html": 'href="vitorium/index.pt.html"',
            "index.es.html": 'href="vitorium/"',
        }
        for name, link in expected.items():
            self.assertIn(link, read(os.path.join(ROOT, name)), name + " não linka o case do VITORIUM")


if __name__ == "__main__":
    unittest.main()
