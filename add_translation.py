import os

with open(r'd:\vdfs89\vdfs89\build_langs.py', 'r', encoding='utf-8') as f:
    content = f.read()

phrase_en = 'The real challenge isn\'t building AI — it\'s trusting it in production. My projects target governance, guardrails and hallucination control.'
phrase_pt = 'O verdadeiro desafio não é construir IA — é confiar nela em produção. Meus projetos focam em governança, guardrails e controle de alucinação.'
phrase_es = 'El verdadero desafío no es construir IA — es confiar en ella en producción. Mis proyectos se centran en gobernanza, guardrails y control de alucinaciones.'

dict_entry = f'''
    "{phrase_en}": (
        "{phrase_pt}",
        "{phrase_es}"
    )
}}'''

if phrase_en not in content:
    content = content.replace('\n}\n\n    # Generate EN', ',' + dict_entry + '\n\n    # Generate EN')
    with open(r'd:\vdfs89\vdfs89\build_langs.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Added translation to build_langs.py')
else:
    print('Already present')
