# Vitor Silva
**AI-First Software Engineer & Solutions Architect**
*Projetando sistemas multiagentes em nível de produção, arquiteturas RAG avançadas e software altamente resiliente.*

Curitiba - PR, Brasil (Disponível para Remoto / Híbrido / Oportunidades Globais)
[LinkedIn](https://www.linkedin.com/in/vitorsilva-aieng/) | [GitHub](https://github.com/vdfs89) | [Portfólio Oficial](https://vitorsilva.page/) | [Email](mailto:vitor_diogo89@hotmail.com)

---

## 🚀 Resumo Executivo

**Como a maturidade em operações de missão crítica se traduz em engenharia de IA robusta.**

Uma transição de carreira estratégica consolidada por **15 anos de liderança em processos e operações de missão crítica** nos Correios (ECT), onde o gerenciamento de riscos, a resiliência sob pressão e o rigoroso cumprimento de SLAs eram as métricas diárias de sucesso. Atualmente na reta final do meu **Bacharelado em Ciência da Computação** e me especializando em **Machine Learning Engineering na FIAP**, trago essa mentalidade de alta confiabilidade corporativa para a engenharia de software avançada.

Minha especialização é a filosofia **AI-First**: não apenas integrar APIs de LLM em produtos convencionais, mas estruturar novos paradigmas para sistemas complexos. Sou especialista em criar **arquiteturas de agentes assíncronos com LangGraph**, mitigação determinística de alucinações em sistemas RAG corporativos, processamento inteligente de documentos (IDP) e estruturação de pipelines sólidos para observabilidade e avaliação contínua (evals).

---

## 🛠️ Grade de Hard Skills (Arquitetura & Engenharia)

```text
┌───────────────────────────────────────┐   ┌───────────────────────────────────────┐
│       INTELIGÊNCIA ARTIFICIAL (IA)    │   │         BACKEND & INTEGRAÇÃO          │
├───────────────────────────────────────┤   ├───────────────────────────────────────┤
│ • Orquestração Multi-Agentes(LangGraph│   │ • Python (FastAPI, Streamlit, Flask)  │
│ • Mitigação Avançada de Alucinações   │   │ • Node.js (JavaScript / TypeScript)   │
│ • Pipelines RAG & Chunking Semântico  │   │ • Programação Assíncrona / Concorrência
│ • Governança de Dados & Curadoria     │   │ • Protocolos Web (REST, WebSockets)   │
│ • Observabilidade (LangSmith & Evals) │   │ • Lógica de Máquina de Estado         │
└───────────────────────────────────────┘   └───────────────────────────────────────┘
┌───────────────────────────────────────┐   ┌───────────────────────────────────────┐
│       INFRAESTRUTURA & MLOPs          │   │           BANCOS DE DADOS             │
├───────────────────────────────────────┤   ├───────────────────────────────────────┤
│ • Conteinerização (Docker)            │   │ • Bancos Vetoriais (Pinecone, PGVector)
│ • Cloud Computing (Azure Services)    │   │ • NoSQL (MongoDB)                     │
│ • CI/CD Automatizado (GitHub Actions) │   │ • Relacional (PostgreSQL)             │
│ • Arquitetura Serverless              │   │ • Pipelines Complexos de Ingestão ETL │
│ • Monitoramento de Data Drift         │   │ • Modelagem de Dados Não Estruturados │
└───────────────────────────────────────┘   └───────────────────────────────────────┘
```

---

## 🏆 Showcase de Engenharia (Projetos em Destaque)

### 📈 1. MestreGrana — Orquestrador Financeiro Multi-Agente
*Plataforma avançada de inteligência financeira estruturada em uma rede de agentes especialistas autônomos para planejamento e auditoria regulatória.*

*   **Stack Principal:** Python, LangGraph, Streamlit, MongoDB.
*   **Abordagem de Negócio:** Substitui a engenharia de prompt linear por um comitê de agentes (planejadores, auditores e validadores) trabalhando colaborativamente para estruturar planos de investimento robustos em total conformidade regulatória.
*   **⚡ O Desafio Técnico Superado:** 
    *   *Mitigação de Alucinações:* Em finanças, a alucinação de dados pode custar milhões ou violar regras regulatórias. Desenvolvi um loop de validação cruzada determinística no LangGraph, onde um Agente de Compliance analisa as saídas geradas confrontando-as com APIs de mercado estruturadas e regras fixas. Se houver uma discrepância de dados maior que 0%, o fluxo se autocorrige e reinicia.
    *   *Persistência de Estado Complexa:* Implementei um sistema customizado de checkpointing do LangGraph no MongoDB, permitindo salvar o estado exato da conversa e as árvores de decisão. Isso garante que interrupções de conexão ou sessões assíncronas longas possam ser retomadas sem perder o progresso histórico.
*   **Links:** 🐙 [Código no GitHub](https://github.com/vdfs89/MestreGrana) | 🌐 [Live Demo](https://mestregrana.streamlit.app/)

---

### 🎓 2. FluencyForge — Tutor Adaptativo de Inglês Técnico
*Ecossistema inteligente que cria trilhas de aprendizado de inglês técnico baseado nas dificuldades em tempo real e contexto do usuário.*

*   **Stack Principal:** FastAPI, Flutter, LangGraph, PostgreSQL.
*   **Abordagem de Negócio:** Um ecossistema mobile e backend voltado para o aprendizado de tech-business, medindo a retenção e o progresso do usuário através de interações contextuais personalizadas.
*   **⚡ O Desafio Técnico Superado:** 
    *   *Streaming Assíncrono e Latência:* Respostas em tempo real exigem processamento de altíssima velocidade. Resolvi a latência implementando streaming de dados bidirecional usando endpoints assíncronos no FastAPI integrados com streams de áudio/texto no Flutter. O processamento pesado de avaliação gramatical roda em background (non-blocking), permitindo que a voz ou o texto de resposta seja gerado em partes (tokens) antes mesmo do fim da análise completa, reduzindo o tempo de resposta percebido para menos de 800ms.
*   **Links:** 🌐 [Live Demo](https://fluencyforge.streamlit.app/)

---

### 🏥 3. Aether Oncology — Cockpit Clínico & Diagnóstico Preditivo
*Plataforma médica de alta densidade para diagnósticos oncológicos, integrando modelos de deep learning de IA Explicável (XAI) com uma interface clínica premium e interativa.*

*   **Stack Principal:** Next.js, PyTorch, FastAPI, Tailwind CSS, Docker.
*   **Abordagem de Negócio:** Substitui terminais de diagnóstico confusos por um cockpit clínico visual de alta densidade (bento-grid de dados clínicos, visualização 3D e XAI) que entrega prognósticos rápidos de tumores com explicações auditáveis para oncologistas.
*   **⚡ O Desafio Técnico Superado:** 
    *   *Explicabilidade do Modelo (XAI) e Latência de Inferência:* Integração de predições de redes neurais profundas (PyTorch) em tempo real sem comprometer a confiança clínica. Desenvolvi um pipeline assíncrono em FastAPI que processa exames e gera heatmaps explicativos (integrated gradients) de atribuição de pixels, retornando o payload em menos de 1,2 segundos.
    *   *Renderização Interativa 3D (GPU):* Projetar um dashboard clínico de alta fidelidade mantendo a interface leve e responsiva. Contornei o gargalo da thread principal do navegador delegando o cálculo de física vetorial e a renderização dinâmica para shaders WebGL acelerados por GPU, garantindo 60fps estáveis.
*   **Links:** 🐙 [Código no GitHub](https://github.com/vdfs89/Aether_Oncology)

---

### 📈 4. Harmoniz.AI — Correlacionador de Dados Biométricos
*Correlação de dados biométricos complexos com pipelines de LLM para otimizar a performance humana.*

*   **Stack Principal:** Python, Pandas, Pipeline LLM, Streamlit.
*   **Links:** 🐙 [Código no GitHub](https://github.com/vdfs89/Harmoniz.AI) | 🌐 [Live Demo](https://harmonizai.streamlit.app/)

---

### 🛒 5. TwinRank AI — Recomendação com Deep Learning
*Two-Tower Neural Network para recomendações de E-commerce.*

*   **Stack Principal:** PyTorch, FastAPI, DVC, MLflow.
*   **Status:** EM DESENVOLVIMENTO

---

### ⚙️ 6. VektorWork — SaaS de Orquestração de IA
*Plataforma de automação self-hosted para freelancers e equipes.*

*   **Stack Principal:** n8n, Docker Compose, PostgreSQL, Redis.
*   **Status:** Repositório Privado

---

### 🔮 7. RetentIA — Engine Preditivo de Churn
*Motor preditivo de churn para B2B SaaS utilizando Machine Learning.*

*   **Stack Principal:** Python, Scikit-learn, XGBoost, FastAPI.
*   **Status:** Repositório Privado

---

### 🏥 8. AIClinicOS — Sistema Operacional para Clínicas
*SO inteligente moderno para gestão de dados clínicos e atendimento de pacientes.*

*   **Stack Principal:** Next.js, Tailwind, Supabase.
*   **Links:** 🌐 [Live Demo](https://ai-clinic-os.vercel.app/)

---

## ⏳ Linha do Tempo Profissional

### 🎓 Formação Acadêmica de Ponta
*   **Pós-Graduação em Machine Learning Engineering**
    *   *FIAP* | Cursando
    *   *Foco prático:* MLOps, deep learning, engenharia de features, deployment escalável de LLMs corporativos e avaliação contínua contra data drift.
*   **Bacharelado em Ciência da Computação**
    *   *Faculdade Descomplica Digital* | Último Ano (Formação em 2026)
    *   *Foco prático:* Base sólida em estruturas de dados complexas, análise de complexidade algorítmica, teoria da computação e segurança de dados.

### 🏢 Liderança & Governança Operacional
*   **Gerente de Processos e Operações de Missão Crítica**
    *   *Correios (ECT)* | 2011 — Presente (15 Anos)
    *   *Entrega Principal:* Coordenação técnica e gestão de equipes operacionais sob alta pressão. Responsável por SLAs de entregas críticas, auditorias federais, mitigação de riscos operacionais complexos e garantia de conformidade legal absoluta.
    *   *Transposição Tecnológica:* Esta profunda experiência operacional confere a maturidade necessária para projetar software a partir da perspectiva de extrema confiabilidade, resiliência do sistema e logs defensivos estruturados contra falhas.

---

## 📬 Contato Direto

Estou sempre aberto a conversar com **CTOs, Engineering Managers e Fundadores de Startups** que procuram engenheiros focados na criação de produtos reais e sistemas de IA robustos.

*   💼 **LinkedIn:** [linkedin.com/in/vitorsilva-aieng](https://www.linkedin.com/in/vitorsilva-aieng/)
*   🐙 **GitHub:** [github.com/vdfs89](https://github.com/vdfs89)
*   🌐 **Site Pessoal:** [vitorsilva.page](https://vitorsilva.page/)
*   ✉️ **Email:** [vitor_diogo89@hotmail.com](mailto:vitor_diogo89@hotmail.com)
