# -*- coding: utf-8 -*-
"""Páginas de case geradas por scripts/build_cases.py.

Roda com `python -m unittest discover tests`, sem dependência externa.
"""

import io
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASES = os.path.join(ROOT, "scripts", "cases")
SLUGS = sorted(n[:-3] for n in os.listdir(CASES) if n.endswith(".py") and not n.startswith("_"))
PAGES = {"index.html": "en", "index.pt.html": "pt-BR"}


def read(path):
    with io.open(path, encoding="utf-8", newline="") as f:
        return f.read()


class CasePages(unittest.TestCase):

    def test_there_is_at_least_one_case(self):
        self.assertTrue(SLUGS)

    def test_pages_render_completely(self):
        for slug in SLUGS:
            for name, lang in PAGES.items():
                html = read(os.path.join(ROOT, slug, name))
                self.assertIn('<html lang="' + lang + '"', html, slug + "/" + name)
                self.assertNotIn("{{", html, slug + "/" + name + " tem placeholder sem texto")
                self.assertNotIn("\r\n", html, slug + "/" + name + " tem CRLF")

    def test_committed_pages_match_a_fresh_build(self):
        """Se falhar, alguém editou <slug>/*.html à mão: edite scripts/cases/
        e rode python scripts/build_cases.py."""
        tmp = tempfile.mkdtemp(prefix="vscases-")
        try:
            shutil.copytree(CASES, os.path.join(tmp, "scripts", "cases"))
            shutil.copy2(os.path.join(ROOT, "scripts", "build_cases.py"), os.path.join(tmp, "scripts"))
            r = subprocess.run([sys.executable, os.path.join(tmp, "scripts", "build_cases.py")],
                               capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            for slug in SLUGS:
                for name in PAGES:
                    self.assertEqual(read(os.path.join(tmp, slug, name)), read(os.path.join(ROOT, slug, name)),
                                     slug + "/" + name + " difere do build")
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def test_local_assets_exist(self):
        for slug in SLUGS:
            base = os.path.join(ROOT, slug)
            for name in PAGES:
                for ref in re.findall(r'(?:src|href)="((?!https?:|#|mailto:)[^"]+)"', read(os.path.join(base, name))):
                    target = os.path.normpath(os.path.join(base, ref.split("#")[0]))
                    if os.path.isdir(target):
                        target = os.path.join(target, "index.html")
                    self.assertTrue(os.path.exists(target), slug + "/" + name + " aponta para " + ref)


class HomeLinksToEachCase(unittest.TestCase):

    def test_each_home_variant_links_to_every_case(self):
        for slug in SLUGS + ["vitorium"]:
            for home, target in (("index.html", slug + "/"), ("index.en.html", slug + "/"),
                                 ("index.es.html", slug + "/"), ("index.pt.html", slug + "/index.pt.html")):
                self.assertIn('class="case-link" href="' + target + '"', read(os.path.join(ROOT, home)),
                              home + " não linka o case " + slug)


if __name__ == "__main__":
    unittest.main()
