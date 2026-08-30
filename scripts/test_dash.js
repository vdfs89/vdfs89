
/* ════════════════════════════════════════════════════════════════
   DADOS — EDITE APENAS ESTE OBJETO
   Tudo que aparece no dashboard vem daqui. Os campos marcados com
   [PREENCHER] devem ser substituídos pelos valores reais.
   A lógica de renderização está mais abaixo e NÃO precisa ser tocada.
   ════════════════════════════════════════════════════════════════ */
const DATA = {

  /* ── Identity / Overview ── */
  nome: "VITOR SILVA — AI ENGINEER",
  localizacao: "Curitiba, PR, Brazil",
  disponibilidade: "AVAILABLE FOR OPPORTUNITIES",

  metricas: [
    { valor: 15,  sufixo: "",   label: "Years of mission-critical operations" },
    { valor: 4,   sufixo: "",   label: "AI projects in production" },
    { valor: 3,   sufixo: "",   label: "Languages (PT · EN · ES)" },
    { valor: 80, sufixo: "", label: "Continuous education certificates" }
  ],

  posicionamento:
    "15 years of mission-critical operations (SLA governance, " +
    "data auditing, logistics management) applied to reliable, " +
    "governed, and production-ready agentic AI systems.",

  ultimoDeploy: {
    nome: "MestreGrana",
    status: "LIVE",
    descricao: "Multi-agent financial advisor — LangGraph orchestration + multi-LLM judge in production.",
    link: "https://mestregrana.com.br"
  },

  links: {
    linkedin:  "https://linkedin.com/in/vitorsilva",
    github:    "https://github.com/vitorsilva",
    portfolio: "https://vitorsilva.engineer",
    email:     "mailto:mkmillhouse89@gmail.com"
  },

  /* ── Profile ── */
  resumoExecutivo:
    "AI Engineer with 15 years of operational maturity. I build scalable, " +
    "reliable multi-agent systems and APIs, bringing a mission-critical " +
    "mindset to AI engineering.",

  dados: [
    { k: "Location",    v: "Curitiba, PR, Brazil" },
    { k: "Availability",v: "Remote · Full-time/Contract · International" },
    { k: "Languages",   v: "Native PT-BR · Fluent EN · Intermediate ES" },
    { k: "Focus",       v: "Agentic AI · RAG · LLM Systems · MLOps" }
  ],

  diretrizes: [
    { k: "Target Model", v: "Remote Contract/Full-time" },
    { k: "Rate/Salary",  v: "To be discussed" },           /* NÃO exibir valores */
    { k: "Core Pillars", v: "AI Engineering · Backend · Architecture" }
  ],

  pilares: [
    "Multi-agent systems governance",
    "Production-ready RAG",
    "Multi-LLM guardrails",
    "Scalable FastAPI APIs",
    "LLM pipelines observability"
  ],

  /* ── Experience (timeline) ── */
  experiencia: [
    {
      periodo: "2024 — PRESENT",
      cargo: "AI Engineer & Solutions Architect",
      org: "Independent",
      badge: "EXPERT",
      bullets: [
        "Building production-grade agentic AI systems",
        "Multi-agent orchestration architecture with guardrails and auditing",
        "Deployment and operation of LLM APIs with end-to-end observability"
      ],
      stack: ["LangGraph", "LangChain", "FastAPI", "RAG", "Docker"]
    },
    {
      periodo: "2020 — 2024",
      cargo: "Operations Analyst — SLA Governance & Data Auditing",
      org: "ECT (Correios)",
      badge: "ADVANCED",
      bullets: [
        "SLA governance over large-scale corporate contracts",
        "Operational data auditing with high financial impact",
        "Technical focal point for corporate system implementations"
      ],
      stack: []
    },
    {
      periodo: "2016 — 2020",
      cargo: "Operations Analyst — Fleet & Logistics Management",
      org: "ECT (Correios)",
      badge: "INTERMEDIATE",
      bullets: [
        "Fleet and logistics management covering nationwide routes",
        "Consolidation of operational data for decision-making"
      ],
      stack: []
    },
    {
      periodo: "2011 — 2016",
      cargo: "Operations Technician",
      org: "ECT (Correios)",
      badge: "JUNIOR",
      bullets: [
        "Base operations in mission-critical environments",
        "Ensured SLA guarantee and large-scale operational continuity"
      ],
      stack: []
    }
  ],

  /* ── Education ── */
  formacao: [
    {
      curso: "Postgraduate in Machine Learning Engineering",
      instituicao: "FIAP",
      status: "IN PROGRESS",
      progresso: 40,
      previsao: "2027",
      foco: "MLOps, model deployment and ML pipelines in production.",
      disciplinas: ["MLOps", "Deep Learning", "Data Engineering", "Cloud ML"]
    },
    {
      curso: "BSc in Computer Science",
      instituicao: "Faculdade Descomplica Digital",
      status: "IN PROGRESS",
      progresso: 50,
      previsao: "2026",
      foco: "Formal foundations in algorithms, systems and distributed computing.",
      disciplinas: ["Algorithms", "Data Structures", "Databases", "Networks"]
    }
  ],

  /* ── Projects (filter categories: ai | fullstack | pipeline) ── */
  projetos: [
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
        diagrama: `┌─────────┐    ┌──────────────┐    ┌────────────────┐
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
                                └──────────────────┘`,
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
    ],

  filtrosProjetos: [
    { id: "todos",     label: "ALL" },
    { id: "ai",        label: "AI/AGENTS" },
    { id: "fullstack", label: "FULL-STACK" },
    { id: "pipeline",  label: "PIPELINE" }
  ],

  stackCompleto: [
    { grupo: "AI/LLM",   itens: ["LangGraph", "LangChain", "RAG", "Embeddings", "Multi-agent"] },
    { grupo: "Backend",  itens: ["Python", "FastAPI", "Node.js"] },
    { grupo: "Data",     itens: ["PostgreSQL", "MongoDB"] },
    { grupo: "Frontend", itens: ["React", "Flutter"] },
    { grupo: "Infra",    itens: ["Docker", "GCP/AWS"] }
  ],

  /* ── Certifications ── */
  certDestaque: {
    nome: "AWS Certified AI Practitioner (AIF-C01)",
    status: "IN PROGRESS",
    progresso: 55,
    plano: ["AWS Skill Builder", "Udemy", "Mocks"],
    previsao: "2026-Q4"
  },

  /* categories: ai | backend | data | soft | dev | outros */
  cursos: [
    { nome: "Data Visualization in Neo4j Browser", inst: "DIO", horas: "1h", data: "2026-05-26", cat: "data" },
    { nome: "Data Analyst: 10 Essential Professional Competencies", inst: "LinkedIn Learning", horas: "1h", data: "2026-05-21", cat: "data" },
    { nome: "Introduction to Santander Experience 2025 - 2nd Semester", inst: "DIO", horas: "1h", data: "2026-05-18", cat: "dev" },
    { nome: "Installing Neo4j Desktop Environment", inst: "DIO", horas: "1h", data: "2026-05-07", cat: "data" },
    { nome: "Using Software Development Copilots", inst: "DIO", horas: "1h", data: "2026-05-02", cat: "ai" },
    { nome: "Introduction to Graph Database and Neo4j", inst: "DIO", horas: "1h", data: "2026-04-30", cat: "data" },
    { nome: "Introduction to Low-Code Development", inst: "DIO", horas: "1h", data: "2026-04-28", cat: "ai" },
    { nome: "Natural or Fake Natty? How to Win in the Generative AI Era!", inst: "DIO", horas: "1h", data: "2026-04-25", cat: "ai" },
    { nome: "Welcome to Bradesco - GenAI & Data", inst: "DIO", horas: "1h", data: "2026-04-02", cat: "ai" },
    { nome: "Prompt Engineering Techniques", inst: "DIO", horas: "1h", data: "2026-03-31", cat: "ai" },
    { nome: "Computer Vision", inst: "DIO", horas: "1h", data: "2026-03-27", cat: "ai" },
    { nome: "Practical Applications of Artificial Intelligence", inst: "DIO", horas: "1h", data: "2026-02-24", cat: "ai" },
    { nome: "Welcome to Microsoft Acceleration - Azure AI Agents", inst: "DIO", horas: "1h", data: "2026-02-19", cat: "ai" },
    { nome: "Final Project Challenge — Build your Virtual Assistant with Generative AI", inst: "DIO", horas: "1h", data: "2026-02-19", cat: "ai" },
    { nome: "Welcome to Santander Bootcamp 2026 - Rust AI Developer", inst: "DIO", horas: "1h", data: "2026-02-19", cat: "backend" },
    { nome: "What are Generative AIs", inst: "DIO", horas: "1h", data: "2026-02-13", cat: "ai" },
    { nome: "Welcome to Bootcamp: Neo4j - Data Analysis with Graphs", inst: "DIO", horas: "1h", data: "2026-02-07", cat: "data" },
    { nome: "DIO Bootcamps: Free Education and Employability Together!", inst: "DIO", horas: "1h", data: "2026-01-26", cat: "dev" },
    { nome: "Accelerate your Learning with AI: Explore the Power of NotebookLM", inst: "DIO", horas: "1h", data: "2026-01-11", cat: "ai" },
    { nome: "Data Visualization: How to Convey Information Effectively", inst: "LinkedIn Learning", horas: "2h", data: "2026-01-01", cat: "data" },
    { nome: "Introduction to Prompt Engineering", inst: "DIO", horas: "1h", data: "2025-12-24", cat: "ai" },
    { nome: "Bradesco - GenAI & Data", inst: "DIO", horas: "1h", data: "2025-12-17", cat: "ai" },
    { nome: "Cybersecurity for Leaders: How to Handle a Cyber Attack", inst: "LinkedIn Learning", horas: "1h", data: "2025-12-05", cat: "outros" },
    { nome: "Fundamentals of Business Intelligence (BI)", inst: "DIO", horas: "1h", data: "2025-11-28", cat: "data" },
    { nome: "Introduction to Machine Learning for Beginners Bootcamp", inst: "DIO", horas: "1h", data: "2025-11-27", cat: "ai" },
    { nome: "Positivity and Emotional Intelligence", inst: "Udemy", horas: "1h", data: "2025-11-26", cat: "soft" },
    { nome: "The COMPLETE Guide to High Productivity + 4 Extra Courses", inst: "Udemy", horas: "1h", data: "2025-11-25", cat: "soft" },
    { nome: "Graph-Oriented Modeling Best Practices (Modeling and Performance)", inst: "DIO", horas: "1h", data: "2025-11-21", cat: "data" },
    { nome: "Essential Aspects of Strategic Business Analysis", inst: "LinkedIn Learning", horas: "1h", data: "2025-11-21", cat: "outros" },
    { nome: "Associating Generative AI Concepts", inst: "DIO", horas: "1h", data: "2025-11-16", cat: "ai" },
    { nome: "Introduction to Artificial Intelligence", inst: "DIO", horas: "1h", data: "2025-11-14", cat: "ai" },
    { nome: "Elevate your life with NLP", inst: "Udemy", horas: "1h", data: "2025-11-13", cat: "soft" },
    { nome: "Algorithms and Machine Learning", inst: "DIO", horas: "1h", data: "2025-11-11", cat: "ai" },
    { nome: "Natural Language Processing", inst: "DIO", horas: "1h", data: "2025-10-17", cat: "ai" },
    { nome: "Indispensable Competencies for your First 90 Days in Management", inst: "LinkedIn Learning", horas: "1h", data: "2025-10-17", cat: "soft" },
    { nome: "Using Microsoft Copilot to Write SQL Queries", inst: "DIO", horas: "1h", data: "2025-10-13", cat: "ai" },
    { nome: "The AI Era: Machine Learning, LLMs, Generative AI and Agents", inst: "DIO", horas: "1h", data: "2025-10-12", cat: "ai" },
    { nome: "Fundamentals of Large Language Models", inst: "DIO", horas: "1h", data: "2025-10-10", cat: "ai" },
    { nome: "Working with Microsoft Copilot", inst: "DIO", horas: "1h", data: "2025-10-07", cat: "ai" },
    { nome: "Applications and Impact of AI in Today's World", inst: "DIO", horas: "1h", data: "2025-10-04", cat: "ai" },
    { nome: "Nexa - Fundamentals of Generative AI with Bedrock", inst: "DIO", horas: "1h", data: "2025-09-28", cat: "ai" },
    { nome: "Introduction to Gamification", inst: "Udemy", horas: "1h", data: "2025-09-19", cat: "soft" },
    { nome: "How to Build and Lead Inclusive IT Teams", inst: "LinkedIn Learning", horas: "1h", data: "2025-09-12", cat: "soft" },
    { nome: "Introduction to Microsoft Acceleration - Data Architecture AI", inst: "DIO", horas: "1h", data: "2025-09-02", cat: "ai" },
    { nome: "Development Environment and First Steps with Python", inst: "DIO", horas: "1h", data: "2025-08-17", cat: "backend" },
    { nome: "Storytelling that Sells: Product Narrative with AI", inst: "LinkedIn Learning", horas: "1h", data: "2025-08-08", cat: "soft" },
    { nome: "Solving Calculations with Python", inst: "DIO", horas: "1h", data: "2025-08-04", cat: "backend" },
    { nome: "How to Improve IT Support in Hybrid Environments", inst: "LinkedIn Learning", horas: "1h", data: "2025-08-02", cat: "outros" },
    { nome: "Welcome to Accenture - Python for Data Analysis and Automation", inst: "DIO", horas: "1h", data: "2025-07-18", cat: "data" },
    { nome: "Conditional and Repetition Structures in Python", inst: "DIO", horas: "1h", data: "2025-07-13", cat: "backend" },
    { nome: "Applying Decisions and Repetitions in Practice", inst: "DIO", horas: "1h", data: "2025-07-10", cat: "outros" },
    { nome: "Coaching Leadership in 7 Days", inst: "Udemy", horas: "1h", data: "2025-07-09", cat: "soft" },
    { nome: "Business English for Portuguese Natives: Pronunciation", inst: "LinkedIn Learning", horas: "1h", data: "2025-07-06", cat: "soft" },
    { nome: "Negotiate like a Wolf - Sales Techniques", inst: "Udemy", horas: "1h", data: "2025-07-05", cat: "soft" },
    { nome: "Shyness: Become the center of attention in 30 days", inst: "Udemy", horas: "1h", data: "2025-06-30", cat: "soft" },
    { nome: "Types of Operators with Python", inst: "DIO", horas: "1h", data: "2025-06-26", cat: "backend" },
    { nome: "Code Versioning with Git and GitHub", inst: "DIO", horas: "1h", data: "2025-06-20", cat: "backend" },
    { nome: "How to Promote Emotional Engagement of your Employees", inst: "LinkedIn Learning", horas: "1h", data: "2025-06-16", cat: "soft" },
    { nome: "Creating an ETL Process with Excel and Power Query", inst: "DIO", horas: "1h", data: "2025-06-06", cat: "data" },
    { nome: "Strategic Positioning for High Potential Professionals", inst: "LinkedIn Learning", horas: "1h", data: "2025-06-04", cat: "soft" },
    { nome: "Explainable Artificial Intelligence (xAI) with Python", inst: "Udemy", horas: "1h", data: "2025-06-04", cat: "ai" },
    { nome: "Mastering Python Functions", inst: "DIO", horas: "1h", data: "2025-05-23", cat: "backend" },
    { nome: "Project Challenges: Create a Winning Portfolio", inst: "DIO", horas: "1h", data: "2025-05-17", cat: "dev" },
    { nome: "Introduction to Relational Databases", inst: "DIO", horas: "1h", data: "2025-04-26", cat: "data" },
    { nome: "How to Become an Inspiring Leader and Attract the Best Talent", inst: "LinkedIn Learning", horas: "2h", data: "2025-04-26", cat: "soft" },
    { nome: "Code Challenges: Perfect Your Logic and Computational Thinking", inst: "DIO", horas: "1h", data: "2025-04-16", cat: "backend" },
    { nome: "Working with Lists in Python", inst: "DIO", horas: "1h", data: "2025-04-14", cat: "backend" },
    { nome: "Manipulating Strings with Python", inst: "DIO", horas: "1h", data: "2025-04-12", cat: "backend" },
    { nome: "Introduction to Excel 365", inst: "DIO", horas: "1h", data: "2025-04-12", cat: "data" },
    { nome: "Games, Microlearning and Gamification in Education", inst: "Udemy", horas: "1h", data: "2025-04-10", cat: "soft" },
    { nome: "Voice Chatting with ChatGPT Using Whisper (OpenAI) and Python", inst: "DIO", horas: "1h", data: "2025-04-01", cat: "ai" },
    { nome: "Learning to Use Dictionaries in Python", inst: "DIO", horas: "1h", data: "2025-03-27", cat: "backend" },
    { nome: "Understanding Banking Operations with Python", inst: "DIO", horas: "1h", data: "2025-03-13", cat: "backend" },
    { nome: "ForteMente - Personal Development", inst: "Udemy", horas: "1h", data: "2025-02-24", cat: "soft" },
    { nome: "Programming Fundamentals with Python", inst: "DIO", horas: "1h", data: "2025-02-21", cat: "backend" },
    { nome: "Getting to Know Tuples in Python", inst: "DIO", horas: "1h", data: "2025-02-19", cat: "backend" },
    { nome: "Exploring Sets in Python", inst: "DIO", horas: "1h", data: "2025-02-07", cat: "backend" },
    { nome: "Building Solutions with Functions in Python", inst: "DIO", horas: "1h", data: "2025-01-20", cat: "backend" },
    { nome: "Getting to Know the Python Programming Language", inst: "DIO", horas: "1h", data: "2025-01-16", cat: "backend" },
    { nome: "Collection Manipulation and Functions in Python", inst: "DIO", horas: "1h", data: "2025-01-16", cat: "backend" }
  ],

  filtrosCursos: [
    { id: "todos",   label: "ALL" },
    { id: "ai",      label: "AI/ML" },
    { id: "backend", label: "BACKEND" },
    { id: "data",    label: "DATA" },
    { id: "soft",    label: "SOFT SKILLS" },
    { id: "dev",     label: "DEV" },
    { id: "outros",  label: "OTHER" }
  ],

  /* hours by area */
  horasPorArea: [
    { area: "AI/ML",       horas: 27 },
    { area: "Backend",     horas: 18 },
    { area: "Soft Skills", horas: 17 },
    { area: "Data",        horas: 13 },
    { area: "Other",      horas: 4 },
    { area: "Dev",         horas: 3 }
  ],

  /* skills certified in DIO (real profile XP) */
  habilidades: [
    { nome: "Leadership", xp: 720 },
    { nome: "Personal Marketing", xp: 480 },
    { nome: "Amazon Bedrock", xp: 480 },
    { nome: "Generative AI", xp: 480 },
    { nome: "Python", xp: 468 },
    { nome: "Artificial Intelligence (AI)", xp: 440 },
    { nome: "Whisper", xp: 240 },
    { nome: "Growth Mindset", xp: 240 },
    { nome: "Microsoft Fabric", xp: 240 },
    { nome: "Data Science", xp: 240 },
    { nome: "Continuous Learning", xp: 240 },
    { nome: "Neo4j", xp: 172 },
    { nome: "LLMs", xp: 60 },
    { nome: "GitHub", xp: 40 },
    { nome: "SQL", xp: 36 },
    { nome: "Systems Architecture", xp: 32 },
    { nome: "Low-code", xp: 24 },
    { nome: "ETL", xp: 16 },
    { nome: "Microsoft Copilot", xp: 16 },
    { nome: "Data", xp: 12 },
    { nome: "Prompt Engineering", xp: 12 },
    { nome: "Excel", xp: 12 }
  ],

  /* ── Achievements ── */
  conquistas: [
    { nome: "80th certificate completed — Data Visualization in Neo4j Browser", cat: "certificacao", data: "2026-05-26", icone: "award" },
    { nome: "58 achievements unlocked on DIO",            cat: "formacao",     data: "2026", icone: "layers" },
    { nome: "22 skills with certified XP on DIO",      cat: "formacao",     data: "2026", icone: "book" },
    { nome: "4 projects published on DIO",                  cat: "projeto",      data: "2026", icone: "git" },
    { nome: "12 courses completed on LinkedIn Learning",     cat: "formacao",     data: "2026", icone: "clock" },
    { nome: "10 courses completed on Udemy",                 cat: "formacao",     data: "2026", icone: "clock" },
    { nome: "MestreGrana in production [ LIVE ]",           cat: "projeto",      data: "2026", icone: "rocket" }
  ],

  filtrosConquistas: [
    { id: "todos",        label: "ALL" },
    { id: "projeto",      label: "PROJECTS" },
    { id: "formacao",     label: "EDUCATION" },
    { id: "certificacao", label: "CERTIFICATIONS" },
    { id: "comunidade",   label: "COMMUNITY" }
  ],

  /* ── AI Assistant — local knowledge base (no external API) ── */
  chat: {
    saudacao:
      "Hi! I'm vitor_ai, the portfolio assistant. I can talk about " +
      "projects, tech stack, experience, education, or contact. What do you want to know?",
    sugestoes: [
      "What is the flagship project?",
      "What is your main tech stack?",
      "Experience summary",
      "How to get in touch?"
    ],
    regras: [
      {
        keywords: ["mestregrana", "flagship", "project", "projects", "portfolio"],
        resposta:
          "The flagship project is MESTREGRANA [ PRODUCTION ] — a multi-agent financial advisor " +
          "with LangGraph orchestration, multi-LLM judge for guardrails, RAG with embeddings, and " +
          "a governance/auditing layer for responses. Other projects: FluencyForge (multi-agent " +
          "edtech), Aether Oncology (healthcare full-stack), and Harmoniz.AI (LLM pipeline). " +
          "Check the Projects & Tech Stack section for details."
      },
      {
        keywords: ["stack", "technology", "technologies", "tool", "language", "framework", "tech"],
        resposta:
          "Main stack: AI/LLM → LangGraph, LangChain, RAG, Embeddings, Multi-agent · " +
          "Backend → Python, FastAPI, Node.js · Data → PostgreSQL, MongoDB · " +
          "Frontend → React, Flutter · Infra → Docker, GCP/AWS."
      },
      {
        keywords: ["experience", "ect", "correios", "career", "work", "job", "trajectory"],
        resposta:
          "Experience summary: 15 years of mission-critical operations at ECT/Correios " +
          "(SLA governance, data auditing, fleet and logistics management), and since 2024 " +
          "working as an independent AI Engineer, building production agentic AI systems " +
          "with LangGraph, FastAPI, RAG, and Docker."
      },
      {
        keywords: ["education", "degree", "fiap", "college", "study", "graduation", "postgrad", "university"],
        resposta:
          "Education in progress: Postgraduate in ML Engineering (FIAP) and BSc in " +
          "Computer Science. Also, 80 continuous education certificates " +
          "(DIO, LinkedIn Learning, and Udemy) and the AWS AI Practitioner " +
          "(AIF-C01) certification in progress."
      },
      {
        keywords: ["certification", "certifications", "aws", "aif", "certificate"],
        resposta:
          "Current certification focus: AWS Certified AI Practitioner (AIF-C01) [ IN PROGRESS ], " +
          "with a study plan: AWS Skill Builder → Udemy → Mocks. Besides that, there are 80 " +
          "completed certificates across DIO, LinkedIn Learning, and Udemy — details in the " +
          "Certifications section."
      },
      {
        keywords: ["contact", "email", "e-mail", "linkedin", "github", "talk", "hire", "opportunity"],
        resposta:
          "To get in touch: email mkmillhouse89@gmail.com or use the LinkedIn, " +
          "GitHub, and Portfolio buttons in the Overview section. Vitor is [ AVAILABLE FOR " +
          "OPPORTUNITIES ] in a remote contract/full-time model, including international roles."
      },
      {
        keywords: ["language", "languages", "english", "spanish", "portuguese"],
        resposta:
          "Languages: Native Portuguese, Fluent English, and Intermediate Spanish."
      },
      {
        keywords: ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"],
        resposta:
          "Hello! 👋 Ask me about the flagship project, tech stack, experience, or how to get in touch."
      }
    ],
    fallback:
      "Hmm, I don't have an answer for that yet. Try asking about: projects, " +
      "tech stack, experience, education, certifications, or contact — or use the suggestions above. :)"
  }
};

