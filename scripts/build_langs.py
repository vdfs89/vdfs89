import os

# Repository root: the parent of scripts/
REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DETECT_SCRIPT = """    <script>
    /* Root page serves English. Send pt-* / es-* browsers to their variant once
       per session; picking a language from the toggle sticks for the session. */
    (function () {
        try {
            if (sessionStorage.getItem('langChosen')) return;
            var lang = (navigator.language || navigator.userLanguage || '').toLowerCase();
            var target = lang.indexOf('pt') === 0 ? '__PT__'
                       : lang.indexOf('es') === 0 ? '__ES__'
                       : null;
            if (target) {
                sessionStorage.setItem('langChosen', '1');
                location.replace(target);
            }
        } catch (e) { /* storage blocked: stay on English */ }
    })();
    </script>
"""


CANONICAL = '<link rel="canonical" href="https://vitorsilva.page/">'
OG_URL = '<meta property="og:url" content="https://vitorsilva.page/">'


def localize_urls(html, filename):
    """Each translated page is canonical to itself, not to the English root."""
    html = html.replace(CANONICAL, CANONICAL.replace('page/"', 'page/' + filename + '"'))
    return html.replace(OG_URL, OG_URL.replace('page/"', 'page/' + filename + '"'))


def with_lang_detect(en_html, pt_file, es_file):
    """Root page is English plus a one-shot browser-language redirect."""
    script = DETECT_SCRIPT.replace('__PT__', pt_file).replace('__ES__', es_file)
    charset = '<meta charset="UTF-8">'
    return en_html.replace(charset, charset + '\n' + script, 1)

