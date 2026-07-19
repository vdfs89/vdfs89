import re

with open(r'd:\vdfs89\vdfs89\dashboard.en.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update "4" to "7" AI projects in production
content = content.replace('{ valor: 4,   sufixo: "",   label: "AI projects in production" }', '{ valor: 7,   sufixo: "",   label: "AI projects in production" }')

# The dashboard sidebar footer usually looks like this:
#   <div class="sidebar__footer">
#     <span class="status-online"><span class="dot"></span>ONLINE</span>
#     <span id="anoAtual">2026</span>
#   </div>
#
# I will inject the lang-toggle right above the sidebar__footer.
lang_toggle = '''
  <nav class="lang-toggle-dash" style="padding: 10px 20px; font-size: 11px; font-family: var(--font-mono); display: flex; gap: 8px; justify-content: center; border-top: 1px solid #1c1c1c; align-items: center;">
    <style>
      .lang-toggle-dash a { color: var(--txt-dim); text-decoration: none; transition: color 0.2s; }
      .lang-toggle-dash a:hover { color: var(--neon); }
      .lang-toggle-dash a.active-lang { color: var(--neon); font-weight: bold; }
    </style>
    <a href="dashboard.en.html" class="__EN_ACTIVE__">EN</a> &middot;
    <a href="dashboard.pt.html" class="__PT_ACTIVE__">PT</a> &middot;
    <a href="dashboard.es.html" class="__ES_ACTIVE__">ES</a>
  </nav>

  <div class="sidebar__footer">
'''

if 'lang-toggle-dash' not in content:
    content = content.replace('  <div class="sidebar__footer">', lang_toggle)

with open(r'd:\vdfs89\vdfs89\dashboard.en.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated dashboard.en.html")
