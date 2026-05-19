# Vitor Silva
**AI-First Software Engineer & Solutions Architect**
*Designing production-grade multi-agent systems, advanced RAG architectures, and highly resilient software systems.*

Curitiba - PR, Brazil (Open to Remote / Hybrid / Global Opportunities)
[LinkedIn](https://linkedin.com/in/vdfs89) | [GitHub](https://github.com/vdfs89) | [Official Portfolio](https://vitorsilva.page/) | [Email](mailto:vdfs89@gmail.com)

---

## 🚀 Proposta de Valor (Executive Summary)

**Como a maturidade operacional de missão crítica se traduz em engenharia de IA robusta.**

Transição de carreira estratégica consolidada por **15 anos de liderança em processos e operações de missão crítica** nos Correios (ECT), onde o gerenciamento de riscos, a resiliência operacional sob pressão e o cumprimento de SLAs rigorosos eram as métricas diárias de sucesso. Atualmente na reta final de **Ciência da Computação** e especializando-me em **Machine Learning Engineering pela FIAP**, trago essa mentalidade de alta confiabilidade corporativa para a engenharia de software avançada.

Minha especialização é a filosofia **AI-First**: não apenas integrar APIs de LLMs em produtos convencionais, mas estruturar novos paradigmas de sistemas complexos. Sou especialista na criação de **arquiteturas agênticas assíncronas com LangGraph**, mitigação determinística de alucinações em sistemas RAG corporativos, processamento inteligente de documentos (IDP) e na estruturação de esteiras sólidas de observabilidade e avaliação contínua. 

---

## 🛠️ Grid de Hard Skills (Arquitetura & Engenharia)

```
┌──────────────────────────────────────────┐   ┌──────────────────────────────────────────┐
│     INTELIGÊNCIA ARTIFICIAL (AI)         │   │         BACKEND & INTEGRAÇÃO             │
├──────────────────────────────────────────┤   ├──────────────────────────────────────────┤
│ • Orquestração Multi-Agente (LangGraph)  │   │ • Python (FastAPI, Streamlit, Flask)     │
│ • Mitigação Avançada de Alucinações      │   │ • Node.js (JavaScript / TypeScript)      │
│ • Pipelines de RAG & Chunking Semântico  │   │ • Programação Assíncrona & Concorrência  │
│ • Governança & Curadoria de Dados        │   │ • Protocolos Web (REST, WebSockets)      │
│ • Observabilidade (LangSmith & Evals)    │   │ • State-Machine Logic & Determinismo     │
└──────────────────────────────────────────┘   └──────────────────────────────────────────┘
┌──────────────────────────────────────────┐   ┌──────────────────────────────────────────┐
│     INFRAESTRUTURA & MLOPs               │   │          BANCOS DE DADOS                 │
├──────────────────────────────────────────┤   ├──────────────────────────────────────────┤
│ • Containerização (Docker)               │   │ • Bancos Vetoriais (Pinecone, PGVector)  │
│ • Cloud Computing (Azure Services)       │   │ • NoSQL (MongoDB)                        │
│ • CI/CD Automático (GitHub Actions)      │   │ • Relacionais (PostgreSQL)               │
│ • Arquitetura Serverless                 │   │ • Pipelines ETL de Ingestão Complexa     │
│ • Monitoramento de Métricas de Deriva    │   │ • Modelagem de Dados Não Estruturados    │
└──────────────────────────────────────────┘   └──────────────────────────────────────────┘
```

---

## 🏆 Projetos Vitrine (Showcase de Engenharia)

### 📈 1. MestreGrana — Orquestrador Multi-Agente Financeiro
*Plataforma avançada de inteligência financeira estruturada em uma rede de agentes autônomos especialistas para planejamento e auditoria regulatória.*

*   **Stack Principal:** Python, LangGraph, Streamlit, MongoDB.
*   **A Abordagem de Negócio:** Substitui o prompt engineering linear por um comitê de agentes (planejadores, auditores e validadores) que trabalham de forma colaborativa para estruturar planejamentos de investimento robustos e em total conformidade regulatória.
*   **⚡ O Desafio Técnico Superado:** 
    *   *Mitigação de Alucinação:* Em finanças, uma alucinação de dados pode custar milhões ou violar regras regulatórias. Desenvolvi um loop determinístico de validação cruzada no LangGraph, onde um Agente de Compliance analisa as saídas geradas confrontando-as com APIs de mercado estruturadas e regras fixas. Se houver discrepância de dados superiores a 0%, o fluxo é reiniciado de forma auto-corretiva.
    *   *Persistência de Estado Complexo:* Implementei um sistema de checkpointing customizado do LangGraph no MongoDB, permitindo salvar o estado exato da conversa e das árvores de decisão. Isso garante que interrupções de conexão ou sessões assíncronas de longa duração possam ser retomadas sem perda de progresso histórico.
*   **Links:** 🐙 [Código no GitHub](https://github.com/vdfs89/mestre-grana) | 🌐 [Demo Ativa](https://mestregrana.streamlit.app/)

---

### 🎓 2. FluencyForge — Tutor Adaptativo de Inglês Técnico
*Ecossistema inteligente que cria percursos de aprendizagem de inglês para tecnologia baseado nas dificuldades e contexto em tempo real do usuário.*

*   **Stack Principal:** FastAPI, Flutter, LangGraph, PostgreSQL.
*   **A Abordagem de Negócio:** Um ecossistema móvel e backend voltado para o aprendizado focado em negócios de tecnologia, medindo a retenção e o progresso do usuário através de interações contextuais personalizadas.
*   **⚡ O Desafio Técnico Superado:** 
    *   *Streaming Assíncrono e Latência:* A resposta a conversas em tempo real requer processamento de altíssima velocidade. Solucionei a latência implementando streaming de dados bi-direcional utilizando endpoints assíncronos no FastAPI integrados a streams de áudio/texto no Flutter. O processamento pesado da avaliação gramatical roda de forma não-bloqueante no background, permitindo que a voz ou texto de resposta seja gerado em partes (tokens) antes mesmo que a análise completa termine, reduzindo o tempo percebido de resposta para menos de 800ms.
*   **Links:** 🐙 [Código no GitHub](https://github.com/vdfs89/fluency-forge)

---

### 🏥 3. Aether Oncology — Cockpit Clínico & Diagnóstico Preditivo
*Plataforma médica de alta densidade para diagnóstico oncológico, integrando modelos de Deep Learning explicáveis (XAI - Explainable AI) a uma interface clínica premium e interativa.*

*   **Stack Principal:** Next.js, PyTorch, FastAPI, Tailwind CSS, Docker.
*   **A Abordagem de Negócio:** Substitui terminais de diagnóstico confusos por um cockpit clínico de alta densidade visual (bento-grid de dados clínicos, estrela-guia de visualização tridimensional e XAI) que entrega prognósticos rápidos de tumores com explicações auditáveis para oncologistas.
*   **⚡ O Desafio Técnico Superado:** 
    *   *Explicabilidade do Modelo (XAI) e Latência de Inferência:* Integrar previsões de redes neurais profundas (PyTorch) em tempo real sem comprometer a confiança clínica. Desenvolvi um pipeline assíncrono no FastAPI que processa exames e gera mapas de calor explicativos (gradientes integrados) de atribuição de pixels, retornando o payload em menos de 1.2 segundos.
    *   *Renderização de Estrela-Guia Interativa (GPU):* Projetar um dashboard clínico de alta fidelidade mantendo a interface leve e responsiva. Contornei o gargalo na main thread do navegador delegando o cálculo vetorial de física e renderização da estrela-guia dinâmica ("Lotus Pulsante") para shaders acelerados por GPU em WebGL, garantindo 60fps estáveis.
*   **Links:** 🐙 [Código no GitHub](https://github.com/vdfs89/Aether_Oncology)

---

## ⏳ Linha do Tempo Profissional

### 🎓 Formação Acadêmica de Vanguarda
*   **Pós-Graduação em Machine Learning Engineering**
    *   *FIAP* | Cursando
    *   *Foco prático:* MLOps, deep learning, engenharia de atributos, implantação escalável de LLMs corporativos e avaliação contínua contra desvio de dados (data drift).
*   **Bacharelado em Ciência da Computação**
    *   *Descomplica Faculdade Digital* | Último Ano (Conclusão 2026)
    *   *Foco prático:* Sólida base em estruturas de dados complexas, análise de complexidade algorítmica, teoria da computação e segurança de dados.

### 🏢 Liderança & Governança Operacional
*   **Gestor de Processos e Operações de Missão Crítica**
    *   *Correios (ECT)* | 2011 — Presente (15 Anos)
    *   *Core Delivery:* Coordenação técnica e gerenciamento de equipes de operação de alta pressão. Responsável por SLA crítico de entregas, auditorias federais, mitigação de riscos operacionais complexos e garantia de conformidade legal absoluta.
    *   *Transposição Tecnológica:* Esta profunda experiência operacional confere a maturidade necessária para desenhar softwares sob a ótica de confiabilidade extrema, resiliência do sistema e logs defensivos estruturados contra falhas.

---

## 📬 Contato Direto

Estou sempre aberto a conversar com **CTOs, Engineering Managers e Fundadores de Startups** que buscam engenheiros focados na criação de produtos reais e sistemas de IA robustos.

*   💼 **LinkedIn:** [linkedin.com/in/vdfs89](https://linkedin.com/in/vdfs89)
*   🐙 **GitHub:** [github.com/vdfs89](https://github.com/vdfs89)
*   🌐 **Website Pessoal:** [vitorsilva.page](https://vitorsilva.page/)
*   ✉️ **E-mail:** [vdfs89@gmail.com](mailto:vdfs89@gmail.com)
