# Vitor Silva
**AI-First Software Engineer & Solutions Architect**
*Designing production-grade multi-agent systems, advanced RAG architectures, and highly resilient software systems.*

Curitiba - PR, Brazil (Open to Remote / Hybrid / Global Opportunities)
[LinkedIn](https://www.linkedin.com/in/vitorsilva-aieng/) | [GitHub](https://github.com/vdfs89) | [Official Portfolio](https://vitorsilva.page/) | [Email](mailto:vitor_diogo89@hotmail.com)

---

## 🚀 Executive Summary

**How mission-critical operational maturity translates into robust AI engineering.**

A strategic career transition consolidated by **15 years of leadership in processes and mission-critical operations** at the Brazilian Postal Service (ECT), where risk management, operational resilience under pressure, and strict SLA compliance were the daily metrics of success. Currently in the final stretch of my **BSc in Computer Science** and specializing in **Machine Learning Engineering at FIAP**, I bring this mindset of high corporate reliability to advanced software engineering.

My specialization is the **AI-First** philosophy: not just integrating LLM APIs into conventional products, but structuring new paradigms for complex systems. I am an expert in creating **asynchronous agentic architectures with LangGraph**, deterministic hallucination mitigation in enterprise RAG systems, intelligent document processing (IDP), and structuring solid pipelines for observability and continuous evaluation.

---

## 🛠️ Hard Skills Grid (Architecture & Engineering)

```
┌───────────────────────────────────────┐   ┌───────────────────────────────────────┐
│       ARTIFICIAL INTELLIGENCE (AI)    │   │         BACKEND & INTEGRATION         │
├───────────────────────────────────────┤   ├───────────────────────────────────────┤
│ • Multi-Agent Orchestration(LangGraph)│   │ • Python (FastAPI, Streamlit, Flask)  │
│ • Advanced Hallucination Mitigation   │   │ • Node.js (JavaScript / TypeScript)   │
│ • RAG Pipelines & Semantic Chunking   │   │ • Async Programming / Concurrency     │
│ • Data Governance & Curation          │   │ • Web Protocols (REST, WebSockets)    │
│ • Observability (LangSmith & Evals)   │   │ • State-Machine Logic & Determinism   │
└───────────────────────────────────────┘   └───────────────────────────────────────┘
┌───────────────────────────────────────┐   ┌───────────────────────────────────────┐
│       INFRASTRUCTURE & MLOPs          │   │               DATABASES               │
├───────────────────────────────────────┤   ├───────────────────────────────────────┤
│ • Containerization (Docker)           │   │ • Vector DBs (Pinecone, PGVector)     │
│ • Cloud Computing (Azure Services)    │   │ • NoSQL (MongoDB)                     │
│ • Automated CI/CD (GitHub Actions)    │   │ • Relational (PostgreSQL)             │
│ • Serverless Architecture             │   │ • Complex Ingestion ETL Pipelines     │
│ • Data Drift Metrics Monitoring       │   │ • Unstructured Data Modeling          │
└───────────────────────────────────────┘   └───────────────────────────────────────┘
```

---

## 🏆 Engineering Showcase (Featured Projects)

### 📈 1. MestreGrana — Financial Multi-Agent Orchestrator
*Advanced financial intelligence platform structured on a network of autonomous specialist agents for planning and regulatory auditing.*

*   **Core Stack:** Python, LangGraph, Streamlit, MongoDB.
*   **The Business Approach:** Replaces linear prompt engineering with a committee of agents (planners, auditors, and validators) working collaboratively to structure robust investment plans in full regulatory compliance.
*   **⚡ The Technical Challenge Overcome:** 
    *   *Hallucination Mitigation:* In finance, data hallucination can cost millions or violate regulatory rules. I developed a deterministic cross-validation loop in LangGraph, where a Compliance Agent analyzes generated outputs by confronting them with structured market APIs and fixed rules. If there is a data discrepancy greater than 0%, the flow self-corrects and restarts.
    *   *Complex State Persistence:* Implemented a custom LangGraph checkpointing system in MongoDB, allowing the exact state of the conversation and decision trees to be saved. This ensures that connection interruptions or long-running async sessions can be resumed without losing historical progress.
*   **Links:** 🐙 [GitHub Code](https://github.com/vdfs89/MestreGrana) | 🌐 [Live Demo](https://mestregrana.streamlit.app/)

---

### 🎓 2. FluencyForge — Adaptive Technical English Tutor
*Intelligent ecosystem that creates tech-English learning paths based on the user's real-time difficulties and context.*

*   **Core Stack:** FastAPI, Flutter, LangGraph, PostgreSQL.
*   **The Business Approach:** A mobile and backend ecosystem aimed at tech-business learning, measuring user retention and progress through personalized contextual interactions.
*   **⚡ The Technical Challenge Overcome:** 
    *   *Async Streaming and Latency:* Real-time conversation response requires extremely high-speed processing. I solved latency by implementing bi-directional data streaming using async endpoints in FastAPI integrated with audio/text streams in Flutter. The heavy processing of grammar evaluation runs non-blocking in the background, allowing the response voice or text to be generated in parts (tokens) even before the full analysis finishes, reducing perceived response time to under 800ms.
*   **Links:** 🌐 [Live Demo](https://fluencyforge.streamlit.app/)

---

### 🏥 3. Aether Oncology — Clinical Cockpit & Predictive Diagnostics
*High-density medical platform for oncological diagnostics, integrating Explainable AI (XAI) deep learning models with a premium, interactive clinical interface.*

*   **Core Stack:** Next.js, PyTorch, FastAPI, Tailwind CSS, Docker.
*   **The Business Approach:** Replaces confusing diagnostic terminals with a high-density visual clinical cockpit (bento-grid of clinical data, 3D guide star visualization, and XAI) that delivers fast tumor prognostics with auditable explanations for oncologists.
*   **⚡ The Technical Challenge Overcome:** 
    *   *Model Explainability (XAI) and Inference Latency:* Integrating deep neural network (PyTorch) predictions in real-time without compromising clinical trust. I developed an async pipeline in FastAPI that processes exams and generates explanatory heatmaps (integrated gradients) of pixel attribution, returning the payload in under 1.2 seconds.
    *   *Interactive Guide Star Rendering (GPU):* Designing a high-fidelity clinical dashboard while keeping the interface lightweight and responsive. I bypassed the browser's main thread bottleneck by delegating the vector physics calculation and rendering of the dynamic guide star ("Pulsating Lotus") to GPU-accelerated WebGL shaders, ensuring a stable 60fps.
*   **Links:** 🐙 [GitHub Code](https://github.com/vdfs89/Aether_Oncology)

---

### 📈 4. Harmoniz.AI — Biometric Data Correlator
*Correlation of complex biometric data with LLM pipelines to optimize human performance.*

*   **Core Stack:** Python, Pandas, LLM Pipeline, Streamlit.
*   **Links:** 🐙 [GitHub Code](https://github.com/vdfs89/Harmoniz.AI) | 🌐 [Live Demo](https://harmonizai.streamlit.app/)

---

### 🛒 5. TwinRank AI — Deep Learning Recommendation
*Two-Tower Neural Network for E-commerce recommendations.*

*   **Core Stack:** PyTorch, FastAPI, DVC, MLflow.
*   **Status:** IN DEVELOPMENT

---

### ⚙️ 6. VektorWork — AI Orchestration SaaS
*Self-hosted automation platform for freelancers.*

*   **Core Stack:** n8n, Docker Compose, PostgreSQL, Redis.
*   **Status:** Private Repository

---

### 🔮 7. RetentIA — Predictive Churn Engine
*Predictive churn engine for B2B SaaS using Machine Learning.*

*   **Core Stack:** Python, Scikit-learn, XGBoost, FastAPI.
*   **Status:** Private Repository

---

### 🏥 8. AIClinicOS — Clinic Management OS
*Modern intelligent OS for clinic data and patient care management.*

*   **Core Stack:** Next.js, Tailwind, Supabase.
*   **Links:** 🌐 [Live Demo](https://ai-clinic-os.vercel.app/)

---

## ⏳ Professional Timeline

### 🎓 Cutting-Edge Academic Background
*   **Postgraduate in Machine Learning Engineering**
    *   *FIAP* | Ongoing
    *   *Practical focus:* MLOps, deep learning, feature engineering, scalable deployment of enterprise LLMs, and continuous evaluation against data drift.
*   **BSc in Computer Science**
    *   *Descomplica Digital University* | Senior Year (Graduation 2026)
    *   *Practical focus:* Solid foundation in complex data structures, algorithmic complexity analysis, theory of computation, and data security.

### 🏢 Leadership & Operational Governance
*   **Process and Mission-Critical Operations Manager**
    *   *Brazilian Postal Service (ECT)* | 2011 — Present (15 Years)
    *   *Core Delivery:* Technical coordination and management of high-pressure operational teams. Responsible for critical delivery SLAs, federal audits, complex operational risk mitigation, and absolute legal compliance assurance.
    *   *Technological Transposition:* This deep operational experience grants the maturity needed to design software from the perspective of extreme reliability, system resilience, and structured defensive logs against failures.

---

## 📬 Direct Contact

I am always open to speaking with **CTOs, Engineering Managers, and Startup Founders** looking for engineers focused on creating real products and robust AI systems.

*   💼 **LinkedIn:** [linkedin.com/in/vitorsilva-aieng](https://www.linkedin.com/in/vitorsilva-aieng/)
*   🐙 **GitHub:** [github.com/vdfs89](https://github.com/vdfs89)
*   🌐 **Personal Website:** [vitorsilva.page](https://vitorsilva.page/)
*   ✉️ **Email:** [vitor_diogo89@hotmail.com](mailto:vitor_diogo89@hotmail.com)
