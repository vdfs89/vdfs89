import re

with open('build_langs.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace double backslashes before single quotes
code = code.replace("\\\\'", "\\'")

with open('build_langs.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Fixed single quotes in build_langs.py")
