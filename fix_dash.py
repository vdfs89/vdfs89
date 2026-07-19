import re

with open(r'd:\vdfs89\vdfs89\dashboard.en.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Match the broken diagrama string
match = re.search(r'diagrama:\n\"┌──.*?└──────────────────┘\"', content, re.DOTALL)
if match:
    old_str = match.group(0)
    # the unescaped literal newline inside "..." + \n "..." needs fixing.
    # basically we just want to replace the whole thing with backticks
    # and strip out the `"\n + \n"` nonsense
    new_diagrama = '''diagrama: `┌─────────┐    ┌──────────────┐    ┌────────────────┐
│  User   │───▶│   FastAPI    │───▶│   LangGraph    │
└─────────┘    │   Gateway    │    │  Orchestrator  │
               └──────────────┘    └───────┬────────┘
                       ┌───────────────────┼───────────────────┐
                       ▼                   ▼                   ▼
               ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
               │     RAG      │    │    Judge     │    │  Governance  │
               │  Embeddings  │    │  Multi-LLM   │    │  & Auditing  │
               └──────┬───────┘    └──────┬───────┘    └──────┬───────┘
                      └───────────────────┼───────────────────┘
                                          ▼
                                ┌──────────────────┐
                                │ Validated Answer │
                                └──────────────────┘`'''
    content = content.replace(old_str, new_diagrama)
    with open(r'd:\vdfs89\vdfs89\dashboard.en.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Replaced quotes with backticks.')
else:
    print('Not found')
