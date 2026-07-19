import re
with open(r'd:\vdfs89\vdfs89\index.en.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'<div class="lang-sel".*?</div>\s*</div>', content, re.DOTALL)
if match:
    with open('lang_sel.txt', 'w', encoding='utf-8') as out:
        out.write(match.group(0))
    print('Saved to lang_sel.txt')
else:
    print('Not found')