/* ════════════════════════════════════════════════════════════════
   LÓGICA DE RENDERIZAÇÃO — não precisa editar daqui para baixo
   ════════════════════════════════════════════════════════════════ */
(function(){
"use strict";

const $  = (sel) => document.querySelector(sel);
const $$ = (sel) => document.querySelectorAll(sel);

/* escapa texto vindo do DATA antes de inserir em HTML */
function esc(s){
  return String(s).replace(/[&<>"']/g, c => ({
    "&":"&amp;", "<":"&lt;", ">":"&gt;", '"':"&quot;", "'":"&#39;"
  }[c]));
}

/* biblioteca mínima de ícones SVG para conquistas */
const ICONES = {
  rocket: '<svg viewBox="0 0 24 24"><path d="M5 15l-2 6 6-2"/><path d="M12 15l-3-3c1-5 4-8 10-9-1 6-4 9-9 12z"/><circle cx="14" cy="10" r="1.5"/></svg>',
  layers: '<svg viewBox="0 0 24 24"><path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/></svg>',
  book:   '<svg viewBox="0 0 24 24"><path d="M4 4h7v16H6a2 2 0 0 1-2-2z"/><path d="M20 4h-7v16h5a2 2 0 0 0 2-2z"/></svg>',
  clock:  '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg>',
  award:  '<svg viewBox="0 0 24 24"><circle cx="12" cy="9" r="6"/><path d="M8.5 14L7 22l5-3 5 3-1.5-8"/></svg>',
  git:    '<svg viewBox="0 0 24 24"><circle cx="6" cy="6" r="2.5"/><circle cx="6" cy="18" r="2.5"/><circle cx="18" cy="12" r="2.5"/><path d="M6 8.5v7M8 7l7.5 4"/></svg>'
};
const iconeDe = (n) => ICONES[n] || ICONES.award;

/* ── STARFIELD — estrelas sutis em movimento (canvas) ──────────── */
(function starfield(){
  const cv = $("#starfield");
  const ctx = cv.getContext("2d");
  let estrelas = [];
  function dimensiona(){
    cv.width = innerWidth;
    cv.height = innerHeight;
    const qtd = Math.min(160, Math.floor(innerWidth * innerHeight / 9000));
    estrelas = Array.from({ length: qtd }, () => ({
      x: Math.random() * cv.width,
      y: Math.random() * cv.height,
      r: Math.random() * 1.3 + .2,
      v: Math.random() * .25 + .05,          /* velocidade vertical */
      a: Math.random() * .5 + .15            /* alpha base */
    }));
  }
  function desenha(){
    ctx.clearRect(0, 0, cv.width, cv.height);
    for (const e of estrelas){
      e.y -= e.v;                            /* deriva suave para cima */
      if (e.y < -2){ e.y = cv.height + 2; e.x = Math.random() * cv.width; }
      const tw = e.a + Math.sin(Date.now() / 900 + e.x) * .12;  /* cintilação */
      ctx.fillStyle = "rgba(0,255,65," + Math.max(.05, tw * .55) + ")";
      ctx.fillRect(e.x, e.y, e.r, e.r);      /* pixel quadrado = estética terminal */
    }
    requestAnimationFrame(desenha);
  }
  addEventListener("resize", dimensiona);
  dimensiona();
  desenha();
})();

/* ── NAVEGAÇÃO SPA ─────────────────────────────────────────────── */
const NOMES_BREADCRUMB = {
  painel: "painel-geral", perfil: "perfil", experiencia: "experiencia",
  formacao: "formacao", projetos: "projetos", certificacoes: "certificacoes",
  conquistas: "conquistas", assistente: "assistente-ia"
};

function mostraSecao(id){
  $$(".secao").forEach(s => s.classList.remove("ativa"));
  $("#secao-" + id).classList.add("ativa");
  $$(".nav-item").forEach(b => b.classList.toggle("ativa", b.dataset.secao === id));
  $("#breadcrumbSecao").textContent = NOMES_BREADCRUMB[id] || id;
  fechaMenuMobile();
  window.scrollTo({ top: 0 });
  /* dispara animações dependentes de visibilidade da seção */
  if (id === "formacao")      animaProgressos("#secao-formacao .progress__fill");
  if (id === "certificacoes"){ animaProgressos("#secao-certificacoes .progress__fill"); animaBarras(); }
}

$("#navPrincipal").addEventListener("click", (ev) => {
  const btn = ev.target.closest(".nav-item");
  if (btn) mostraSecao(btn.dataset.secao);
});

/* ── MENU MOBILE (hamburger) ───────────────────────────────────── */
const sidebar  = $("#sidebar");
const hamb     = $("#hamburger");
const backdrop = $("#backdrop");
function fechaMenuMobile(){
  sidebar.classList.remove("aberta");
  hamb.classList.remove("aberto");
  hamb.setAttribute("aria-expanded", "false");
  backdrop.classList.remove("visivel");
}
hamb.addEventListener("click", () => {
  const aberto = sidebar.classList.toggle("aberta");
  hamb.classList.toggle("aberto", aberto);
  hamb.setAttribute("aria-expanded", String(aberto));
  backdrop.classList.toggle("visivel", aberto);
});
backdrop.addEventListener("click", fechaMenuMobile);

/* ── TYPEWRITER do título do painel ────────────────────────────── */
(function typewriter(){
  const alvo = $("#typedTitulo");
  const texto = DATA.nome;
  let i = 0;
  (function tique(){
    if (i <= texto.length){
      alvo.textContent = texto.slice(0, i++);
      setTimeout(tique, 38);
    }
  })();
})();

/* ── COUNT-UP das métricas (dispara ao entrar na viewport) ─────── */
function countUp(el, fim, sufixo){
  const dur = 1300;
  const t0 = performance.now();
  (function frame(t){
    const p = Math.min(1, (t - t0) / dur);
    const eased = 1 - Math.pow(1 - p, 3);              /* easeOutCubic */
    el.textContent = Math.round(fim * eased) + sufixo;
    if (p < 1) requestAnimationFrame(frame);
  })(t0);
}

/* ── RENDER: Painel Geral ──────────────────────────────────────── */
$("#heroStatus").innerHTML =
  '<span>📍 ' + esc(DATA.localizacao) + '</span> · <span class="tag">' + esc(DATA.disponibilidade) + '</span>';

$("#metricasGrid").innerHTML = DATA.metricas.map(m =>
  '<div class="metric-card">' +
    '<div class="metric-num" data-valor="' + m.valor + '" data-sufixo="' + esc(m.sufixo) + '">0</div>' +
    '<div class="metric-label">' + esc(m.label) + '</div>' +
  '</div>'
).join("");

/* observa as métricas e dispara o count-up uma única vez */
const obsMetricas = new IntersectionObserver((entradas) => {
  entradas.forEach(e => {
    if (e.isIntersecting){
      const el = e.target;
      countUp(el, Number(el.dataset.valor), el.dataset.sufixo);
      obsMetricas.unobserve(el);
    }
  });
}, { threshold: .4 });
$$(".metric-num").forEach(el => obsMetricas.observe(el));

$("#posicionamento").innerHTML =
  '<span class="prompt">$ cat positioning.txt</span><br>' +
  '<span class="out">' + esc(DATA.posicionamento) + '</span>';

$("#deployCard").innerHTML =
  '<h3>Último deploy</h3>' +
  '<div class="deploy-nome">' + esc(DATA.ultimoDeploy.nome) + '</div>' +
  '<span class="tag">' + esc(DATA.ultimoDeploy.status) + '</span>' +
  '<p style="color:var(--txt-dim);font-size:12.5px;margin-top:12px;">' + esc(DATA.ultimoDeploy.descricao) + '</p>';

$("#botoesLinks").innerHTML =
  '<a class="btn" href="' + esc(DATA.links.linkedin) + '" target="_blank" rel="noopener">LinkedIn</a>' +
  '<a class="btn" href="' + esc(DATA.links.github) + '" target="_blank" rel="noopener">GitHub</a>' +
  '<a class="btn btn--solid" href="' + esc(DATA.links.portfolio) + '" target="_blank" rel="noopener">Portfolio</a>' +
  '<a class="btn" href="' + esc(DATA.links.email) + '">E-mail</a>';

/* ── RENDER: Perfil ────────────────────────────────────────────── */
$("#resumoExecutivo").textContent = DATA.resumoExecutivo;

const linhaDado = (d) =>
  '<div class="dado-linha"><span class="k">' + esc(d.k) + '</span><span class="v">' + esc(d.v) + '</span></div>';
$("#dadosGrid").innerHTML      = DATA.dados.map(linhaDado).join("");
$("#diretrizesGrid").innerHTML = DATA.diretrizes.map(linhaDado).join("");
$("#pilaresLista").innerHTML   = DATA.pilares.map(p => "<li>" + esc(p) + "</li>").join("");

/* ── RENDER: Experiência (timeline) ────────────────────────────── */
$("#timelineExp").innerHTML = DATA.experiencia.map(x =>
  '<div class="tl-no">' +
    '<div class="card">' +
      '<div class="tl-periodo">' + esc(x.periodo) + '</div>' +
      '<div style="display:flex;flex-wrap:wrap;align-items:center;gap:10px;">' +
        '<span class="tl-cargo">' + esc(x.cargo) + '</span>' +
        '<span class="tag tag--cyan">' + esc(x.badge) + '</span>' +
      '</div>' +
      '<div class="tl-org">' + esc(x.org) + '</div>' +
      '<ul class="tl-bullets">' + x.bullets.map(b => "<li>" + esc(b) + "</li>").join("") + '</ul>' +
      (x.stack.length
        ? '<div class="tl-stack">' + x.stack.map(s => '<span class="tag tag--dim">' + esc(s) + '</span>').join("") + '</div>'
        : "") +
    '</div>' +
  '</div>'
).join("");

/* ── RENDER: Formação ──────────────────────────────────────────── */
$("#formacaoGrid").innerHTML = DATA.formacao.map(f =>
  '<div class="card">' +
    '<div style="display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin-bottom:6px;">' +
      '<h3 style="margin:0;">' + esc(f.curso) + '</h3>' +
      '<span class="tag tag--amber">' + esc(f.status) + '</span>' +
    '</div>' +
    '<div style="color:var(--txt-dim);font-size:12.5px;">' + esc(f.instituicao) + '</div>' +
    '<div class="progress"><div class="progress__fill" data-progresso="' + f.progresso + '"></div></div>' +
    '<div class="progress-label"><span>progresso</span><span style="color:var(--neon);">' + f.progresso + '%</span></div>' +
    '<p style="font-size:12.5px;margin-top:12px;">' + esc(f.foco) + '</p>' +
    '<div style="color:var(--txt-dim);font-size:11.5px;margin-top:8px;">previsão: ' + esc(f.previsao) + '</div>' +
    '<div class="disciplinas">' + f.disciplinas.map(d => '<span class="tag tag--dim">' + esc(d) + '</span>').join("") + '</div>' +
  '</div>'
).join("");

/* anima barras de progresso (formação e cert) quando a seção abre */
function animaProgressos(seletor){
  requestAnimationFrame(() => {
    $$(seletor).forEach(el => { el.style.width = el.dataset.progresso + "%"; });
  });
}

/* ── RENDER: Projetos & filtros ────────────────────────────────── */
function montaFiltros(containerSel, filtros, aoFiltrar){
  const cont = $(containerSel);
  cont.innerHTML = filtros.map((f, i) =>
    '<button class="filtro-btn' + (i === 0 ? " ativa" : "") + '" data-filtro="' + f.id + '">' + esc(f.label) + '</button>'
  ).join("");
  cont.addEventListener("click", (ev) => {
    const btn = ev.target.closest(".filtro-btn");
    if (!btn) return;
    cont.querySelectorAll(".filtro-btn").forEach(b => b.classList.toggle("ativa", b === btn));
    aoFiltrar(btn.dataset.filtro);
  });
}

$("#projetosGrid").innerHTML = DATA.projetos.map(p =>
  '<article class="projeto-card' + (p.flagship ? " flagship" : "") + '" data-cats="' + p.categorias.join(" ") + '">' +
    '<div class="projeto-head">' +
      '<span class="projeto-nome">' + esc(p.nome) + '</span>' +
      p.tags.map(t => '<span class="tag">' + esc(t) + '</span>').join("") +
    '</div>' +
    '<p class="projeto-desc">' + esc(p.descricao) + '</p>' +
    /* arquitetura usa <strong> controlado pelo DATA (conteúdo próprio, não input externo) */
    '<p class="projeto-arq">' + p.arquitetura + '</p>' +
    '<div class="stack-tags">' + p.stack.map(s => '<span class="tag tag--dim">' + esc(s) + '</span>').join("") + '</div>' +
    (p.diagrama ? '<pre class="ascii-diagrama">' + esc(p.diagrama) + '</pre>' : "") +
    '<div class="projeto-metricas">' +
      p.metricas.map(m => '<span>' + esc(m.k) + ': <b>' + esc(m.v) + '</b></span>').join("") +
    '</div>' +
    '<div class="botoes-links">' +
      p.links.map(l => '<a class="btn' + (l.solid ? " btn--solid" : "") + '" href="' + esc(l.url) + '" target="_blank" rel="noopener">' + esc(l.label) + '</a>').join("") +
    '</div>' +
  '</article>'
).join("");

montaFiltros("#filtrosProjetos", DATA.filtrosProjetos, (filtro) => {
  $$("#projetosGrid .projeto-card").forEach(card => {
    const cats = card.dataset.cats.split(" ");
    card.classList.toggle("oculto", filtro !== "todos" && !cats.includes(filtro));
  });
});

$("#stackGrupos").innerHTML = DATA.stackCompleto.map(g =>
  '<div class="stack-grupo">' +
    '<span class="grupo-nome">' + esc(g.grupo) + '</span>' +
    g.itens.map(i => '<span class="tag tag--dim">' + esc(i) + '</span>').join("") +
  '</div>'
).join("");

/* ── RENDER: Certificações ─────────────────────────────────────── */
const cd = DATA.certDestaque;
$("#certDestaque").innerHTML =
  '<div style="display:flex;flex-wrap:wrap;align-items:center;gap:10px;">' +
    '<h3 style="font-family:var(--font-tit);font-size:17px;color:#fff;margin:0;">' + esc(cd.nome) + '</h3>' +
    '<span class="tag tag--amber">' + esc(cd.status) + '</span>' +
  '</div>' +
  '<div class="progress"><div class="progress__fill" data-progresso="' + cd.progresso + '"></div></div>' +
  '<div class="progress-label"><span>preparação</span><span style="color:var(--neon);">' + cd.progresso + '%</span></div>' +
  '<div class="cert-plano">plano: ' +
    cd.plano.map(p => '<span class="tag tag--dim">' + esc(p) + '</span>').join('<span class="seta">→</span>') +
  '</div>' +
  '<div style="color:var(--txt-dim);font-size:11.5px;margin-top:10px;">previsão: ' + esc(cd.previsao) + '</div>';

$("#cursosGrid").innerHTML = DATA.cursos.map(c =>
  '<div class="curso-card" data-cat="' + esc(c.cat) + '">' +
    '<div class="curso-nome">' + esc(c.nome) + '</div>' +
    '<div class="curso-meta"><span>' + esc(c.inst) + '</span><span>' + esc(c.horas) + ' · ' + esc(c.data) + '</span></div>' +
  '</div>'
).join("");

montaFiltros("#filtrosCursos", DATA.filtrosCursos, (filtro) => {
  $$("#cursosGrid .curso-card").forEach(card => {
    card.classList.toggle("oculto", filtro !== "todos" && card.dataset.cat !== filtro);
  });
});

/* gráfico de barras horizontal (CSS puro, largura proporcional) */
const maxHoras = Math.max(...DATA.horasPorArea.map(h => h.horas));
$("#graficoLinhas").innerHTML = DATA.horasPorArea.map(h =>
  '<div class="grafico-linha">' +
    '<span class="area">' + esc(h.area) + '</span>' +
    '<div class="barra-track"><div class="barra-fill" data-pct="' + Math.round(h.horas / maxHoras * 100) + '"></div></div>' +
    '<span class="horas">' + h.horas + 'h</span>' +
  '</div>'
).join("");

/* gráfico de XP por habilidade (DIO) — top 12, mesma estética */
const topHabilidades = DATA.habilidades.slice(0, 12);
const maxXP = Math.max(...topHabilidades.map(h => h.xp));
$("#graficoXPLinhas").innerHTML = topHabilidades.map(h =>
  '<div class="grafico-linha">' +
    '<span class="area">' + esc(h.nome) + '</span>' +
    '<div class="barra-track"><div class="barra-fill" data-pct="' + Math.round(h.xp / maxXP * 100) + '"></div></div>' +
    '<span class="horas">' + h.xp + 'xp</span>' +
  '</div>'
).join("");

function animaBarras(){
  requestAnimationFrame(() => {
    $$("#secao-certificacoes .barra-fill").forEach(el => { el.style.width = el.dataset.pct + "%"; });
  });
}

/* ── RENDER: Conquistas ────────────────────────────────────────── */
$("#conquistasContador").textContent =
  DATA.conquistas.length + " conquistas registradas · filtre por categoria";

const ultima = DATA.conquistas[0];
$("#ultimaConquista").innerHTML =
  iconeDe(ultima.icone) +
  '<div>' +
    '<div style="font-size:11px;color:var(--neon);letter-spacing:.1em;margin-bottom:4px;">ÚLTIMA CONQUISTA DESBLOQUEADA</div>' +
    '<div style="font-family:var(--font-tit);font-weight:700;color:#fff;">' + esc(ultima.nome) + '</div>' +
    '<div style="color:var(--txt-dim);font-size:11.5px;margin-top:3px;">' + esc(ultima.cat) + ' · ' + esc(ultima.data) + '</div>' +
  '</div>';

$("#badgesGrid").innerHTML = DATA.conquistas.map(c =>
  '<div class="badge-card" data-cat="' + esc(c.cat) + '">' +
    iconeDe(c.icone) +
    '<div>' +
      '<div class="badge-nome">' + esc(c.nome) + '</div>' +
      '<div class="badge-meta">' + esc(c.cat) + ' · ' + esc(c.data) + '</div>' +
    '</div>' +
  '</div>'
).join("");

montaFiltros("#filtrosConquistas", DATA.filtrosConquistas, (filtro) => {
  $$("#badgesGrid .badge-card").forEach(card => {
    card.classList.toggle("oculto", filtro !== "todos" && card.dataset.cat !== filtro);
  });
});

/* ── ASSISTENTE IA — chat local por palavras-chave ─────────────────
   ▼▼▼ INTEGRAÇÃO FUTURA COM GEMINI API ▼▼▼
   Para trocar o matching local por um LLM real, substitua a função
   `respondeLocal(pergunta)` por uma chamada assíncrona, por exemplo:

     async function respondeLLM(pergunta){
       const r = await fetch(
         "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=SUA_KEY",
         { method: "POST", headers: { "Content-Type": "application/json" },
           body: JSON.stringify({ contents: [{ parts: [{ text: pergunta }] }] }) }
       );
       const j = await r.json();
       return j.candidates[0].content.parts[0].text;
     }

   IMPORTANTE: não exponha a API key no frontend em produção —
   use um backend/proxy (ex: endpoint FastAPI) para fazer a chamada.
   ▲▲▲ FIM DA NOTA DE INTEGRAÇÃO ▲▲▲                                */

function normaliza(s){
  return s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
}

function respondeLocal(pergunta){
  const q = normaliza(pergunta);
  for (const regra of DATA.chat.regras){
    if (regra.keywords.some(k => q.includes(normaliza(k)))) return regra.resposta;
  }
  return DATA.chat.fallback;
}

const chatCorpo = $("#chatCorpo");

function addMsgUser(texto){
  const div = document.createElement("div");
  div.className = "msg msg--user";
  div.textContent = texto;
  chatCorpo.appendChild(div);
  chatCorpo.scrollTop = chatCorpo.scrollHeight;
}

/* mensagem do bot com efeito de digitação */
function addMsgBot(texto, instantaneo){
  const div = document.createElement("div");
  div.className = "msg msg--bot";
  div.innerHTML = '<span class="msg-prefixo">vitor_ai&gt;</span> <span class="msg-texto"></span>';
  chatCorpo.appendChild(div);
  const alvo = div.querySelector(".msg-texto");
  if (instantaneo){
    alvo.textContent = texto;
    chatCorpo.scrollTop = chatCorpo.scrollHeight;
    return;
  }
  let i = 0;
  (function tique(){
    if (i <= texto.length){
      alvo.textContent = texto.slice(0, i);
      i += 2;                                /* 2 chars por tique = digitação ágil */
      chatCorpo.scrollTop = chatCorpo.scrollHeight;
      setTimeout(tique, 14);
    }
  })();
}

/* sugestões clicáveis */
$("#chatSugestoes").innerHTML = DATA.chat.sugestoes.map(s =>
  '<button type="button" class="sugestao">' + esc(s) + '</button>'
).join("");
$("#chatSugestoes").addEventListener("click", (ev) => {
  const btn = ev.target.closest(".sugestao");
  if (!btn) return;
  enviaPergunta(btn.textContent);
});

function enviaPergunta(texto){
  const t = texto.trim();
  if (!t) return;
  addMsgUser(t);
  setTimeout(() => addMsgBot(respondeLocal(t)), 350);   /* pequena pausa "pensando" */
}

$("#chatForm").addEventListener("submit", (ev) => {
  ev.preventDefault();
  const input = $("#chatInput");
  enviaPergunta(input.value);
  input.value = "";
});

/* saudação inicial */
addMsgBot(DATA.chat.saudacao, true);

/* ── ano no footer da sidebar ──────────────────────────────────── */
$("#anoAtual").textContent = new Date().getFullYear();

})();
