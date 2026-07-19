import os

def main():
    base_dir = "d:/vdfs89/vdfs89"
    with open(os.path.join(base_dir, 'index.html'), 'r', encoding='utf-8') as f:
        content = f.read()

    css_to_add = '''
    /* ════════════════════════════════════
       LANG TOGGLE
    ════════════════════════════════════ */
    .lang-toggle {
        display: flex; gap: 0.5rem; align-items: center; margin-left: 1rem;
        font-size: 0.65rem; font-weight: 700; letter-spacing: 0.08em;
        color: var(--muted);
    }
    .lang-toggle a { color: inherit; text-decoration: none; transition: color .2s; }
    .lang-toggle a:hover { color: var(--green-dim); }
    .lang-toggle a.active-lang { color: var(--green); text-shadow: var(--glow-text); }
'''
    
    # 1. Add CSS
    if '.lang-toggle' not in content:
        content = content.replace('</style>', css_to_add + '</style>')
    
    # 2. Add nav toggle
    nav_toggle_html = '''
            <nav class="lang-toggle">
                <a href="index.en.html" class="__EN_ACTIVE__">EN</a> &middot;
                <a href="index.pt.html" class="__PT_ACTIVE__">PT</a> &middot;
                <a href="index.es.html" class="__ES_ACTIVE__">ES</a>
            </nav>'''
    if 'class="lang-toggle"' not in content:
        content = content.replace('</nav>', '</nav>' + nav_toggle_html, 1)

    # Dictionary for replacements: English -> Portuguese -> Spanish
    # Structure: EN: (PT, ES)
    replacements = {
        # HTML tag
        '<html lang="en"': ('<html lang="pt-BR"', '<html lang="es"'),
        
        # Meta & Titles
        '<title>Vitor Silva | AI Software Engineer | Backend AI Engineer</title>': (
            '<title>Vitor Silva | Engenheiro de IA Sênior | LangGraph, RAG & FastAPI</title>',
            '<title>Vitor Silva | Ingeniero de IA Senior | LangGraph, RAG y FastAPI</title>'
        ),
        'content="AI Software Engineer specialized in LangGraph, FastAPI, Agentic AI, RAG, Multi-Agent Systems and Production AI."': (
            'content="Engenheiro de IA especializado em LangGraph, FastAPI, Agentic AI, RAG, Sistemas Multiagentes e IA em Produção."',
            'content="Ingeniero de IA especializado en LangGraph, FastAPI, Agentic AI, RAG, Sistemas Multiagente e IA en Producción."'
        ),
        '<meta property="og:title" content="Vitor Silva | AI Software Engineer">': (
            '<meta property="og:title" content="Vitor Silva | Engenheiro de IA Sênior">',
            '<meta property="og:title" content="Vitor Silva | Ingeniero de IA Senior">'
        ),
        'content="AI Software Engineer specialized in LangGraph, FastAPI, Agentic AI, RAG, and Multi-Agent Systems."': (
            'content="Engenheiro de IA especializado em LangGraph, FastAPI, Agentic AI, RAG e Sistemas Multiagentes."',
            'content="Ingeniero de IA especializado en LangGraph, FastAPI, Agentic AI, RAG y Sistemas Multiagente."'
        ),
        '<meta name="twitter:title" content="Vitor Silva | AI Software Engineer">': (
            '<meta name="twitter:title" content="Vitor Silva | Engenheiro de IA Sênior">',
            '<meta name="twitter:title" content="Vitor Silva | Ingeniero de IA Senior">'
        ),
        'content="Building production-grade AI systems with LangGraph, FastAPI and RAG."': (
            'content="Construindo sistemas de IA em nível de produção com LangGraph, FastAPI e RAG."',
            'content="Construyendo sistemas de IA a nivel de producción con LangGraph, FastAPI y RAG."'
        ),

        # Nav
        '<a href="#about">ABOUT</a>': ('<a href="#about">SOBRE</a>', '<a href="#about">SOBRE MÍ</a>'),
        '<a href="#projects">PROJECTS</a>': ('<a href="#projects">PROJETOS</a>', '<a href="#projects">PROYECTOS</a>'),
        '<a href="#experience">EXPERIENCE</a>': ('<a href="#experience">EXPERIÊNCIA</a>', '<a href="#experience">EXPERIENCIA</a>'),
        '<a href="#stack">STACK</a>': ('<a href="#stack">STACK</a>', '<a href="#stack">STACK</a>'),
        '<a href="#services">SERVICES</a>': ('<a href="#services">SERVIÇOS</a>', '<a href="#services">SERVICIOS</a>'),
        '<a href="#contact">CONTACT</a>': ('<a href="#contact">CONTATO</a>', '<a href="#contact">CONTACTO</a>'),
        
        # Hero
        'OPEN TO OPPORTUNITIES': ('ABERTO A OPORTUNIDADES', 'ABIERTO A OPORTUNIDADES'),
        'AI Engineer Building Production-Grade Agentic Systems': ('Engenheiro de IA Construindo Sistemas Multiagentes em Produção', 'Ingeniero de IA Construyendo Sistemas Multiagente en Producción'),
        'I design, build, and deploy scalable, observable, and cost-efficient AI agents that deliver real-world business value.': (
            'Eu projeto, construo e implemento agentes de IA escaláveis, observáveis e com eficiência de custo que entregam valor real de negócio.',
            'Diseño, construyo e implemento agentes de IA escalables, observables y rentables que aportan valor real al negocio.'
        ),
        'From stateful multi-agent orchestrations with LangGraph to high-fidelity RAG pipelines, I turn complex requirements into reliable software.': (
            'Desde orquestrações multiagentes stateful com LangGraph até pipelines RAG de alta fidelidade, eu transformo requisitos complexos em software confiável.',
            'Desde orquestraciones multiagente stateful con LangGraph hasta pipelines RAG de alta fidelidad, transformo requisitos complejos en software confiable.'
        ),
        'View Projects &rarr;': ('Ver Projetos &rarr;', 'Ver Proyectos &rarr;'),
        'Book a Discovery Call': ('Agendar uma Reunião', 'Agendar una Reunión'),
        
        'Years ECT': ('Anos ECT', 'Años ECT'),
        'AI Projects': ('Projetos IA', 'Proyectos IA'),
        'Ambition': ('Ambição', 'Ambición'),
        
        'AI systems with clear business value.': ('Sistemas de IA com valor de negócio claro.', 'Sistemas de IA con valor de negocio claro.'),
        'Agents, retrieval pipelines and operational tools balancing technical depth with real user outcomes.': (
            'Agentes, pipelines de RAG e ferramentas operacionais que equilibram profundidade técnica e resultados reais.',
            'Agentes, pipelines de RAG y herramientas operativas que equilibran la profundidad técnica con resultados reales.'
        ),
        '38 repositories &middot; 245 commits<br>Production AI &middot; Active development': (
            '38 repositórios &middot; 245 commits<br>IA em Produção &middot; Dev Ativo',
            '38 repositorios &middot; 245 commits<br>IA en Producción &middot; Dev Activo'
        ),
        
        # About
        'ENGINEERING PHILOSOPHY': ('FILOSOFIA DE ENGENHARIA', 'FILOSOFÍA DE INGENIERÍA'),
        'Engineering Product, Not Just Code': ('Engenharia de Produto, Não Apenas Código', 'Ingeniería de Producto, No Sólo Código'),
        'I transition operations into robust software systems.': (
            'Eu transformo operações em sistemas de software robustos.',
            'Transformo operaciones en sistemas de software robustos.'
        ),
        'With 15 years leading high-pressure operations at ECT, I learned that failure is not an option in mission-critical environments.': (
            'Com 15 anos liderando operações de alta pressão nos Correios (ECT), aprendi que falhas não são uma opção em ambientes de missão crítica.',
            'Con 15 años liderando operaciones de alta presión en ECT, aprendí que los fallos no son una opción en entornos de misión crítica.'
        ),
        'I bring this exact rigor to AI Engineering. My focus is on deterministic outcomes, comprehensive observability (LangSmith/Evals), and hallucination mitigation in agentic workflows.': (
            'Trago exatamente esse rigor para a Engenharia de IA. Meu foco está em resultados determinísticos, observabilidade abrangente (LangSmith/Evals) e mitigação de alucinações em fluxos multiagentes.',
            'Aporto exactamente ese rigor a la Ingeniería de IA. Mi enfoque está en resultados deterministas, observabilidad exhaustiva (LangSmith/Evals) y mitigación de alucinaciones en flujos multiagente.'
        ),
        'Code is easy. Production is hard.': ('Código é fácil. Produção é difícil.', 'El código es fácil. La producción es difícil.'),
        
        # Projects
        'FEATURED WORK': ('PROJETOS EM DESTAQUE', 'PROYECTOS DESTACADOS'),
        'Showcase of Architecture & Engineering': ('Showcase de Arquitetura & Engenharia', 'Showcase de Arquitectura e Ingeniería'),
        
        'Financial intelligence platform structured on an autonomous network of specialist agents for regulatory auditing.': (
            'Plataforma de inteligência financeira estruturada em uma rede autônoma de agentes especialistas para auditoria regulatória.',
            'Plataforma de inteligencia financiera estructurada en una red autónoma de agentes especialistas para auditoría regulatoria.'
        ),
        'Replaces linear prompting with a committee of agents (planners, auditors, validators) working to structure robust investment plans.': (
            'Substitui o prompting linear por um comitê de agentes (planejadores, auditores, validadores) trabalhando para estruturar planos de investimento.',
            'Sustituye el prompting lineal por un comité de agentes (planificadores, auditores, validadores) trabajando para estructurar planes de inversión.'
        ),
        'Implemented a deterministic cross-validation loop and MongoDB checkpointing for complex state persistence in async workflows.': (
            'Implementei um loop de validação cruzada determinística e checkpointing no MongoDB para persistência de estado em fluxos assíncronos.',
            'Implementé un bucle de validación cruzada determinista y checkpointing en MongoDB para la persistencia del estado en flujos asíncronos.'
        ),
        '0 Hallucinations': ('0 Alucinações', '0 Alucinaciones'),
        'Stateful checkpointer': ('Checkpointer stateful', 'Checkpointer stateful'),
        
        'Adaptive Technical English Tutor': ('Tutor Adaptativo de Inglês Técnico', 'Tutor Adaptativo de Inglés Técnico'),
        'Intelligent ecosystem that creates tech-English learning paths based on real-time difficulties.': (
            'Ecossistema inteligente que cria trilhas de aprendizado de inglês técnico com base nas dificuldades em tempo real.',
            'Ecosistema inteligente que crea rutas de aprendizaje de inglés técnico basadas en las dificultades en tiempo real.'
        ),
        'Resolved processing latency by implementing bidirectional data streaming, enabling sub-800ms voice/text responses while grammar analysis runs non-blocking.': (
            'Resolvi a latência implementando streaming bidirecional, permitindo respostas em <800ms enquanto a análise gramatical roda em background.',
            'Resolví la latencia implementando streaming bidireccional, permitiendo respuestas en <800ms mientras el análisis gramatical se ejecuta en background.'
        ),
        'Sub-800ms': ('<800ms', '<800ms'),
        'Real-time response latency': ('Latência de resposta em tempo real', 'Latencia de respuesta en tiempo real'),
        
        'Clinical Cockpit & Predictive Diagnostics': ('Cockpit Clínico & Diagnóstico Preditivo', 'Cockpit Clínico & Diagnóstico Predictivo'),
        'High-density medical platform integrating Explainable AI (XAI) deep learning models with a premium clinical interface.': (
            'Plataforma médica de alta densidade integrando modelos de deep learning e IA Explicável (XAI) com interface clínica premium.',
            'Plataforma médica de alta densidad que integra modelos de deep learning e IA Explicable (XAI) con interfaz clínica premium.'
        ),
        'Asynchronous FastAPI pipeline processing tumor diagnostics with integrated gradients in under 1.2s. Accelerated UI using WebGL shaders.': (
            'Pipeline assíncrono em FastAPI processando diagnósticos de tumores com integrated gradients em <1.2s. UI acelerada com WebGL shaders.',
            'Pipeline asíncrono en FastAPI que procesa diagnósticos de tumores con integrated gradients en <1.2s. UI acelerada con WebGL shaders.'
        ),
        '1.2s payload': ('1.2s payload', '1.2s payload'),
        'GPU Shaders': ('GPU Shaders', 'GPU Shaders'),
        
        'Biometric Data Correlator': ('Correlacionador de Dados Biométricos', 'Correlador de Datos Biométricos'),
        'Correlation of complex biometric data with LLM pipelines to optimize human performance.': (
            'Correlação de dados biométricos complexos com pipelines LLM para otimizar a performance humana.',
            'Correlación de datos biométricos complejos con pipelines LLM para optimizar el rendimiento humano.'
        ),
        
        'Two-Tower Neural Network for E-commerce recommendations.': (
            'Two-Tower Neural Network para recomendações de E-commerce.',
            'Two-Tower Neural Network para recomendaciones de E-commerce.'
        ),
        
        'Self-hosted automation platform for freelancers.': (
            'Plataforma de automação self-hosted para freelancers.',
            'Plataforma de automatización self-hosted para freelancers.'
        ),
        
        'Predictive churn engine for B2B SaaS using Machine Learning.': (
            'Motor preditivo de churn para B2B SaaS usando Machine Learning.',
            'Motor predictivo de churn para B2B SaaS usando Machine Learning.'
        ),
        
        'Modern intelligent OS for clinic data and patient care management.': (
            'SO inteligente moderno para gestão de dados e pacientes em clínicas.',
            'SO inteligente moderno para la gestión de datos y pacientes en clínicas.'
        ),
        
        # Badges
        '> Private Repository': ('> Repositório Privado', '> Repositorio Privado'),
        '> IN DEVELOPMENT': ('> EM DESENVOLVIMENTO', '> EN DESARROLLO'),
        
        # Experience
        'CAREER TIMELINE': ('LINHA DO TEMPO PROFISSIONAL', 'LÍNEA DE TIEMPO PROFESIONAL'),
        'Academic & Operational Background': ('Trajetória Acadêmica & Operacional', 'Trayectoria Académica y Operativa'),
        'Postgraduate in Machine Learning Engineering': ('Pós-Graduação em Machine Learning Engineering', 'Postgrado en Machine Learning Engineering'),
        'Ongoing': ('Cursando', 'En curso'),
        'Practical Focus:': ('Foco Prático:', 'Enfoque Práctico:'),
        'MLOps, deep learning, feature engineering, scalable deployment of enterprise LLMs, and continuous evaluation against data drift.': (
            'MLOps, deep learning, engenharia de features, deployment escalável de LLMs e avaliação contínua contra data drift.',
            'MLOps, deep learning, ingeniería de features, despliegue escalable de LLMs y evaluación continua contra el data drift.'
        ),
        
        'BSc in Computer Science': ('Bacharelado em Ciência da Computação', 'Licenciatura en Ciencias de la Computación'),
        'Descomplica Digital University': ('Faculdade Descomplica Digital', 'Universidad Digital Descomplica'),
        'Senior Year (Graduation 2026)': ('Último Ano (Formação 2026)', 'Último Año (Graduación 2026)'),
        'Solid foundation in complex data structures, algorithmic complexity analysis, theory of computation, and data security.': (
            'Base sólida em estruturas de dados complexas, análise de complexidade algorítmica, teoria da computação e segurança de dados.',
            'Base sólida en estructuras de datos complejas, análisis de complejidad algorítmica, teoría de la computación y seguridad de datos.'
        ),
        
        'Process and Mission-Critical Operations Manager': ('Gerente de Processos e Operações de Missão Crítica', 'Gerente de Procesos y Operaciones de Misión Crítica'),
        'Brazilian Postal Service (ECT)': ('Correios (ECT)', 'Correos (ECT)'),
        '2011 &mdash; Present (15 Years)': ('2011 &mdash; Presente (15 Anos)', '2011 &mdash; Presente (15 Años)'),
        'Core Delivery:': ('Entrega Principal:', 'Entrega Principal:'),
        'Technical coordination and management of high-pressure operational teams. Responsible for critical delivery SLAs, federal audits, complex operational risk mitigation, and absolute legal compliance assurance.': (
            'Coordenação técnica e gestão de equipes operacionais sob alta pressão. Responsável por SLAs críticos, auditorias federais, mitigação de riscos e garantia de compliance legal.',
            'Coordinación técnica y gestión de equipos operativos bajo alta presión. Responsable de SLAs críticos, auditorías federales, mitigación de riesgos y garantía de compliance legal.'
        ),
        'Technological Transposition:': ('Transposição Tecnológica:', 'Transposición Tecnológica:'),
        'This deep operational experience grants the maturity needed to design software from the perspective of extreme reliability, system resilience, and structured defensive logs against failures.': (
            'Esta experiência operacional profunda confere a maturidade necessária para projetar software sob a perspectiva de extrema confiabilidade, resiliência e logs defensivos estruturados.',
            'Esta profunda experiencia operativa otorga la madurez necesaria para diseñar software desde la perspectiva de la fiabilidad extrema, resiliencia y logs defensivos estructurados.'
        ),
        
        # Tech Stack
        'TECH STACK': ('TECH STACK', 'TECH STACK'),
        'Architecture & Engineering Grid': ('Grade de Arquitetura & Engenharia', 'Matriz de Arquitectura e Ingeniería'),
        'Multi-Agent Orchestration': ('Orquestração Multi-Agente', 'Orquestación Multiagente'),
        'Advanced Hallucination Mitigation': ('Mitigação Avançada de Alucinações', 'Mitigación Avanzada de Alucinaciones'),
        'RAG Pipelines & Semantic Chunking': ('Pipelines RAG & Chunking Semântico', 'Pipelines RAG y Chunking Semántico'),
        'Data Governance & Curation': ('Governança de Dados & Curadoria', 'Gobernanza de Datos y Curaduría'),
        'Observability (LangSmith & Evals)': ('Observabilidade (LangSmith & Evals)', 'Observabilidad (LangSmith & Evals)'),
        'Async Programming / Concurrency': ('Programação Assíncrona / Concorrência', 'Programación Asíncrona / Concurrencia'),
        'Web Protocols (REST, WebSockets)': ('Protocolos Web (REST, WebSockets)', 'Protocolos Web (REST, WebSockets)'),
        'State-Machine Logic & Determinism': ('Lógica de Máquinas de Estado', 'Lógica de Máquinas de Estado'),
        'Containerization': ('Conteinerização', 'Contenerización'),
        'Cloud Computing': ('Cloud Computing', 'Cloud Computing'),
        'Automated CI/CD': ('CI/CD Automatizado', 'CI/CD Automatizado'),
        'Serverless Architecture': ('Arquitetura Serverless', 'Arquitectura Serverless'),
        'Data Drift Metrics Monitoring': ('Monitoramento de Data Drift', 'Monitoreo de Data Drift'),
        'Vector DBs': ('Bancos Vetoriais', 'Bases de Datos Vectoriales'),
        'Relational': ('Relacional', 'Relacional'),
        'Complex Ingestion ETL Pipelines': ('Pipelines Complexos de Ingestão ETL', 'Pipelines Complejos de Ingestión ETL'),
        'Unstructured Data Modeling': ('Modelagem de Dados Não Estruturados', 'Modelado de Datos No Estructurados'),
        
        # Services
        'MY SERVICES': ('MEUS SERVIÇOS', 'MIS SERVICIOS'),
        'What I can do for your business': ('O que posso fazer pelo seu negócio', 'Qué puedo hacer por tu negocio'),
        'Agentic AI Development': ('Desenvolvimento de IA Multiagente', 'Desarrollo de IA Multiagente'),
        'I build autonomous multi-agent systems using LangGraph to solve complex, multi-step business problems reliably.': (
            'Construo sistemas multiagentes autônomos com LangGraph para resolver problemas de negócio complexos de forma confiável.',
            'Construyo sistemas multiagente autónomos con LangGraph para resolver problemas de negocio complejos de forma fiable.'
        ),
        'Enterprise RAG Systems': ('Sistemas RAG Corporativos', 'Sistemas RAG Corporativos'),
        'Implementing production-grade Retrieval-Augmented Generation with strict hallucination controls and source attribution.': (
            'Implementação de RAG em nível de produção com controles rigorosos de alucinação e atribuição de fontes.',
            'Implementación de RAG a nivel de producción con estrictos controles de alucinación y atribución de fuentes.'
        ),
        'Backend Architecture': ('Arquitetura Backend', 'Arquitectura Backend'),
        'Designing scalable APIs with FastAPI, managing complex state and building async data processing pipelines.': (
            'Projetando APIs escaláveis com FastAPI, gerenciando estados complexos e construindo pipelines de processamento assíncrono.',
            'Diseñando APIs escalables con FastAPI, gestionando estados complejos y construyendo pipelines de procesamiento asíncrono.'
        ),
        'Remote, based in Brazil &mdash; available for clients in Brazil and worldwide. Fluent English for technical communication.': (
            'Remoto, baseado no Brasil &mdash; disponível para clientes no Brasil e globalmente. Inglês fluente.',
            'Remoto, con base en Brasil &mdash; disponible para clientes globales. Inglés fluido para comunicación técnica.'
        ),
        
        # Contact / Footer
        'START A PROJECT': ('INICIAR UM PROJETO', 'INICIAR UN PROYECTO'),
        'Get In Touch': ('Entre em Contato', 'Ponte en Contacto'),
        'Are you a CTO, Engineering Manager, or Founder looking for a dedicated AI engineer? Let\'s talk about your next big challenge.': (
            'Você é CTO, Engineering Manager ou Founder procurando um engenheiro de IA dedicado? Vamos conversar sobre o seu próximo grande desafio.',
            '¿Eres CTO, Engineering Manager o Founder buscando un ingeniero de IA dedicado? Hablemos sobre tu próximo gran desafío.'
        ),
        'COPY EMAIL': ('COPIAR EMAIL', 'COPIAR EMAIL'),
        'Curitiba - PR, Brazil': ('Curitiba - PR, Brasil', 'Curitiba - PR, Brasil'),
        'Designed and engineered by Vitor Silva.': (
            'Projetado e desenvolvido por Vitor Silva.',
            'Diseñado y desarrollado por Vitor Silva.'
        ),
        
        # FAQ
        'FREQUENTLY ASKED': ('PERGUNTAS FREQUENTES', 'PREGUNTAS FRECUENTES'),
        'Clarifications & Details': ('Esclarecimentos & Detalhes', 'Aclaraciones y Detalles'),
        'What is your availability?': ('Qual a sua disponibilidade?', '¿Cuál es tu disponibilidad?'),
        'I am currently open to full-time remote or hybrid opportunities, as well as select consulting projects.': (
            'Atualmente estou aberto a oportunidades remotas ou híbridas em tempo integral, bem como projetos de consultoria selecionados.',
            'Actualmente estoy abierto a oportunidades remotas o híbridas a tiempo completo, así como a proyectos de consultoría seleccionados.'
        ),
        'Do you work with frontend technologies?': ('Você trabalha com tecnologias de frontend?', '¿Trabajas con tecnologías de frontend?'),
        'While my primary focus is backend AI architecture (Python/FastAPI), I have experience building full-stack applications using Next.js and Tailwind CSS when necessary for complete product delivery.': (
            'Embora meu foco seja arquitetura backend e IA (Python/FastAPI), tenho experiência construindo aplicações full-stack com Next.js e Tailwind CSS quando necessário.',
            'Aunque mi enfoque principal es la arquitectura backend e IA (Python/FastAPI), tengo experiencia construyendo aplicaciones full-stack con Next.js y Tailwind CSS cuando es necesario.'
        ),
        'Why LangGraph over standard LangChain?': ('Por que LangGraph em vez de LangChain padrão?', '¿Por qué LangGraph en lugar del LangChain estándar?'),
        'LangGraph allows for cyclic, stateful multi-agent workflows with human-in-the-loop capabilities, which is essential for deterministic production systems, unlike linear chains.': (
            'O LangGraph permite fluxos de trabalho cíclicos, stateful e com human-in-the-loop, essenciais para sistemas determinísticos em produção, diferente das chains lineares.',
            'LangGraph permite flujos de trabajo cíclicos, stateful y con human-in-the-loop, lo que es esencial para sistemas deterministas en producción, a diferencia de las cadenas lineales.'
        )
    }

    # Generate EN
    en_content = content.replace('__EN_ACTIVE__', 'active-lang').replace('__PT_ACTIVE__', '').replace('__ES_ACTIVE__', '')
    with open(os.path.join(base_dir, 'index.en.html'), 'w', encoding='utf-8') as f:
        f.write(en_content)
    # Default index is EN
    with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(en_content)

    # Generate PT
    pt_content = content.replace('__EN_ACTIVE__', '').replace('__PT_ACTIVE__', 'active-lang').replace('__ES_ACTIVE__', '')
    for en, (pt, es) in replacements.items():
        pt_content = pt_content.replace(en, pt)
    with open(os.path.join(base_dir, 'index.pt.html'), 'w', encoding='utf-8') as f:
        f.write(pt_content)

    # Generate ES
    es_content = content.replace('__EN_ACTIVE__', '').replace('__PT_ACTIVE__', '').replace('__ES_ACTIVE__', 'active-lang')
    for en, (pt, es) in replacements.items():
        es_content = es_content.replace(en, es)
    with open(os.path.join(base_dir, 'index.es.html'), 'w', encoding='utf-8') as f:
        f.write(es_content)

    print("Success! Created index.en.html, index.pt.html, index.es.html, and updated index.html.")

if __name__ == '__main__':
    main()
