<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=00ff41&height=200&section=header&text=Vitor%20Silva&fontSize=50&fontColor=ffffff&desc=AI%20Software%20Engineer&descAlignY=70&descAlign=50" alt="Vitor Silva - AI Software Engineer" />
</p>

<p align="center">
  <a href="https://vitorsilva.page"><img src="https://img.shields.io/badge/Portfolio-vitorsilva.page-00ff41?style=for-the-badge&logo=vercel&logoColor=white" /></a>
  <a href="https://linkedin.com/in/vitorsilva-aieng"><img src="https://img.shields.io/badge/LinkedIn-vitorsilva--aieng-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="https://github.com/vdfs89"><img src="https://img.shields.io/badge/GitHub-vdfs89-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
  <a href="mailto:vitor@vitorsilva.page"><img src="https://img.shields.io/badge/Email-Hire%20Me-EA4335?style=for-the-badge&logo=gmail&logoColor=white" /></a>
</p>

<p align="center">
  <b>Building production-grade AI systems with LangGraph • FastAPI • Python • RAG • Multi-Agent Systems</b>
</p>

---

## Hi, I'm Vitor Silva 👋

### AI Software Engineer | LLM Engineering • Agentic AI • Backend Python

> I build AI systems that **don't break in production.**

Most AI projects die in the demo. Mine are designed for the part nobody likes to talk about: **reliability, governance, and not hallucinating in front of a real user.**

I bring **14 years of mission-critical operations** into modern AI engineering — someone who understands **LangGraph stateful orchestration and multi-LLM guardrails** *and* what it actually costs when a system fails at scale.

📍 Curitiba, Brazil · **Open to international remote**

---

## 🚀 Anchor Projects

### 💰 [MestreGrana — Multi-Agent Financial Platform](https://github.com/vdfs89/InvestimentoDIO)
**Problem:** LLM hallucinations in high-stakes financial advice destroy trust and create legal exposure.
**Solution:** Multi-LLM judge architecture where every output is audited before reaching the user.
**Impact:** 4 specialized agents • 100% audited outputs • sub-200ms RAG retrieval • zero unvalidated responses in production
**Stack:** `LangGraph` `FastAPI` `Python` `MongoDB` `RAG`

### 🎓 [FluencyForge — Multi-Agent EdTech Platform](https://fluencyforge.streamlit.app/)
**Problem:** Static learning paths fail to adapt to real user progress and context.
**Solution:** Stateful LangGraph orchestrator with long-term memory and real-time RAG personalization.
**Impact:** Dynamic curriculum generation • continuous context across sessions • multi-tool AI integration
**Stack:** `LangGraph` `FastAPI` `RAG` `Vector DB` `Python`

### 🧬 [Aether Oncology — Clinical ML Platform](https://github.com/vdfs89/Aether_Oncology)
**Problem:** Oncology screening with manual processes creates delays and errors in critical decisions.
**Solution:** ML pipeline for safe, auditable AI-assisted clinical triage.
**Impact:** End-to-end ML pipeline • FastAPI backend • React + Flutter frontend • production-ready architecture
**Stack:** `Python` `FastAPI` `PyTorch` `React` `Flutter` `MLOps`

### 🍷 [Harmoniz.AI — RAG Recommendation Engine](https://github.com/vdfs89/Harmoniz.AI)
**Problem:** Generic product recommendations fail to capture nuanced user preferences.
**Solution:** RAG-based generative AI engine with semantic search and LLM-powered curation.
**Impact:** Semantic retrieval pipeline • LLM-scored recommendations • Streamlit + FastAPI interface
**Stack:** `Python` `LangChain` `RAG` `ChromaDB` `FastAPI` `Streamlit`

### 📊 [RetentIA — Churn Prediction ML System](https://github.com/vdfs89/RetentIA)
**Problem:** Customer churn detected too late to act.
**Solution:** MLP PyTorch model with FastAPI serving and MLflow experiment tracking.
**Impact:** 89.8% recall at a cost-weighted threshold • ROC-AUC 0.845, nearly identical to XGBoost (the value is the threshold, not the architecture) • MLflow tracking • Prometheus metrics • CI
**Stack:** `PyTorch` `FastAPI` `MLflow` `XGBoost` `Python` `Docker`

---

