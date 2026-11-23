# -*- coding: utf-8 -*-
"""Build the project case study pages: <slug>/index.html (EN) and <slug>/index.pt.html (PT).

Each project is one module in scripts/cases/<slug>.py exposing a CASE dict;
the markup is scripts/cases/template.html. Text fields are either a plain
string (same in both languages) or an (English, Portuguese) tuple.

Integrity rule, same as the project READMEs: every number on a case page must
come from a versioned file in the project's own repository, and the page
prints that file's path under the number. Private projects get no numbers.

The VITORIUM page predates this engine and has its own builder
(scripts/build_vitorium.py) because of its in-browser demo.

Usage: python scripts/build_cases.py
"""

import html
import importlib.util
import io
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASES_DIR = os.path.join(REPO_DIR, "scripts", "cases")
TEMPLATE = os.path.join(CASES_DIR, "template.html")
SITE = "https://vitorsilva.page/"

LANGS = ("en", "pt")

UI = {
    "nav_label": ("Case study sections", "Seções do case"),
    "back": ("← All projects", "← Todos os projetos"),
    "projects": ("Projects", "Projetos"),
    "nav_numbers": ("Results", "Resultados"),
    "nav_demo": ("Demo", "Demo"),
    "nav_arch": ("Architecture", "Arquitetura"),
    "nav_video": ("Video", "Vídeo"),
    "github": ("GitHub →", "GitHub →"),
    "private": ("Private repository", "Repositório privado"),
    "demo_btn": ("▶ Open the live demo", "▶ Abrir a demo ao vivo"),
    "video_btn": ("Watch the video", "Ver o vídeo"),
    "numbers_prompt": ("Results", "Resultados"),
    "numbers_lead": ("Each figure comes from a versioned file in the repository. The source path is under every number.",
                     "Cada número vem de um arquivo versionado no repositório. O caminho da fonte está embaixo de cada número."),
    "demo_prompt": ("Live demo", "Demo ao vivo"),
    "arch_prompt": ("Architecture", "Arquitetura"),
    "story_prompt": ("Engineering decisions", "Decisões de engenharia"),
    "ev_prompt": ("Evidence", "Evidências"),
    "vid_prompt": ("Video", "Vídeo"),
    "vid_play": ("Play the presentation video", "Assistir ao vídeo de apresentação"),
    "vid_note": ("The player loads from YouTube only when you press play.",
                 "O player só carrega do YouTube quando você aperta o play."),
    "lim_prompt": ("Limitations", "Limitações"),
    "lim_h2a": ("What this project", "O que este projeto"),
    "lim_h2b": ("is not.", "não é."),
    "cta_repo": ("Read the code →", "Ver o código →"),
    "cta_contact": ("Get in touch", "Entrar em contato"),
    "private_note": ("The code is in a private repository. This page describes the architecture and the decisions only; ask me for a walkthrough.",
                     "O código está em um repositório privado. Esta página descreve só a arquitetura e as decisões; peça uma demonstração."),
}

# Rough glyph widths for IBM Plex Mono at the diagram's font sizes, used to
# refuse a build whose text would overflow its box.
TITLE_CH = 7.6
SUB_CH = 6.4


def t(value, i):
    """Pick the language variant of a text field."""
    if isinstance(value, tuple):
        return value[i]
    return value


def attr(text):
    return html.escape(text, quote=True)


def load_cases():
    cases = []
    for name in sorted(os.listdir(CASES_DIR)):
        if not name.endswith(".py") or name.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location("case_" + name[:-3], os.path.join(CASES_DIR, name))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        case = mod.CASE
        if case["slug"] != name[:-3]:
            raise ValueError(name + ": slug must match the file name")
        cases.append(case)
    return cases


