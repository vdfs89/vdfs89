with open(r'd:\vdfs89\vdfs89\dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(len(lines)):
    if 'nome: "VITOR SILVA — AI ENGINEER"' in lines[i]:
        lines[i] = lines[i].replace('nome: "VITOR SILVA — AI ENGINEER"', 'nome: "VITOR SILVA — AI ENGINEER & ML ENGINEER"')
        break # Only replace the first one!

for i in range(len(lines)):
    if 'disponibilidade: "AVAILABLE FOR OPPORTUNITIES"' in lines[i]:
        lines[i] = lines[i].replace('AVAILABLE FOR OPPORTUNITIES', 'Open to remote opportunities (Brazil & global)')
        break

for i in range(len(lines)):
    if '{ valor: 15,  sufixo: "",   label: "Years of mission-critical operations" }' in lines[i]:
        lines[i] = lines[i].replace('sufixo: ""', 'sufixo: "+"')
        break

for i in range(len(lines)):
    if 'cargo: "AI Engineer & Solutions Architect"' in lines[i]:
        lines[i] = lines[i].replace('cargo: "AI Engineer & Solutions Architect"', 'cargo: "AI Engineer & ML Engineer"')
        break

resume = "AI Engineer working end-to-end across architecture, backend and ML systems. I build scalable, reliable multi-agent systems and APIs, bringing a mission-critical mindset to AI engineering."

for i in range(len(lines)):
    if 'resumoExecutivo:' in lines[i]:
        lines[i+1] = f'    "{resume}",\n'
        lines[i+2] = ''
        lines[i+3] = ''
        break

# Add lang-toggle CSS if not exists
css_to_add = '''
/* ════════════════════════════════════
   LANG TOGGLE
════════════════════════════════════ */
.lang-toggle {
    display: flex; gap: 0.5rem; align-items: center; justify-content: center; margin-bottom: 15px;
    font-size: 0.7rem; font-weight: 700; letter-spacing: 0.08em;
    color: var(--muted);
}
.lang-toggle a { color: inherit; text-decoration: none; transition: color .2s; }
.lang-toggle a:hover { color: var(--green-dim); }
.lang-toggle a.active-lang { color: var(--green); text-shadow: var(--glow-text); }
'''

content = "".join(lines)
if '.lang-toggle' not in content:
    content = content.replace('</style>', css_to_add + '\n</style>')

# Add lang-toggle to sidebar__nav
if 'lang-toggle' not in content.split('<nav class="sidebar__nav"')[1]:
    nav_html = '''<nav class="sidebar__nav" aria-label="Navegação principal" id="navPrincipal">
    <nav class="lang-toggle">
        <a href="dashboard.en.html" class="__EN_ACTIVE__">EN</a> &middot;
        <a href="dashboard.pt.html" class="__PT_ACTIVE__">PT</a> &middot;
        <a href="dashboard.es.html" class="__ES_ACTIVE__">ES</a>
    </nav>'''
    content = content.replace('<nav class="sidebar__nav" aria-label="Navegação principal" id="navPrincipal">', nav_html)

with open(r'd:\vdfs89\vdfs89\dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)