### 🛒 [TwinRank AI — Two-Tower Recommender](https://github.com/vdfs89/TwinRankAI)
**Problem:** Popularity-based recommendation systems collapse into generic suggestions and fail at real personalization.
**Solution:** Two-Tower neural collaborative filtering with a versioned, reproducible training pipeline.
**Impact:** Recall@10 of 0.123 vs 0.0034 for the popularity baseline (part of the gain is repeated items; the model still leads on pure discovery) • DVC-tracked datasets • MLflow experiment tracking • FastAPI serving
**Demo:** [live app](https://twinrankai.streamlit.app/) · [video walkthrough](https://youtu.be/YUeemzMXzqA)
**Stack:** `PyTorch` `Two-Tower NN` `FastAPI` `DVC` `MLflow`

### ⚙️ VektorWork — Privacy-First Multi-Agent Platform *(private repository)*
**Problem:** AI tools for careers and freelancing send sensitive data, like CVs and expectations, to third-party clouds.
**Solution:** Two isolated LangGraph pipelines behind a FastAPI gateway: a career mode that runs 100% local on Ollama, and a freelance mode on cloud inference.
**Impact:** Local-first execution for personal data • a reviewer agent as the quality gate • Flutter and Electron clients
**Stack:** `FastAPI` `LangGraph` `Ollama` `Flutter` `Playwright` `Docker`

### 🏥 [AIClinicOS — Clinic Management SaaS](https://ai-clinic-os.vercel.app/)
**Problem:** Modern clinics juggle patient data across disconnected tools, costing time on every appointment.
**Solution:** Full-stack operating system for clinics with integrated scheduling, records, and AI-assisted workflows.
**Impact:** Next.js app with server-side rendering • Supabase auth and persistence • live production deployment
**Stack:** `Next.js` `TypeScript` `Tailwind` `Supabase`

### 🏢 [Rankium Systems — Multi-Tenant B2B Platform](https://rankiumsystems.com.br/)
**Problem:** B2B service operations need one governed platform for leads, contracts and payments, with each organization's data kept apart.
**Solution:** Core platform with identity, organizations, RBAC, billing and audit trail, plus pluggable suites for agency, marketplace and CRM work.
**Impact:** Live in production • Stripe Connect escrow • real-time chat • 261 cross-tenant isolation checks passing on a test database (row-level security is written and validated, not yet enabled in production)
**Stack:** `FastAPI` `Next.js` `PostgreSQL` `Redis` `Stripe`

### 🩺 [VITORIUM — MLOps Pipeline for Medical Text](https://github.com/vdfs89/vitorium-mednlp-mlops)
**Problem:** A hospital needs incoming medical reports triaged by urgency, with a model that can be retrained, monitored and served fast.
**Solution:** TF-IDF and logistic regression baseline served by FastAPI, exported to ONNX Runtime, retrained through an Airflow DAG and monitored with Prometheus and Grafana.
**Impact:** p95 API latency of 3.07 ms on the baseline • macro F1 0.62 on heuristic urgency labels (didactic mapping, not clinical) • CI with lint, tests and image build
**Stack:** `Python` `FastAPI` `ONNX` `Airflow` `Docker` `Prometheus`

### 🏋️ Corpo em Ação — Workout Tracker
**Problem:** Generic training apps ignore the user's goal and equipment, and give no clear view of progress.
**Solution:** Flutter app with personalized plans, timer-driven sessions, progress charts and AI suggestions with an offline fallback.
**Stack:** `Flutter` `Dart` `Hive` `OpenAI API`

---

## 🛠️ Core Stack

| Domain | Technologies |
|---|---|
| **AI & Agents** | LangGraph, LangChain, RAG, Multi-LLM Guardrails, Agentic AI |
| **Backend** | Python, FastAPI, Async, REST APIs |
| **ML/MLOps** | PyTorch, Scikit-learn, MLflow, XGBoost, Docker |
| **Databases** | PostgreSQL, MongoDB, ChromaDB, Vector DBs |
| **Cloud & DevOps** | AWS, Azure, Google Cloud, Docker, GitHub Actions, CI/CD |
| **Frontend** | React, Node.js, Flutter / Dart |

---

## 📊 GitHub Activity

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=vdfs89&show_icons=true&theme=dark&hide_border=true&count_private=true&rank_icon=github" alt="GitHub Stats" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=vdfs89&layout=compact&theme=dark&hide_border=true&langs_count=8" alt="Top Languages" />
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=vdfs89&theme=dark&hide_border=true" alt="GitHub Streak" />
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/vdfs89/vdfs89/output/github-contribution-grid-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/vdfs89/vdfs89/output/github-contribution-grid-snake.svg" />
    <img src="https://raw.githubusercontent.com/vdfs89/vdfs89/output/github-contribution-grid-snake.svg" alt="Contribution graph snake animation" />
  </picture>
</p>

---

## 💬 Currently

- 🔭 **B.Sc. Computer Science** (final year) + **Postgrad ML Engineering @ FIAP**
- 🎯 Focused on: LangGraph production systems, AI governance, multi-LLM architectures
- 🌎 **Open to:** International remote • AI Engineer • ML Engineer • Backend Python
- 💼 **Hire me:** [vitorsilva.page](https://vitorsilva.page) • [LinkedIn](https://linkedin.com/in/vitorsilva-aieng)

---

<p align="center">
  <i>"The maturity of someone who operated systems that cannot stop — applied to reliable AI agents for the real world."</i>
</p>