def diagram(case, i):
    lanes = case["diagram"]["lanes"]
    width, pad, gap = 1000, 14, 38
    y, parts = 10, []
    for lane in lanes:
        nodes = lane["nodes"]
        lines = max(len(n.get("s", [])) for n in nodes)
        node_h = 44 + 18 * lines
        lane_h = node_h + 56
        parts.append('<rect class="lane" x="10" y="%d" width="980" height="%d" rx="2"/>' % (y, lane_h))
        parts.append('<text class="lt" x="24" y="%d">%s</text>' % (y + 22, t(lane["title"], i)))
        n = len(nodes)
        inner = width - 2 * (10 + pad)
        w = (inner - gap * (n - 1)) / n
        for k, node in enumerate(nodes):
            x = 10 + pad + k * (w + gap)
            ny = y + 38
            title = t(node["t"], i)
            subs = [t(s, i) for s in node.get("s", [])]
            for text, ch in [(title, TITLE_CH)] + [(s, SUB_CH) for s in subs]:
                if len(text) * ch > w - 24:
                    raise ValueError("%s: diagram text too wide for its box (%d px): %r" % (case["slug"], w, text))
            parts.append('<rect class="n" x="%.1f" y="%d" width="%.1f" height="%d" rx="2"/>' % (x, ny, w, node_h))
            parts.append('<text class="t" x="%.1f" y="%d">%s</text>' % (x + 14, ny + 25, html.escape(title)))
            for j, s in enumerate(subs):
                parts.append('<text class="s" x="%.1f" y="%d">%s</text>' % (x + 14, ny + 45 + 18 * j, html.escape(s)))
            if k + 1 < n and lane.get("flow", True):
                ay = ny + node_h / 2
                parts.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" marker-end="url(#ar)"/>' % (x + w, ay, x + w + gap - 4, ay))
        y += lane_h + 22
    height = y - 12
    svg = [
        '<svg class="arch" viewBox="0 0 %d %d" role="img" aria-labelledby="aT aD">' % (width, height),
        '<title id="aT">%s</title>' % html.escape(t(case["diagram"]["title"], i)),
        '<desc id="aD">%s</desc>' % html.escape(t(case["diagram"]["desc"], i)),
        '<defs><marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        '<path d="M2 1L8 5L2 9" fill="none" stroke="#00cc33" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>',
    ] + parts + ["</svg>"]
    return "\n".join(svg)


def heading(prompt, h2, lead, i):
    out = '<div class="prompt">%s</div>\n<h2>%s<br><span class="g">%s</span></h2>\n' % (t(prompt, i), t(h2[0], i), t(h2[1], i))
    if lead:
        out += '<p class="lead">%s</p>\n' % t(lead, i)
    return out


def section(sid, body):
    return '<hr class="sep">\n<section class="sec" id="%s">\n<div class="wrap">\n%s</div>\n</section>\n' % (sid, body)


def render(case, lang):
    i = LANGS.index(lang)
    slug = case["slug"]
    url_en, url_pt = SITE + slug + "/", SITE + slug + "/index.pt.html"
    home = "../" if lang == "en" else "../index.pt.html"
    u = {k: v[i] for k, v in UI.items()}
    sections, nav = [], []

    if case.get("numbers"):
        nav.append('<a class="hide-sm" href="#numbers">%s</a>' % u["nav_numbers"])
        cards = []
        for num in case["numbers"]:
            cls = "card num honest" if num.get("honest") else "card num"
            cards.append('<div class="%s"><div class="num-v">%s</div><div class="num-k">%s</div><div class="num-d">%s</div><div class="src">%s</div></div>'
                         % (cls, t(num["v"], i), t(num["k"], i), t(num["d"], i), num["src"]))
        body = heading(u["numbers_prompt"], case["numbers_h2"], case.get("numbers_lead", UI["numbers_lead"]), i)
        sections.append(section("numbers", body + '<div class="nums">\n' + "\n".join(cards) + "\n</div>\n"))

    demo = case.get("demo")
    if demo:
        nav.append('<a class="hide-sm" href="#demo">%s</a>' % u["nav_demo"])
        paras = "".join("<p>%s</p>" % t(p, i) for p in demo["p"])
        wake = '<p class="wake">%s</p>' % t(demo["wake"], i) if demo.get("wake") else ""
        body = heading(u["demo_prompt"], demo["h2"], None, i)
        body += ('<div class="card demo"><div>%s%s</div><div class="actions"><a class="btn btn-solid" href="%s" target="_blank" rel="noreferrer">%s</a></div></div>\n'
                 % (paras, wake, demo["url"], t(demo.get("label", UI["demo_btn"]), i)))
        sections.append(section("demo", body))

    nav.append('<a class="hide-sm" href="#architecture">%s</a>' % u["nav_arch"])
    d = case["diagram"]
    body = heading(u["arch_prompt"], d["h2"], d.get("lead"), i)
    body += '<div class="card arch-wrap">\n%s\n</div>\n' % diagram(case, i)
    if d.get("note"):
        body += '<p class="arch-note">%s</p>\n' % t(d["note"], i)
    sections.append(section("architecture", body))

    cards = []
    for k, dec in enumerate(case["decisions"], 1):
        cards.append('<article class="card st"><div class="st-k">%02d · %s</div><h3>%s</h3>%s</article>'
                     % (k, t(dec["k"], i), t(dec["h"], i), "".join("<p>%s</p>" % t(p, i) for p in dec["p"])))
    body = heading(u["story_prompt"], case["decisions_h2"], None, i)
    sections.append(section("story", body + '<div class="story">\n' + "\n".join(cards) + "\n</div>\n"))

    if case.get("evidence"):
        ev = case["evidence"]
        figs = []
        for f in ev["images"]:
            figs.append('<figure class="card"><img src="%s" width="%d" height="%d" loading="lazy" alt="%s"><figcaption>%s</figcaption></figure>'
                        % (f["src"], f["w"], f["h"], attr(t(f["alt"], i)), t(f["cap"], i)))
        cls = "ev one" if len(figs) == 1 else "ev"
        body = heading(u["ev_prompt"], ev["h2"], ev.get("lead"), i)
        sections.append(section("evidence", body + '<div class="%s">\n%s\n</div>\n' % (cls, "\n".join(figs))))

    video_script = ""
    if case.get("video"):
        v = case["video"]
        nav.append('<a class="hide-sm" href="#video">%s</a>' % u["nav_video"])
        body = heading(u["vid_prompt"], v["h2"], v.get("lead"), i)
        body += ('<div class="card video"><button type="button" id="play" aria-label="%s" style="background-image:url(\'https://i.ytimg.com/vi/%s/hqdefault.jpg\')"></button></div>\n'
                 '<p class="video-note">%s <a href="https://youtu.be/%s" target="_blank" rel="noreferrer">youtu.be/%s</a></p>\n'
                 % (attr(u["vid_play"]), v["id"], u["vid_note"], v["id"], v["id"]))
        sections.append(section("video", body))
        video_script = ('<script>\ndocument.getElementById("play").addEventListener("click", function () {\n'
                        '    var f = document.createElement("iframe");\n'
                        '    f.src = "https://www.youtube-nocookie.com/embed/%s?autoplay=1&rel=0";\n'
                        '    f.title = %s;\n'
                        '    f.allow = "autoplay; encrypted-media; picture-in-picture; fullscreen";\n'
                        '    f.allowFullscreen = true;\n'
                        '    this.replaceWith(f);\n'
                        '});\n</script>' % (v["id"], '"' + case["name"].replace('"', "") + '"'))

    lis = "".join("<li>%s</li>" % t(x, i) for x in case["limits"])
    ctas = []
    if case.get("github"):
        ctas.append('<a class="btn btn-solid" href="%s" target="_blank" rel="noreferrer">%s</a>' % (case["github"], u["cta_repo"]))
    for extra in case.get("extra_links", []):
        ctas.append('<a class="btn" href="%s" target="_blank" rel="noreferrer">%s</a>' % (extra["url"], t(extra["label"], i)))
    ctas.append('<a class="btn" href="%s#contact">%s</a>' % (home, u["cta_contact"]))
    body = heading(u["lim_prompt"], (UI["lim_h2a"], UI["lim_h2b"]), None, i)
    body += '<ul class="limits">%s</ul>\n<div class="actions" style="margin-top:2rem">%s</div>\n' % (lis, "".join(ctas))
    sections.append(section("limits", body))

    chips = "".join('<span class="chip%s">%s</span>' % (" amber" if c.get("amber") else "", t(c["t"], i))
                    for c in [x if isinstance(x, dict) else {"t": x} for x in case["chips"]])
    actions = []
    if demo:
        actions.append('<a class="btn btn-solid" href="#demo">%s</a>' % u["demo_btn"])
    if case.get("video"):
        actions.append('<a class="btn" href="#video">%s</a>' % u["video_btn"])
    if case.get("github"):
        actions.append('<a class="btn" href="%s" target="_blank" rel="noreferrer">%s</a>' % (case["github"], u["github"]))
    else:
        actions.append('<span class="chip amber" style="align-self:center">%s</span>' % u["private"])
    notice = ""
    if case.get("notice"):
        notice = '<p class="notice"><strong>%s</strong> %s</p>' % (t(case["notice"][0], i), t(case["notice"][1], i))
    elif not case.get("github"):
        notice = '<p class="notice">%s</p>' % u["private_note"]

    values = {
        "html_lang": "en" if lang == "en" else "pt-BR",
        "title": t(case["title"], i) + " | Vitor Silva",
        "og_title": t(case["title"], i),
        "meta_desc": attr(t(case["meta_desc"], i)),
        "canonical": url_en if lang == "en" else url_pt,
        "url_en": url_en, "url_pt": url_pt,
        "home_href": home,
        "en_on": "on" if lang == "en" else "", "pt_on": "on" if lang == "pt" else "",
        "ui_nav_label": u["nav_label"], "ui_back": u["back"], "ui_projects": u["projects"],
        "nav_links": "\n            ".join(nav),
        "index": case["index"], "tag": t(case["tag"], i), "name": case["name"],
        "hero_sub": t(case["hero_sub"], i), "hero_copy": t(case["hero_copy"], i),
        "chips": chips, "hero_actions": "".join(actions), "notice": notice,
        "sections": "".join(sections), "video_script": video_script,
    }
    with io.open(TEMPLATE, encoding="utf-8") as f:
        out = f.read()

    def sub(m):
        if m.group(1) not in values:
            raise KeyError("template key without value: " + m.group(1))
        return values[m.group(1)]

    out = re.sub(r"\{\{(\w+)\}\}", sub, out)
    if "{{" in out:
        raise ValueError(slug + ": unrendered placeholder")
    return out


def main():
    for case in load_cases():
        out_dir = os.path.join(REPO_DIR, case["slug"])
        os.makedirs(out_dir, exist_ok=True)
        for lang, name in (("en", "index.html"), ("pt", "index.pt.html")):
            with io.open(os.path.join(out_dir, name), "w", encoding="utf-8", newline="\n") as f:
                f.write(render(case, lang))
        print("wrote", case["slug"] + "/")


if __name__ == "__main__":
    main()
