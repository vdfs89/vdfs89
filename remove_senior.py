import io

def replace_in_file(filename, replacements):
    with io.open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements.items():
        if old in content:
            content = content.replace(old, new)
        else:
            print(f"Warning: Could not find '{old}' in {filename}")
            
    with io.open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

index_reps = {
    '<title>Vitor Silva | Senior AI Engineer | LangGraph, RAG and FastAPI</title>': '<title>Vitor Silva | AI Engineer | LangGraph, RAG and FastAPI</title>',
    '<meta property="og:title" content="Vitor Silva | Senior AI Engineer">': '<meta property="og:title" content="Vitor Silva | AI Engineer">',
    '<meta name="twitter:title" content="Vitor Silva | Senior AI Engineer">': '<meta name="twitter:title" content="Vitor Silva | AI Engineer">',
    '<span class="brand-sub">AI ENGINEER & SOLUTIONS ARCHITECT</span>': '<span class="brand-sub">AI ENGINEER</span>',
    '<div class="tl-title">AI Engineer & Solutions Architect</div>': '<div class="tl-title">AI Engineer</div>\n                              <p class="tl-copy">AI Engineer working end-to-end across architecture, backend and ML systems.</p>',
    'Open to AI Engineer or Solutions Architect positions. Professional maturity + cutting-edge AI stack for your team.': 'Open to AI Engineer positions. AI Engineer working end-to-end across architecture, backend and ML systems. Professional maturity + cutting-edge AI stack for your team.',
    'AI Engineer Curitiba, Solutions Architect': 'AI Engineer Curitiba, AI Architecture'
}

dash_reps = {
    'AI Engineer & Solutions Architect': 'AI Engineer',
    'nome: "VITOR SILVA — AI ENGINEER & SOLUTIONS ARCHITECT"': 'nome: "VITOR SILVA — AI ENGINEER"',
    'badge: "SÊNIOR"': 'badge: "AVANÇADO"',
    'cargo: "[PREENCHER cargo sênior real]': 'cargo: "[PREENCHER cargo real]',
    'cargo: "AI Engineer",\n        org: "Independente",\n        badge: "ESPECIALISTA",\n        bullets: [': 'cargo: "AI Engineer",\n        org: "Independente",\n        badge: "ESPECIALISTA",\n        bullets: [\n          "AI Engineer working end-to-end across architecture, backend and ML systems.",'
}

build_reps = {
    "'<title>Vitor Silva | Senior AI Engineer | LangGraph, RAG and FastAPI</title>': (\n            '<title>Vitor Silva | Engenheiro de IA Sênior | LangGraph, RAG e FastAPI</title>',\n            '<title>Vitor Silva | Ingeniero de IA Senior | LangGraph, RAG y FastAPI</title>'\n        )": "'<title>Vitor Silva | AI Engineer | LangGraph, RAG and FastAPI</title>': (\n            '<title>Vitor Silva | Engenheiro de IA | LangGraph, RAG e FastAPI</title>',\n            '<title>Vitor Silva | Ingeniero de IA | LangGraph, RAG y FastAPI</title>'\n        )",
    "'<meta property=\"og:title\" content=\"Vitor Silva | Senior AI Engineer\">': (\n            '<meta property=\"og:title\" content=\"Vitor Silva | Engenheiro de IA Sênior\">',\n            '<meta property=\"og:title\" content=\"Vitor Silva | Ingeniero de IA Senior\">'\n        )": "'<meta property=\"og:title\" content=\"Vitor Silva | AI Engineer\">': (\n            '<meta property=\"og:title\" content=\"Vitor Silva | Engenheiro de IA\">',\n            '<meta property=\"og:title\" content=\"Vitor Silva | Ingeniero de IA\">'\n        )",
    "'<meta name=\"twitter:title\" content=\"Vitor Silva | Senior AI Engineer\">': (\n            '<meta name=\"twitter:title\" content=\"Vitor Silva | Engenheiro de IA Sênior\">',\n            '<meta name=\"twitter:title\" content=\"Vitor Silva | Ingeniero de IA Senior\">'\n        )": "'<meta name=\"twitter:title\" content=\"Vitor Silva | AI Engineer\">': (\n            '<meta name=\"twitter:title\" content=\"Vitor Silva | Engenheiro de IA\">',\n            '<meta name=\"twitter:title\" content=\"Vitor Silva | Ingeniero de IA\">'\n        )",
    "'Open to AI Engineer or Solutions Architect positions. Professional maturity + cutting-edge AI stack for your team.': (\n        'Aberto a posições de Engenheiro de IA ou Arquiteto de Soluções. Maturidade profissional + stack de IA de ponta para o seu time.',\n        'Abierto a posiciones de Ingeniero de IA o Arquitecto de Soluciones. Madurez profesional + stack de IA de vanguardia para su equipo.'\n    )": "'Open to AI Engineer positions. AI Engineer working end-to-end across architecture, backend and ML systems. Professional maturity + cutting-edge AI stack for your team.': (\n        'Aberto a posições de Engenheiro de IA. AI Engineer trabalhando de ponta a ponta em arquitetura, backend e sistemas de ML. Maturidade profissional + stack de IA de ponta para o seu time.',\n        'Abierto a posiciones de Ingeniero de IA. AI Engineer trabajando de extremo a extremo en arquitectura, backend y sistemas de ML. Madurez profesional + stack de IA de vanguardia para su equipo.'\n    )"
}

replace_in_file('index.html', index_reps)
replace_in_file('dashboard.html', dash_reps)
replace_in_file('build_langs.py', build_reps)

print("Text replacements completed.")