def main():
    base_dir = REPO_DIR
    with open(os.path.join(base_dir, 'index.en.html'), 'r', encoding='utf-8') as f:
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
    
    # 2. Add or update nav toggle
    import re
    # Remove any existing nav lang-toggle so we can insert the templated one
    content = re.sub(r'\s*<nav class="lang-toggle">.*?</nav>', '', content, flags=re.DOTALL)
    
    nav_toggle_html = '''
            <nav class="lang-toggle">
                <a href="index.en.html" class="__EN_ACTIVE__">EN</a> &middot;
                <a href="index.pt.html" class="__PT_ACTIVE__">PT</a> &middot;
                <a href="index.es.html" class="__ES_ACTIVE__">ES</a>
            </nav>'''
    # Append it to the main nav
    content = content.replace('</nav>', '</nav>' + nav_toggle_html, 1)

    # Dictionary for replacements: English -> Portuguese -> Spanish
    # Structure: EN: (PT, ES)
    replacements = {
        # HTML tag
        '<html lang="en"': ('<html lang="pt-BR"', '<html lang="es"'),
        
        # Meta & Titles

        # Nav
        '<a href="#about">ABOUT</a>': ('<a href="#about">SOBRE</a>', '<a href="#about">SOBRE MÍ</a>'),
        '<a href="#projects">PROJECTS</a>': ('<a href="#projects">PROJETOS</a>', '<a href="#projects">PROYECTOS</a>'),
        '<a href="#experience">EXPERIENCE</a>': ('<a href="#experience">EXPERIÊNCIA</a>', '<a href="#experience">EXPERIENCIA</a>'),
        '<a href="#stack">STACK</a>': ('<a href="#stack">STACK</a>', '<a href="#stack">STACK</a>'),
        '<a href="#contact">CONTACT</a>': ('<a href="#contact">CONTATO</a>', '<a href="#contact">CONTACTO</a>'),
        
        # Hero
        'OPEN TO OPPORTUNITIES': ('ABERTO A OPORTUNIDADES', 'ABIERTO A OPORTUNIDADES'),
        'View Projects &rarr;': ('Ver Projetos &rarr;', 'Ver Proyectos &rarr;'),
        
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
            'Com 14 anos liderando operações de alta pressão nos Correios (ECT), aprendi que falhas não são uma opção em ambientes de missão crítica.',
            'Con 14 años liderando operaciones de alta presión en ECT, aprendí que los fallos no son una opción en entornos de misión crítica.'
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
        ),
        
        # --- NEW HIGHLIGHTS ---
        'Engineering <span class="g">Highlights.</span>': ('Destaques de <span class="g">Engenharia.</span>', 'Aspectos Destacados de <span class="g">Ingeniería.</span>'),
        'Engineering <span class="g">Product,</span><br>Not Just <span class="g">Code.</span>': ('Engenharia de <span class="g">Produto,</span><br>Não Apenas <span class="g">Código.</span>', 'Ingeniería de <span class="g">Producto,</span><br>No Sólo <span class="g">Código.</span>'),
        'Architectures that<br><span class="g">generate business value.</span>': ('Arquiteturas que<br><span class="g">geram valor de negócio.</span>', 'Arquitecturas que<br><span class="g">generan valor de negocio.</span>'),
        
        'With 14 years of mission-critical operations experience, I don\'t just write scripts—I architect resilient systems. I\'ve spent over a decade managing high-pressure logistics where downtime means total failure. That operational maturity is the foundation of my engineering.': (
            'Com mais de 14 anos de experiência em operações de missão crítica, eu não escrevo apenas scripts — eu arquiteto sistemas resilientes. Passei mais de uma década gerenciando logística de alta pressão, onde a inatividade significa falha total. Essa maturidade operacional é a base da minha engenharia.',
            'Con más de 14 años de experiencia en operaciones de misión crítica, no solo escribo scripts — diseño sistemas resilientes. He pasado más de una década gestionando logística de alta presión donde el tiempo de inactividad significa fracaso total. Esa madurez operativa es la base de mi ingeniería.'
        ),
        'I focus on systems that are observable, gracefully degrading, and maintainable. I build solutions to solve the real business problem, not just the technical challenge.': (
            'Foco em sistemas observáveis, de degradação suave e fáceis de manter. Construo soluções para resolver o problema real de negócio, não apenas o desafio técnico.',
            'Me enfoco en sistemas observables, con degradación elegante y fáciles de mantener. Construyo soluciones para resolver el problema de negocio real, no solo el desafío técnico.'
        ),
        
        '14 Years': ('15+ Anos', '15+ Años'),
        'Operations and reliability mindset': ('Mentalidade de operação e confiabilidade', 'Mentalidad de operación y confiabilidad'),
        'AI Systems': ('Sistemas de IA', 'Sistemas de IA'),
        'Agents, RAG, orchestration, data pipelines': ('Agentes, RAG, orquestração, pipelines de dados', 'Agentes, RAG, orquestración, pipelines de datos'),
        'Available for global opportunities': ('Disponível para oportunidades globais', 'Disponible para oportunidades globales'),
        
        'MISSION CRITICAL': ('MISSÃO CRÍTICA', 'MISIÓN CRÍTICA'),
        'I operated for 14 years in zero-tolerance-for-failure environments. That mindset translates to defensive coding, robust error handling, and architectures built for resilience.': (
            'Operei 14 anos em ambientes de tolerância zero a falhas. Essa mentalidade se traduz em código defensivo, tratamento robusto de erros e arquiteturas construídas para resiliência.',
            'Operé 14 años en entornos de tolerancia cero a fallos. Esa mentalidad se traduce en código defensivo, manejo robusto de errores y arquitecturas construidas para la resiliencia.'
        ),
        'PRODUCT, NOT JUST CODE': ('PRODUTO, NÃO APENAS CÓDIGO', 'PRODUCTO, NO SÓLO CÓDIGO'),
        'I understand business processes because I managed them for over a decade. I design solutions that deliver real-world outcomes.': (
            'Entendo os processos de negócio porque os gerenciei por mais de uma década. Desenho soluções que entregam resultados no mundo real.',
            'Entiendo los procesos de negocio porque los gestioné durante más de una década. Diseño soluciones que ofrecen resultados en el mundo real.'
        ),
        
        'FINTECH &middot; AI GOVERNANCE': ('FINTECH &middot; GOVERNANÇA DE IA', 'FINTECH &middot; GOBERNANZA DE IA'),
        'LIVE': ('ATIVO', 'ACTIVO'),
        'Business Problem:': ('Problema de Negócio:', 'Problema de Negocio:'),
        'High risk of hallucination and lack of governance in generative AI for financial advice.': (
            'Alto risco de alucinação e falta de governança na IA generativa para aconselhamento financeiro.',
            'Alto riesgo de alucinación y falta de gobernanza en IA generativa para asesoramiento financiero.'
        ),
        'Architecture:': ('Arquitetura:', 'Arquitectura:'),
        'Technical Solution:': ('Solução Técnica:', 'Solución Técnica:'),
        'Stateful orchestration via LangGraph for long-term memory.': ('Orquestração stateful via LangGraph para memória de longo prazo.', 'Orquestración stateful vía LangGraph para memoria a largo plazo.'),
        '"Judge" LLM system to audit answers (Guardrails).': ('Sistema LLM "Juiz" para auditar respostas (Guardrails).', 'Sistema LLM "Juez" para auditar respuestas (Guardrails).'),
        'Multi-LLM Judges': ('Juízes Multi-LLM', 'Jueces Multi-LLM'),
        'Audit guardrails + hallucination mitigation in production': ('Guardrails de auditoria + mitigação de alucinação em produção', 'Guardrails de auditoría + mitigación de alucinación en producción'),
        '▶ Watch Demo': ('▶ Ver Demo', '▶ Ver Demo'),
        'State Graphs + Multi-LLM Guardrails': ('Grafos de Estado + Guardrails Multi-LLM', 'Grafos de Estado + Guardrails Multi-LLM'),
        
        'EDTECH &middot; AGENTIC AI': ('EDTECH &middot; IA AGÊNTICA', 'EDTECH &middot; IA AGÉNTICA'),
        'FEATURED': ('DESTAQUE', 'DESTACADO'),
        'Teaching personalization at scale hits LLM context limits.': ('Personalização de ensino em escala atinge os limites de contexto do LLM.', 'La personalización de la enseñanza a escala alcanza los límites de contexto del LLM.'),
        'Solution:': ('Solução:', 'Solución:'),
        'Dynamic RAG coupled with stateful memory to maintain historical context.': ('RAG dinâmico aliado a memória stateful para manter o contexto histórico.', 'RAG dinámico junto con memoria stateful para mantener el contexto histórico.'),
        'LangGraph + State Management + RAG': ('LangGraph + Gestão de Estado + RAG', 'LangGraph + Gestión de Estado + RAG'),
        
        'E-COMMERCE &middot; DEEP LEARNING': ('E-COMMERCE &middot; DEEP LEARNING', 'E-COMMERCE &middot; DEEP LEARNING'),
        'IN DEV': ('EM DESENV', 'EN DESARR'),
        'Popularity-based recommendation systems fail in personalization.': ('Sistemas de recomendação baseados em popularidade falham na personalização.', 'Los sistemas de recomendación basados en popularidad fallan en la personalización.'),
        'Tech Stack:': ('Tech Stack:', 'Tech Stack:'),
        'Neural Collaborative Filtering': ('Filtragem Colaborativa Neural', 'Filtrado Colaborativo Neuronal'),
        
        'HEALTHTECH &middot; FULL STACK': ('HEALTHTECH &middot; FULL STACK', 'HEALTHTECH &middot; FULL STACK'),
        'Business Case:': ('Caso de Negócio:', 'Caso de Negocio:'),
        'Robust clinical data integration for multi-platform interfaces.': ('Integração robusta de dados clínicos para interfaces multiplataforma.', 'Integración robusta de datos clínicos para interfaces multiplataforma.'),
        'Full Stack &middot; API-Driven': ('Full Stack &middot; API-Driven', 'Full Stack &middot; API-Driven'),
        
        'SAAS &middot; AI ORCHESTRATION': ('SAAS &middot; ORQUESTRAÇÃO DE IA', 'SAAS &middot; ORQUESTACIÓN DE IA'),
        'PRIVATE': ('PRIVADO', 'PRIVADO'),
        
        'B2B SAAS &middot; PREDICTIVE': ('B2B SAAS &middot; PREDITIVO', 'B2B SAAS &middot; PREDICTIVO'),
        'High churn rates in SaaS platforms due to reactive support.': ('Altas taxas de churn em plataformas SaaS devido ao suporte reativo.', 'Altas tasas de churn en plataformas SaaS debido al soporte reactivo.'),
        'Predictive Churn Engine': ('Motor Preditivo de Churn', 'Motor Predictivo de Churn'),
        
        'HEALTHTECH &middot; DATA': ('HEALTHTECH &middot; DADOS', 'HEALTHTECH &middot; DATOS'),
        'Scalably correlating complex biometric data.': ('Correlacionando de forma escalável dados biométricos complexos.', 'Correlacionando de forma escalable datos biométricos complejos.'),

        'CURRENT_PROFILE': ('PERFIL_ATUAL', 'PERFIL_ACTUAL'),
        'AVAILABLE': ('DISPONÍVEL', 'DISPONIBLE'),
        'FOCUS': ('FOCO', 'ENFOQUE')
    ,
    'Operational maturity.<br><span class="g">Cutting-edge stack.</span>': (
        'Maturidade operacional.<br><span class="g">Stack de ponta.</span>',
        'Madurez operativa.<br><span class="g">Stack de vanguardia.</span>'
    ),
    '2011 → PRESENT': (
        '2011 → PRESENTE',
        '2011 → PRESENTE'
    ),
    'Operational Support · Curitiba, PR': (
        'Suporte Operacional · Curitiba, PR',
        'Soporte Operativo · Curitiba, PR'
    ),
    'Reliability mindset forged through high-pressure operations and problem-solving in environments that do not tolerate failures.': (
        'Mentalidade de confiabilidade forjada através de operações de alta pressão e resolução de problemas em ambientes que não toleram falhas.',
        'Mentalidad de fiabilidad forjada a través de operaciones de alta presión y resolución de problemas en entornos que no toleran fallos.'
    ),
    'SLA guarantee and large-scale operational continuity': (
        'Garantia de SLA e continuidade operacional em larga escala',
        'Garantía de SLA y continuidad operativa a gran escala'
    ),
    'Technical focal point for corporate system implementation': (
        'Ponto focal técnico para implementação de sistemas corporativos',
        'Punto focal técnico para la implementación de sistemas corporativos'
    ),
    'Analytical profile for real-time failure mitigation': (
        'Perfil analítico para mitigação de falhas em tempo real',
        'Perfil analítico para mitigación de fallos en tiempo real'
    ),
    '2023 → 2026': (
        '2023 → 2026',
        '2023 → 2026'
    ),
    'BSc in Computer Science': (
        'Bacharelado em Ciência da Computação',
        'Licenciatura en Ciencias de la Computación'
    ),
    'Formal foundations in algorithms, systems and distributed computing': (
        'Fundamentos formais em algoritmos, sistemas e computação distribuída',
        'Fundamentos formales en algoritmos, sistemas y computación distribuida'
    ),
    'Complementary tracks: MLOps, FastAPI and Data Engineering': (
        'Trilhas complementares: MLOps, FastAPI e Engenharia de Dados',
        'Pistas complementarias: MLOps, FastAPI e Ingeniería de Datos'
    ),
    '2026 → 2027': (
        '2026 → 2027',
        '2026 → 2027'
    ),
    'MLOps, model deployment and ML pipelines in production': (
        'MLOps, deploy de modelos e pipelines de ML em produção',
        'MLOps, despliegue de modelos y pipelines de ML en producción'
    ),
    'Scalable AI system architecture and model governance': (
        'Arquitetura de sistemas de IA escaláveis e governança de modelos',
        'Arquitectura de sistemas de IA escalables y gobernanza de modelos'
    ),
    '2024 → NOW': (
        '2024 → AGORA',
        '2024 → AHORA'
    ),
    'Independent projects · Open to Opportunities': (
        'Projetos independentes · Aberto a Oportunidades',
        'Proyectos independientes · Abierto a Oportunidades'
    ),
    'Stateful agentic systems with memory and LangGraph orchestration': (
        'Sistemas agênticos stateful com memória e orquestração LangGraph',
        'Sistemas agénticos stateful con memoria y orquestación LangGraph'
    ),
    'FastAPI services with async patterns and high performance': (
        'Serviços FastAPI com padrões assíncronos e alto desempenho',
        'Servicios FastAPI con patrones asíncronos y alto rendimiento'
    ),
    'RAG pipelines designed for real use cases with semantic precision': (
        'Pipelines RAG projetados para casos de uso reais com precisão semântica',
        'Pipelines RAG diseñados para casos de uso reales con precisión semántica'
    ),
    'Delivery Under Pressure': (
        'Entrega Sob Pressão',
        'Entrega Bajo Presión'
    ),
    '14 years of zero-downtime tolerance translate into defensive code and architectures that degrade gracefully.': (
        '14 anos de tolerância zero a inatividade se traduzem em código defensivo e arquiteturas que degradam suavemente.',
        '14 años de tolerancia cero a inactividad se traducen en código defensivo y arquitecturas que se degradan suavemente.'
    ),
    'Product Vision, Not Just Code': (
        'Visão de Produto, Não Apenas Código',
        'Visión de Producto, No Sólo Código'
    ),
    'I understand business processes because I operated them. I design systems that solve the real problem.': (
        'Entendo processos de negócio porque os operei. Desenho sistemas que resolvem o problema real.',
        'Entiendo los procesos de negocio porque los operé. Diseño sistemas que resuelven el problema real.'
    ),
    'Modern Stack, Engineer Mindset': (
        'Stack Moderna, Mentalidade de Engenheiro',
        'Stack Moderna, Mentalidad de Ingeniero'
    ),
    'LangGraph, RAG, FastAPI — not as buzzwords, but applied in projects with measurable business objectives.': (
        'LangGraph, RAG, FastAPI — não como buzzwords, mas aplicados em projetos com objetivos de negócio mensuráveis.',
        'LangGraph, RAG, FastAPI — no como palabras de moda, sino aplicados en proyectos con objetivos de negocio medibles.'
    ),
    'Certifications': (
        'Certificações',
        'Certificaciones'
    ),
    'Tools.<br><span class="g">Not just buzzwords.</span>': (
        'Ferramentas.<br><span class="g">Não apenas buzzwords.</span>',
        'Herramientas.<br><span class="g">No solo palabras de moda.</span>'
    ),
    'Agentic Systems with LangGraph': (
        'Sistemas Agênticos com LangGraph',
        'Sistemas Agénticos con LangGraph'
    ),
    'Architecture and development of stateful agents with memory, multi-agent orchestration and robust decision flows.': (
        'Arquitetura e desenvolvimento de agentes stateful com memória, orquestração multi-agente e fluxos de decisão robustos.',
        'Arquitectura y desarrollo de agentes stateful con memoria, orquestación multiagente y flujos de decisión robustos.'
    ),
    'RAG & Retrieval Pipelines': (
        'RAG & Pipelines de Recuperação',
        'RAG & Pipelines de Recuperación'
    ),
    'High-fidelity semantic retrieval pipelines for Q&A, support and enterprise knowledge bases.': (
        'Pipelines de recuperação semântica de alta fidelidade para Q&A, suporte e bases de conhecimento corporativas.',
        'Pipelines de recuperación semántica de alta fidelidad para Q&A, soporte y bases de conocimiento corporativas.'
    ),
    'AI Guardrails & Governance': (
        'Guardrails & Governança de IA',
        'Guardrails & Gobernanza de IA'
    ),
    'Multi-LLM audit systems that mitigate hallucinations before they reach the user. Cost control and groundedness.': (
        'Sistemas de auditoria Multi-LLM que mitigam alucinações antes de chegarem ao usuário. Controle de custos e fundamentação.',
        'Sistemas de auditoría Multi-LLM que mitigan las alucinaciones antes de que lleguen al usuario. Control de costes y fundamentación.'
    ),
    'FastAPI & Python Backend': (
        'Backend Python & FastAPI',
        'Backend Python & FastAPI'
    ),
    'High-performance async backends integrating AI models, databases and external services.': (
        'Backends assíncronos de alta performance integrando modelos de IA, bancos de dados e serviços externos.',
        'Backends asíncronos de alto rendimiento que integran modelos de IA, bases de datos y servicios externos.'
    ),
    'What is the difference between RAG and a regular chatbot?': (
        'Qual a diferença entre RAG e um chatbot comum?',
        '¿Cuál es la diferencia entre RAG y un chatbot común?'
    ),
    'INITIATE CONVERSATION': (
        'INICIAR CONVERSA',
        'INICIAR CONVERSACIÓN'
    ),
    "Let's build the<br>next level?": (
        'Vamos construir o<br>próximo nível?',
        '¿Construimos el<br>siguiente nivel?'
    ),
    "The real challenge isn't building AI — it's trusting it in production. My projects target governance, guardrails and hallucination control.": (
        "O verdadeiro desafio não é construir IA — é confiar nela em produção. Meus projetos focam em governança, guardrails e controle de alucinação.",
        "El verdadero desafío no es construir IA — es confiar en ella en producción. Mis proyectos se centran en gobernanza, guardrails y control de alucinaciones."
    ),
    'View Projects': ('Ver Projetos', 'Ver Proyectos'),
    # These come after the contact paragraph above on purpose: that paragraph
    # contains the same sentence, and replacing the short form first would stop
    # the longer key from ever matching.
    'Modern clinics need intelligent OS to manage data and patient care efficiently.': (
        'Clínicas modernas precisam de um sistema inteligente para gerir dados e atendimento com eficiência.',
        'Las clínicas modernas necesitan un sistema inteligente para gestionar datos y atención con eficiencia.'
    ),
    'mkmillhouse89@gmail.com">CONTACT</a>': (
        'mkmillhouse89@gmail.com">CONTATO</a>',
        'mkmillhouse89@gmail.com">CONTACTO</a>'
    ),
    # Architecture diagrams. Keyed with the closing tag so short words like
    # "User" or "Judge" cannot match prose elsewhere on the page.
    '>User</text>': ('>Usuário</text>', '>Usuario</text>'),
    '>Question</text>': ('>Pergunta</text>', '>Pregunta</text>'),
    '>HTTP gateway</text>': ('>Gateway HTTP</text>', '>Gateway HTTP</text>'),
    '>Stateful orchestrator</text>': ('>Orquestrador stateful</text>', '>Orquestador stateful</text>'),
    '>Embeddings</text>': ('>Embeddings</text>', '>Embeddings</text>'),
    '>Judge</text>': ('>Júri</text>', '>Jurado</text>'),
    '>Governance</text>': ('>Governança</text>', '>Gobernanza</text>'),
    '>Auditing</text>': ('>Auditoria</text>', '>Auditoría</text>'),
    '>Validated answer</text>': ('>Resposta validada</text>', '>Respuesta validada</text>'),
    '>Audited before delivery</text>': ('>Auditada antes de entregar</text>', '>Auditada antes de entregar</text>'),
    '>User request</text>': ('>Requisição do usuário</text>', '>Solicitud del usuario</text>'),
    '>FastAPI gateway</text>': ('>Gateway FastAPI</text>', '>Gateway FastAPI</text>'),
    '>LangGraph orchestrator</text>': ('>Orquestrador LangGraph</text>', '>Orquestador LangGraph</text>'),
    '>Context retrieval (Vector DB)</text>': ('>Recuperação de contexto (Vector DB)</text>', '>Recuperación de contexto (Vector DB)</text>'),
    '>Curriculum agent</text>': ('>Agente de currículo</text>', '>Agente de currículo</text>'),
    '>Assessment agent</text>': ('>Agente de avaliação</text>', '>Agente de evaluación</text>'),
    'MestreGrana architecture': ('Arquitetura do MestreGrana', 'Arquitectura de MestreGrana'),
    'FluencyForge architecture': ('Arquitetura do FluencyForge', 'Arquitectura de FluencyForge'),
    # Projects added to the portfolio
    '>Projects built</span>': (
        '>Projetos construídos</span>',
        '>Proyectos construidos</span>'
    ),
    'Recall@10 vs 0.0034 for the popularity baseline on the RetailRocket dataset. Part of the gain comes from repeated items; the model still leads on pure discovery.': (
        'Recall@10 contra 0,0034 do baseline de popularidade no dataset RetailRocket. Parte do ganho vem de itens repetidos; o modelo continua à frente em descoberta pura.',
        'Recall@10 frente a 0,0034 del baseline de popularidad en el dataset RetailRocket. Parte de la ganancia viene de ítems repetidos; el modelo sigue liderando en descubrimiento puro.'
    ),
    'recall at a cost-weighted threshold. ROC-AUC 0.845, nearly identical to XGBoost; the value is the threshold calibrated to the cost of a missed churner.': (
        'recall com limiar ponderado por custo. ROC-AUC 0,845, quase idêntico ao do XGBoost; o valor está no limiar calibrado ao custo de deixar um churner passar.',
        'recall con umbral ponderado por costo. ROC-AUC 0,845, casi idéntico al de XGBoost; el valor está en el umbral calibrado al costo de dejar pasar a un cliente que se va.'
    ),
    '>VIDEO →</a>': (
        '>VÍDEO →</a>',
        '>VIDEO →</a>'
    ),
    "B2B service operations need one governed platform for leads, contracts and payments, with each organization's data kept apart.": (
        'Operações B2B de serviços precisam de uma plataforma única e governada para leads, contratos e pagamentos, com os dados de cada organização isolados.',
        'Las operaciones B2B de servicios necesitan una plataforma única y gobernada para leads, contratos y pagos, con los datos de cada organización aislados.'
    ),
    'cross-tenant isolation checks passed on a test database. Row-level security is not yet enabled in production.': (
        'verificações de isolamento entre organizações aprovadas em um banco de testes. O isolamento por linha (RLS) ainda não está ativo em produção.',
        'verificaciones de aislamiento entre organizaciones aprobadas en una base de pruebas. La seguridad por fila (RLS) aún no está activa en producción.'
    ),
    '<span>Multi-tenant B2B Platform</span>': (
        '<span>Plataforma B2B Multi-tenant</span>',
        '<span>Plataforma B2B Multi-tenant</span>'
    ),
    'A hospital needs incoming medical reports triaged by urgency, with a model that can be retrained, monitored and served fast.': (
        'Um hospital precisa triar laudos médicos por urgência, com um modelo que possa ser retreinado, monitorado e servido com rapidez.',
        'Un hospital necesita clasificar informes médicos por urgencia, con un modelo que pueda reentrenarse, monitorearse y servirse rápido.'
    ),
    'p95 API latency on the baseline model (200 requests). Macro F1 of 0.62 on heuristic urgency labels.': (
        'latência p95 da API no modelo baseline (200 requisições). F1 macro de 0,62 em rótulos de urgência heurísticos.',
        'latencia p95 de la API en el modelo baseline (200 solicitudes). F1 macro de 0,62 con etiquetas de urgencia heurísticas.'
    ),
    '<span>End-to-End MLOps Pipeline</span>': (
        '<span>Pipeline MLOps de Ponta a Ponta</span>',
        '<span>Pipeline MLOps de Extremo a Extremo</span>'
    ),
    "Generic training apps ignore the user's goal and equipment, and give no clear view of progress.": (
        'Apps de treino genéricos ignoram o objetivo e o equipamento do usuário e não mostram a evolução com clareza.',
        'Las apps de entrenamiento genéricas ignoran el objetivo y el equipamiento del usuario y no muestran la evolución con claridad.'
    ),
    '<span>Workout Tracker App</span>': (
        '<span>App de Acompanhamento de Treino</span>',
        '<span>App de Seguimiento de Entrenamiento</span>'
    ),
    'AI tools for careers and freelancing send sensitive data, like CVs and expectations, to third-party clouds.': (
        'Ferramentas de IA para carreira e freelas enviam dados sensíveis, como currículos e pretensões, para nuvens de terceiros.',
        'Las herramientas de IA para carrera y freelance envían datos sensibles, como currículos y expectativas, a nubes de terceros.'
    ),
    '<span>Privacy-First Multi-Agent Platform</span>': (
        '<span>Plataforma Multiagente com Privacidade em Primeiro Lugar</span>',
        '<span>Plataforma Multiagente con Privacidad Primero</span>'
    ),
    '<span>ALSO BUILT</span>': (
        '<span>TAMBÉM CONSTRUÍ</span>',
        '<span>TAMBIÉN CONSTRUÍ</span>'
    ),
    'Long-term memory and retrieval layer for an AI agent: vector search plus PostgreSQL state.': (
        'Camada de memória de longo prazo e recuperação para um agente de IA: busca vetorial e estado em PostgreSQL.',
        'Capa de memoria de largo plazo y recuperación para un agente de IA: búsqueda vectorial y estado en PostgreSQL.'
    ),
    'Space action game built with Unity and C#, my first game.': (
        'Jogo de ação espacial feito em Unity e C#, meu primeiro jogo.',
        'Juego de acción espacial hecho en Unity y C#, mi primer juego.'
    ),
    'Molecular structures modeled as graphs, in Python.': (
        'Estruturas moleculares modeladas como grafos, em Python.',
        'Estructuras moleculares modeladas como grafos, en Python.'
    ),
    'High-conversion landing page for an e-book, built on 58 scientific sources.': (
        'Landing page de alta conversão para um e-book, baseada em 58 fontes científicas.',
        'Landing page de alta conversión para un e-book, basada en 58 fuentes científicas.'
    ),
    # Corrected after the user confirmed the figures
    'People led, covering the supervisor': (
        'Pessoas lideradas, cobrindo o supervisor',
        'Personas lideradas, cubriendo al supervisor'
    ),
    # Repositioning: junior full stack and AI developer
    '<title>Vitor Silva | Full Stack and AI Developer | Python, FastAPI, React</title>': (
        '<title>Vitor Silva | Desenvolvedor Full Stack e IA | Python, FastAPI, React</title>',
        '<title>Vitor Silva | Desarrollador Full Stack e IA | Python, FastAPI, React</title>'
    ),
    'content="Junior Full Stack and AI developer with 14 years in critical operations. Python, FastAPI, React, Next.js, LangGraph and RAG. Open to remote roles."': (
        'content="Desenvolvedor Full Stack e IA júnior com 14 anos em operações críticas. Python, FastAPI, React, Next.js, LangGraph e RAG. Aberto a vagas remotas."',
        'content="Desarrollador Full Stack e IA junior con 14 años en operaciones críticas. Python, FastAPI, React, Next.js, LangGraph y RAG. Abierto a puestos remotos."'
    ),
    '<meta property="og:title" content="Vitor Silva | Full Stack and AI Developer">': (
        '<meta property="og:title" content="Vitor Silva | Desenvolvedor Full Stack e IA">',
        '<meta property="og:title" content="Vitor Silva | Desarrollador Full Stack e IA">'
    ),
    'content="Junior Full Stack and AI developer. Python, FastAPI, React, LangGraph and RAG. Open to remote roles."': (
        'content="Desenvolvedor Full Stack e IA júnior. Python, FastAPI, React, LangGraph e RAG. Aberto a vagas remotas."',
        'content="Desarrollador Full Stack e IA junior. Python, FastAPI, React, LangGraph y RAG. Abierto a puestos remotos."'
    ),
    '<meta name="twitter:title" content="Vitor Silva | Full Stack and AI Developer">': (
        '<meta name="twitter:title" content="Vitor Silva | Desenvolvedor Full Stack e IA">',
        '<meta name="twitter:title" content="Vitor Silva | Desarrollador Full Stack e IA">'
    ),
    'content="Junior full stack developer building AI applications with Python, FastAPI and React."': (
        'content="Desenvolvedor full stack júnior construindo aplicações com IA em Python, FastAPI e React."',
        'content="Desarrollador full stack junior construyendo aplicaciones con IA en Python, FastAPI y React."'
    ),
    '<a href="#services">WHAT I DO</a>': (
        '<a href="#services">O QUE FAÇO</a>',
        '<a href="#services">QUÉ HAGO</a>'
    ),
    '<p class="hero-role">Junior Full Stack and AI Developer</p>': (
        '<p class="hero-role">Desenvolvedor Full Stack e IA Júnior</p>',
        '<p class="hero-role">Desarrollador Full Stack e IA Junior</p>'
    ),
    'I build web applications end to end — Python and FastAPI on the back end, React and Next.js on the front — and add AI where it earns its place.': (
        'Construo aplicações web de ponta a ponta — Python e FastAPI no back-end, React e Next.js no front-end — e uso IA onde ela realmente agrega.',
        'Construyo aplicaciones web de extremo a extremo — Python y FastAPI en el back-end, React y Next.js en el front-end — y uso IA donde realmente aporta.'
    ),
    'After 14 years running critical operations at Correios, I build software the way I ran operations: measured, documented and designed not to fail.': (
        'Depois de 14 anos em operações críticas nos Correios, construo software do jeito que operava: medido, documentado e projetado para não falhar.',
        'Tras 14 años en operaciones críticas en Correios, construyo software como operaba: medido, documentado y diseñado para no fallar.'
    ),
    '<a class="btn" href="mailto:mkmillhouse89@gmail.com">Get in touch</a>': (
        '<a class="btn" href="mailto:mkmillhouse89@gmail.com">Entrar em contato</a>',
        '<a class="btn" href="mailto:mkmillhouse89@gmail.com">Ponerse en contacto</a>'
    ),
    '<div class="prompt reveal">WHAT I DO</div>': (
        '<div class="prompt reveal">O QUE FAÇO</div>',
        '<div class="prompt reveal">QUÉ HAGO</div>'
    ),
    'What I bring<br><span class="g">to your team.</span>': (
        'O que eu levo<br><span class="g">para o seu time.</span>',
        'Lo que aporto<br><span class="g">a su equipo.</span>'
    ),
    'Remote-first, based in Curitiba. Open to junior full stack and AI developer roles.': (
        'Remoto em primeiro lugar, baseado em Curitiba. Aberto a vagas de desenvolvedor full stack e IA júnior.',
        'Remoto ante todo, con base en Curitiba. Abierto a puestos de desarrollador full stack e IA junior.'
    ),
    'Are you looking for a junior role?': (
        'Você busca uma vaga júnior?',
        '¿Buscas un puesto junior?'
    ),
    'Yes. I am looking for a junior full stack or AI developer position, remote or hybrid in Curitiba. I bring 14 years of operations experience and a portfolio of projects I built and shipped.': (
        'Sim. Busco uma vaga de desenvolvedor full stack ou IA júnior, remota ou híbrida em Curitiba. Trago 14 anos de experiência em operações e um portfólio de projetos que construí e coloquei no ar.',
        'Sí. Busco un puesto de desarrollador full stack o IA junior, remoto o híbrido en Curitiba. Aporto 14 años de experiencia en operaciones y un portafolio de proyectos que construí y publiqué.'
    ),
    'What can you do from day one?': (
        'O que você entrega desde o primeiro dia?',
        '¿Qué puedes hacer desde el primer día?'
    ),
    'Build and ship features end to end on a Python and React stack, write tests and document what I build. TypeScript and cloud are where I am still growing.': (
        'Construir e entregar funcionalidades de ponta a ponta numa stack Python e React, escrever testes e documentar o que construo. TypeScript e cloud são onde ainda estou crescendo.',
        'Construir y entregar funcionalidades de extremo a extremo en un stack Python y React, escribir pruebas y documentar lo que construyo. TypeScript y cloud son donde aún estoy creciendo.'
    ),
    'Do you work with international teams?': (
        'Você trabalha com times internacionais?',
        '¿Trabajas con equipos internacionales?'
    ),
    'Yes. I read technical English fluently and I am comfortable with remote, asynchronous work.': (
        'Sim. Leio inglês técnico com fluência e me sinto confortável com trabalho remoto e assíncrono.',
        'Sí. Leo inglés técnico con fluidez y me siento cómodo con el trabajo remoto y asíncrono.'
    ),
    'Plenty of juniors can write the code. Few have spent 14 years in mission-critical operations learning what makes a system resilient.': (
        'Muitos juniores sabem escrever código. Poucos passaram 14 anos em operações críticas aprendendo o que torna um sistema resiliente.',
        'Muchos juniors saben escribir código. Pocos pasaron 14 años en operaciones críticas aprendiendo qué hace resiliente a un sistema.'
    ),
    '<div class="tl-title">Full Stack and AI Developer</div>': (
        '<div class="tl-title">Desenvolvedor Full Stack e IA</div>',
        '<div class="tl-title">Desarrollador Full Stack e IA</div>'
    ),
    'Building web applications and AI systems end to end: back end, front end and deployment.': (
        'Construindo aplicações web e sistemas de IA de ponta a ponta: back-end, front-end e deploy.',
        'Construyendo aplicaciones web y sistemas de IA de extremo a extremo: back-end, front-end y despliegue.'
    ),
    'Open to junior full stack and AI developer roles, remote or hybrid in Curitiba. Fourteen years of operational discipline, plus software I built and shipped.': (
        'Aberto a vagas de desenvolvedor full stack e IA júnior, remoto ou híbrido em Curitiba. Quatorze anos de disciplina operacional, mais software que construí e coloquei no ar.',
        'Abierto a puestos de desarrollador full stack e IA junior, remoto o híbrido en Curitiba. Catorce años de disciplina operativa, más software que construí y publiqué.'
    ),
    '<span>Full Stack and AI Developer</span>': (
        '<span>Desenvolvedor Full Stack e IA</span>',
        '<span>Desarrollador Full Stack e IA</span>'
    ),
    '<a href="#services">What I do</a>': (
        '<a href="#services">O que faço</a>',
        '<a href="#services">Qué hago</a>'
    ),
    'Full Stack Web Applications': (
        'Aplicações Web Full Stack',
        'Aplicaciones Web Full Stack'
    ),
    'React and Next.js front ends over Python or Node APIs, with authentication, a database and a deploy pipeline.': (
        'Front-ends em React e Next.js sobre APIs em Python ou Node, com autenticação, banco de dados e pipeline de deploy.',
        'Front-ends en React y Next.js sobre APIs en Python o Node, con autenticación, base de datos y pipeline de despliegue.'
    ),
    'Operations to Software': (
        'Da Operação ao Software',
        'De la Operación al Software'
    ),
    'I turn operational processes into software: map the flow, find where it fails and automate the repetitive part.': (
        'Transformo processos operacionais em software: mapeio o fluxo, encontro onde ele falha e automatizo a parte repetitiva.',
        'Convierto procesos operativos en software: mapeo el flujo, encuentro dónde falla y automatizo la parte repetitiva.'
    ),
    '🌐 Remote-first': (
        '🌐 Remoto em primeiro lugar',
        '🌐 Remoto ante todo'
    ),
    'Based in Curitiba, Brazil. Available for remote roles in Brazil and abroad. Technical English.': (
        'Baseado em Curitiba, Brasil. Disponível para vagas remotas no Brasil e no exterior. Inglês técnico.',
        'Con base en Curitiba, Brasil. Disponible para puestos remotos en Brasil y en el exterior. Inglés técnico.'
    ),
    '>GET IN TOUCH →</a>': (
        '>ENTRAR EM CONTATO →</a>',
        '>PONERSE EN CONTACTO →</a>'
    ),
    # Footer columns
    'Building AI systems that hold up in production, with the operational discipline of someone who ran critical systems for fourteen years.': (
        'Construindo sistemas de IA que se sustentam em produção, com a disciplina operacional de quem cuidou de sistemas críticos por quatorze anos.',
        'Construyendo sistemas de IA que se sostienen en producción, con la disciplina operativa de quien cuidó sistemas críticos durante catorce años.'
    ),
    '<h3>Navigate</h3>': ('<h3>Navegar</h3>', '<h3>Navegar</h3>'),
    '<h3>Elsewhere</h3>': ('<h3>Em outros lugares</h3>', '<h3>En otros sitios</h3>'),
    '<a href="#about">About</a>': ('<a href="#about">Sobre</a>', '<a href="#about">Sobre mí</a>'),
    '<a href="#projects">Projects</a>': ('<a href="#projects">Projetos</a>', '<a href="#projects">Proyectos</a>'),
    '<a href="#experience">Experience</a>': ('<a href="#experience">Experiência</a>', '<a href="#experience">Experiencia</a>'),
    '<a href="dashboard.html">Dashboard</a>': ('<a href="dashboard.pt.html">Dashboard</a>', '<a href="dashboard.es.html">Dashboard</a>'),
    # Stack tabs
    'aria-label="Technology categories"': ('aria-label="Categorias de tecnologia"', 'aria-label="Categorías de tecnología"'),
    '>Data &amp; Infra<': ('>Dados &amp; Infra<', '>Datos e Infra<'),
    '>Cloud &amp; Tools<': ('>Cloud &amp; Ferramentas<', '>Cloud y Herramientas<'),
    '>Data Analysis<': ('>Análise de Dados<', '>Análisis de Datos<'),
    '<span>PROFILE</span>': ('<span>PERFIL</span>', '<span>PERFIL</span>'),
    # Hero visual + metrics band
    'Photo goes here': ('Foto entra aqui', 'La foto va aquí'),
    '<span>System status</span>': ('<span>Status do sistema</span>', '<span>Estado del sistema</span>'),
    'Open to opportunities': ('Aberto a oportunidades', 'Abierto a oportunidades'),
    'Curitiba, PR &middot; remote': ('Curitiba, PR &middot; remoto', 'Curitiba, PR &middot; remoto'),
    '<span>Activity</span>': ('<span>Atividade</span>', '<span>Actividad</span>'),
    'Years in critical operations': ('Anos em operação crítica', 'Años en operación crítica'),
    'Automated tests in CI': ('Testes automatizados em CI', 'Pruebas automatizadas en CI'),
    'Fewer operational failures': ('Menos falhas operacionais', 'Menos fallos operativos'),
    'justify-content:center;">CONTACT</div>': (
        'justify-content:center;">CONTATO</div>',
        'justify-content:center;">CONTACTO</div>'
    ),
}

    # Generate EN
    en_content = content.replace('__EN_ACTIVE__', 'active-lang').replace('__PT_ACTIVE__', '').replace('__ES_ACTIVE__', '')
    with open(os.path.join(base_dir, 'index.en.html'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(en_content)
    # Generate PT
    pt_content = content.replace('__EN_ACTIVE__', '').replace('__PT_ACTIVE__', 'active-lang').replace('__ES_ACTIVE__', '')
    for en, (pt, es) in replacements.items():
        pt_content = pt_content.replace(en, pt)
    with open(os.path.join(base_dir, 'index.pt.html'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(localize_urls(pt_content, 'index.pt.html'))
        
    # Default index is EN + browser-language detection (see with_lang_detect)
    with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(with_lang_detect(en_content, 'index.pt.html', 'index.es.html'))

    # Generate ES
    es_content = content.replace('__EN_ACTIVE__', '').replace('__PT_ACTIVE__', '').replace('__ES_ACTIVE__', 'active-lang')
    for en, (pt, es) in replacements.items():
        es_content = es_content.replace(en, es)
    with open(os.path.join(base_dir, 'index.es.html'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(localize_urls(es_content, 'index.es.html'))

    print("Success! Created index.en.html, index.pt.html, index.es.html, and updated index.html (EN default).")

if __name__ == '__main__':
    main()
