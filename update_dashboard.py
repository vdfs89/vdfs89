import json
import re

with open(r'd:\vdfs89\vdfs89\dashboard.en.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We want to replace the `projetos: [ ... ]` part of DATA with ALL the projects
projects_replacement = r'''projetos: [
      {
        nome: "MESTREGRANA",
        tags: ["FLAGSHIP", "PRODUCTION"],
        flagship: true,
        categorias: ["ai"],
        descricao: "Multi-agent financial advisor — financial consulting with specialized agents and audited responses.",
        arquitetura: "LangGraph orchestration coordinating specialized agents; multi-LLM judge system for quality and security guardrails; RAG with embeddings for knowledge base grounding; governance and auditing layer logging and validating every response before delivery.",
        stack: ["LangGraph", "FastAPI", "Python", "RAG", "Multi-LLM", "MongoDB"],
        metricas: [
          { k: "Latency p95", v: "< 2s" },
          { k: "Uptime", v: "99.9%" },
          { k: "Accuracy (judge)", v: "> 95%" }
        ],
        diagrama:
"┌─────────┐    ┌──────────────┐    ┌────────────────┐\n" +
"│  User   │───▶│   FastAPI    │───▶│   LangGraph    │\n" +
"└─────────┘    │   Gateway    │    │  Orchestrator  │\n" +
"               └──────────────┘    └───────┬────────┘\n" +
"                       ┌───────────────────┼───────────────────┐\n" +
"                       ▼                   ▼                   ▼\n" +
"               ┌──────────────┐    ┌──────────────┐    ┌──────────────┐\n" +
"               │     RAG      │    │    Judge     │    │  Governance  │\n" +
"               │  Embeddings  │    │  Multi-LLM   │    │  & Auditing  │\n" +
"               └──────┬───────┘    └──────┬───────┘    └──────┬───────┘\n" +
"                      └───────────────────┼───────────────────┘\n" +
"                                          ▼\n" +
"                                ┌──────────────────┐\n" +
"                                │ Validated Answer │\n" +
"                                └──────────────────┘",
        links: [
          { label: "GitHub", url: "https://github.com/vdfs89/InvestimentoDIO" },
          { label: "Live Demo", url: "https://mestregrana.streamlit.app/", solid: true }
        ]
      },
      {
        nome: "FLUENCYFORGE",
        tags: ["EDTECH", "MULTI-AGENT"],
        flagship: false,
        categorias: ["ai"],
        descricao: "Edtech language learning platform with conversational agents, correction, and adaptive progression.",
        arquitetura: "Multi-agent system with tutor, evaluator, and curriculum planner roles; structured feedback pipeline by student level.",
        stack: ["LangGraph", "FastAPI", "RAG", "Flutter"],
        metricas: [{ k: "Status", v: "DESTAQUE" }],
        diagrama: null,
        links: [
          { label: "Live Demo", url: "https://fluencyforge.streamlit.app/", solid: true }
        ]
      },
      {
        nome: "TWINRANK AI",
        tags: ["E-COMMERCE", "DEEP LEARNING"],
        flagship: false,
        categorias: ["ai"],
        descricao: "Popularity-based recommendation systems fail in personalization.",
        arquitetura: "Two-Tower Neural Network built on PyTorch for collaborative filtering.",
        stack: ["PyTorch", "Two-Tower NN", "MLOps"],
        metricas: [{ k: "Status", v: "EM DESENV" }],
        diagrama: null,
        links: [{ label: "GitHub", url: "https://github.com/vdfs89" }]
      },
      {
        nome: "AETHER ONCOLOGY",
        tags: ["HEALTHCARE", "FULL-STACK"],
        flagship: false,
        categorias: ["fullstack"],
        descricao: "Full-stack oncology support platform — patient tracking, clinical data, and mobile.",
        arquitetura: "React web frontend, Flutter mobile app, Node.js API, and Python auxiliary services.",
        stack: ["React", "Node.js", "Flutter", "Python"],
        metricas: [{ k: "Status", v: "2026" }],
        diagrama: null,
        links: [
          { label: "GitHub", url: "https://github.com/vdfs89/Aether_Oncology" },
          { label: "Demo", url: "https://aetheroncology.vercel.app/", solid: true }
        ]
      },
      {
        nome: "VEKTORWORK",
        tags: ["SAAS", "ORCHESTRATION"],
        flagship: false,
        categorias: ["fullstack"],
        descricao: "Freelancers rely on high-cost cloud tools for complex workflows, without data ownership.",
        arquitetura: "Self-hosted automation platform with n8n, Docker Compose, PostgreSQL, and Redis.",
        stack: ["n8n", "Docker", "Self-Hosted"],
        metricas: [{ k: "Status", v: "PRIVADO" }],
        diagrama: null,
        links: [{ label: "GitHub", url: "https://github.com/vdfs89" }]
      },
      {
        nome: "RETENTIA",
        tags: ["B2B SAAS", "PREDICTIVE"],
        flagship: false,
        categorias: ["ai", "data"],
        descricao: "Predictive Churn Engine. High churn rates in SaaS platforms due to reactive support.",
        arquitetura: "Predictive churn modeling using Machine Learning, XGBoost, and FastAPI.",
        stack: ["Machine Learning", "XGBoost", "Churn"],
        metricas: [{ k: "Status", v: "ATIVO" }],
        diagrama: null,
        links: [
          { label: "GitHub", url: "https://github.com/vdfs89/RetentIA" },
          { label: "Demo", url: "https://retentia.vitorsilva.page/", solid: true }
        ]
      },
      {
        nome: "HARMONIZ.AI",
        tags: ["HEALTHTECH", "DATA"],
        flagship: false,
        categorias: ["pipeline"],
        descricao: "LLM pipeline for data harmonization and enrichment with automated staged validation.",
        arquitetura: "Staged pipeline with extraction, LLM normalization, rule-based validation, and auditable persistence.",
        stack: ["Python", "LLMs", "Data Engineering"],
        metricas: [{ k: "Status", v: "2026" }],
        diagrama: null,
        links: [{ label: "GitHub", url: "#" }]
      }
    ],'''

content = re.sub(r'projetos:\s*\[.*?\],\s*filtrosProjetos:', projects_replacement + '\n\n  filtrosProjetos:', content, flags=re.DOTALL)

with open(r'd:\vdfs89\vdfs89\dashboard.en.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Replaced projetos in dashboard.en.html')
