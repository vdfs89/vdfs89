import os

# Repository root: the parent of scripts/
REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import re


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


def join_string_literals(html):
    """Collapse JS string concatenations ("a " + "b") into one literal.

    The translation table is keyed on whole sentences, so a sentence split
    across several literals never matched and shipped untranslated.
    """
    return re.sub(r'"[ \t]*\+\s*\n\s*"', '', html)


def with_lang_detect(en_html, pt_file, es_file):
    """Root page is English plus a one-shot browser-language redirect."""
    script = DETECT_SCRIPT.replace('__PT__', pt_file).replace('__ES__', es_file)
    charset = '<meta charset="UTF-8">'
    return en_html.replace(charset, charset + '\n' + script, 1)

def main():
    base_dir = REPO_DIR
    with open(os.path.join(base_dir, 'dashboard.en.html'), 'r', encoding='utf-8') as f:
        content = f.read()

    replacements = {
        # Nav sidebar
        '>\n      Overview\n    </button>': ('>\n      Visão Geral\n    </button>', '>\n      Visión General\n    </button>'),
        '>\n      Profile\n    </button>': ('>\n      Perfil\n    </button>', '>\n      Perfil\n    </button>'),
        '>\n      Experience\n    </button>': ('>\n      Experiência\n    </button>', '>\n      Experiencia\n    </button>'),
        '>\n      Education\n    </button>': ('>\n      Formação\n    </button>', '>\n      Educación\n    </button>'),
        '>\n      Projects &amp; Stack\n    </button>': ('>\n      Projetos &amp; Stack\n    </button>', '>\n      Proyectos &amp; Stack\n    </button>'),
        '>\n      Certifications\n    </button>': ('>\n      Certificações\n    </button>', '>\n      Certificaciones\n    </button>'),
        '>\n      Achievements\n    </button>': ('>\n      Conquistas\n    </button>', '>\n      Logros\n    </button>'),
        '>\n      AI Assistant\n    </button>': ('>\n      Assistente de IA\n    </button>', '>\n      Asistente de IA\n    </button>'),

        # Section 1
        '<h3>Connect</h3>': ('<h3>Conectar</h3>', '<h3>Conectar</h3>'),
        'Official channels and portfolio.': ('Canais oficiais e portfólio.', 'Canales oficiales y portafolio.'),
        
        # Section 2
        '<h2 class="secao-titulo">Profile</h2>': ('<h2 class="secao-titulo">Perfil</h2>', '<h2 class="secao-titulo">Perfil</h2>'),
        'executive summary · data · guidelines · pillars': ('resumo executivo · dados · diretrizes · pilares', 'resumen ejecutivo · datos · directrices · pilares'),
        '<h3>Executive Summary</h3>': ('<h3>Resumo Executivo</h3>', '<h3>Resumen Ejecutivo</h3>'),
        '<h3>Data</h3>': ('<h3>Dados</h3>', '<h3>Datos</h3>'),
        '<h3>Professional Guidelines</h3>': ('<h3>Diretrizes Profissionais</h3>', '<h3>Directrices Profesionales</h3>'),
        '<h3>Expertise Pillars</h3>': ('<h3>Pilares de Especialidade</h3>', '<h3>Pilares de Especialidad</h3>'),

        # Section 3
        '<h2 class="secao-titulo">Experience</h2>': ('<h2 class="secao-titulo">Experiência</h2>', '<h2 class="secao-titulo">Experiencia</h2>'),

        # Section 4
        '<h2 class="secao-titulo">Education</h2>': ('<h2 class="secao-titulo">Formação</h2>', '<h2 class="secao-titulo">Educación</h2>'),
        'ongoing academic education': ('formação acadêmica em andamento', 'educación académica en curso'),

        # Section 5
        '<h2 class="secao-titulo">Projects &amp; Tech Stack</h2>': ('<h2 class="secao-titulo">Projetos &amp; Tech Stack</h2>', '<h2 class="secao-titulo">Proyectos &amp; Tech Stack</h2>'),
        'real systems, in production or active evolution': ('sistemas reais, em produção ou evolução ativa', 'sistemas reales, en producción o evolución activa'),
        '<h3>Full Tech Stack</h3>': ('<h3>Tech Stack Completa</h3>', '<h3>Tech Stack Completa</h3>'),

        # Section 6
        '<h2 class="secao-titulo">Certifications</h2>': ('<h2 class="secao-titulo">Certificações</h2>', '<h2 class="secao-titulo">Certificaciones</h2>'),
        'certification in progress + continuous education': ('certificação em andamento + educação contínua', 'certificación en curso + educación continua'),
        'Hours distribution by area': ('Distribuição de horas por área', 'Distribución de horas por área'),
        'Top skills by XP (DIO)': ('Principais habilidades por XP (DIO)', 'Principales habilidades por XP (DIO)'),

        # Section 7
        '<h2 class="secao-titulo">Achievements</h2>': ('<h2 class="secao-titulo">Conquistas</h2>', '<h2 class="secao-titulo">Logros</h2>'),

        # Section 8
        '<h2 class="secao-titulo">AI Assistant</h2>': ('<h2 class="secao-titulo">Assistente de IA</h2>', '<h2 class="secao-titulo">Asistente de IA</h2>'),
        'ask about projects, tech stack, experience or contact': ('pergunte sobre projetos, stack, experiência ou contato', 'pregunta sobre proyectos, stack, experiencia o contacto'),
        'placeholder="type your question..."': ('placeholder="digite sua pergunta..."', 'placeholder="escribe tu pregunta..."'),
        '>SEND<': ('>ENVIAR<', '>ENVIAR<'),

        # DATA replacements
        'Curitiba, PR, Brazil': ('Curitiba, PR, Brasil', 'Curitiba, PR, Brasil'),
        'Open to remote opportunities (Brazil & global)': ('Aberto a oportunidades remotas (Brasil e global)', 'Abierto a oportunidades remotas (Brasil y global)'),
        'AVAILABLE FOR OPPORTUNITIES': ('DISPONÍVEL PARA OPORTUNIDADES', 'DISPONIBLE PARA OPORTUNIDADES'),
        'Years of mission-critical operations': ('Anos de operações de missão crítica', 'Años de operaciones de misión crítica'),
        'Languages (PT · EN · ES)': ('Idiomas (PT · EN · ES)', 'Idiomas (PT · EN · ES)'),
        'Continuous education certificates': ('Certificados de educação contínua', 'Certificados de educación continua'),

        
        'Multi-agent financial advisor — LangGraph orchestration + multi-LLM judge in production.': (
            'Consultor financeiro multiagente — Orquestração LangGraph + juiz multi-LLM em produção.',
            'Asesor financiero multiagente — Orquestación LangGraph + juez multi-LLM en producción.'
        ),

        'AI Engineer working end-to-end across architecture, backend and ML systems. I build scalable, reliable multi-agent systems and APIs, bringing a mission-critical mindset to AI engineering.': (
            'Engenheiro de IA atuando de ponta a ponta em arquitetura, backend e sistemas de ML. Construo sistemas multiagentes e APIs escaláveis e confiáveis, trazendo uma mentalidade de missão crítica para a engenharia de IA.',
            'Ingeniero de IA trabajando de extremo a extremo en arquitectura, backend y sistemas de ML. Construyo sistemas multiagente y APIs escalables y confiables, aportando una mentalidad de misión crítica a la ingeniería de IA.'
        ),
        
        'Remote · Full-time/Contract · International': ('Remoto · Tempo Integral/Contrato · Internacional', 'Remoto · Tiempo Completo/Contrato · Internacional'),
        'Native PT-BR · Fluent EN · Intermediate ES': ('PT-BR Nativo · EN Fluente · ES Intermediário', 'PT-BR Nativo · EN Fluido · ES Intermedio'),
        'Remote Contract/Full-time': ('Remoto Contrato/Tempo Integral', 'Remoto Contrato/Tiempo Completo'),
        'To be discussed': ('A combinar', 'A convenir'),
        
        # Pillars
        'Multi-agent systems governance': ('Governança de sistemas multiagentes', 'Gobernanza de sistemas multiagente'),
        'Production-ready RAG': ('RAG pronto para produção', 'RAG listo para producción'),
        'Multi-LLM guardrails': ('Guardrails Multi-LLM', 'Guardrails Multi-LLM'),
        'Scalable FastAPI APIs': ('APIs FastAPI escaláveis', 'APIs FastAPI escalables'),
        'LLM pipelines observability': ('Observabilidade de pipelines LLM', 'Observabilidad de pipelines LLM'),

        # Experience
        '2024 — PRESENT': ('2024 — PRESENTE', '2024 — PRESENTE'),
        'Independent': ('Independente', 'Independiente'),
        'Building production-grade agentic AI systems': ('Construindo sistemas de IA agênticos em nível de produção', 'Construyendo sistemas de IA agénticos a nivel de producción'),
        'Multi-agent orchestration architecture with guardrails and auditing': ('Arquitetura de orquestração multiagente com guardrails e auditoria', 'Arquitectura de orquestación multiagente con guardrails y auditoría'),
        'Deployment and operation of LLM APIs with end-to-end observability': ('Implantação e operação de APIs LLM com observabilidade de ponta a ponta', 'Despliegue y operación de APIs LLM con observabilidad de extremo a extremo'),
        
        'Operations Analyst — SLA Governance & Data Auditing': ('Analista de Operações — Governança de SLA & Auditoria de Dados', 'Analista de Operaciones — Gobernanza de SLA & Auditoría de Datos'),
        'SLA governance over large-scale corporate contracts': ('Governança de SLA sobre contratos corporativos de grande escala', 'Gobernanza de SLA sobre contratos corporativos a gran escala'),
        'Operational data auditing with high financial impact': ('Auditoria de dados operacionais com alto impacto financeiro', 'Auditoría de datos operativos con alto impacto financiero'),
        'Technical focal point for corporate system implementations': ('Ponto focal técnico para implementações de sistemas corporativos', 'Punto focal técnico para implementaciones de sistemas corporativos'),
        
        'Operations Analyst — Fleet & Logistics Management': ('Analista de Operações — Gestão de Frota & Logística', 'Analista de Operaciones — Gestión de Flota & Logística'),
        'Fleet and logistics management covering nationwide routes': ('Gestão de frota e logística cobrindo rotas nacionais', 'Gestión de flota y logística cubriendo rutas nacionales'),
        'Consolidation of operational data for decision-making': ('Consolidação de dados operacionais para tomada de decisão', 'Consolidación de datos operativos para la toma de decisiones'),
        
        'Operations Technician': ('Técnico de Operações', 'Técnico de Operaciones'),
        'Base operations in mission-critical environments': ('Operações de base em ambientes de missão crítica', 'Operaciones base en entornos de misión crítica'),
        'Ensured SLA guarantee and large-scale operational continuity': ('Garantia de SLA e continuidade operacional em larga escala', 'Garantía de SLA y continuidad operativa a gran escala'),

        # Education
        'Postgraduate in Machine Learning Engineering': ('Pós-Graduação em Machine Learning Engineering', 'Postgrado en Machine Learning Engineering'),
        'IN PROGRESS': ('EM ANDAMENTO', 'EN CURSO'),
        'Popularity-based recommendation systems fail in personalization.': (
            'Sistemas de recomendação baseados em popularidade falham na personalização.',
            'Los sistemas de recomendación basados en popularidad fallan en la personalización.'
        ),
        'Predictive Churn Engine. High churn rates in SaaS platforms due to reactive support.': (
            'Motor Preditivo de Churn. Altas taxas de churn em plataformas SaaS devido ao suporte reativo.',
            'Motor Predictivo de Churn. Altas tasas de churn en plataformas SaaS debido al soporte reactivo.'
        ),
        'MLOps, model deployment and ML pipelines in production.': ('MLOps, implantação de modelos e pipelines de ML em produção.', 'MLOps, despliegue de modelos y pipelines de ML en producción.'),
        'BSc in Computer Science': ('Bacharelado em Ciência da Computação', 'Licenciatura en Ciencias de la Computación'),
        'Formal foundations in algorithms, systems and distributed computing.': ('Fundamentos formais em algoritmos, sistemas e computação distribuída.', 'Fundamentos formales en algoritmos, sistemas y computación distribuida.'),
        
        # Projects
        'Multi-agent financial advisor — financial consulting with specialized agents and audited responses.': (
            'Consultor financeiro multiagente — consultoria financeira com agentes especializados e respostas auditadas.',
            'Asesor financiero multiagente — consultoría financiera con agentes especializados y respuestas auditadas.'
        ),
        '<strong>LangGraph</strong> orchestration coordinating specialized agents; <strong>multi-LLM judge</strong> system for quality and security guardrails; <strong>RAG</strong> with embeddings for knowledge base grounding; <strong>governance and auditing</strong> layer logging and validating every response before delivery.': (
            'Orquestração <strong>LangGraph</strong> coordenando agentes especializados; sistema <strong>juiz multi-LLM</strong> para guardrails de qualidade e segurança; <strong>RAG</strong> com embeddings para fundamentação na base de conhecimento; camada de <strong>governança e auditoria</strong> registrando e validando cada resposta antes da entrega.',
            'Orquestación <strong>LangGraph</strong> coordinando agentes especializados; sistema <strong>juez multi-LLM</strong> para guardrails de calidad y seguridad; <strong>RAG</strong> con embeddings para fundamentación en la base de conocimiento; capa de <strong>gobernanza y auditoría</strong> registrando y validando cada respuesta antes de la entrega.'
        ),
        
        'Edtech language learning platform with conversational agents, correction, and adaptive progression.': (
            'Plataforma edtech de aprendizado de idiomas com agentes conversacionais, correção e progressão adaptativa.',
            'Plataforma edtech de aprendizaje de idiomas con agentes conversacionales, corrección y progresión adaptativa.'
        ),
        'Multi-agent system with tutor, evaluator, and curriculum planner roles; structured feedback pipeline by student level.': (
            'Sistema multiagente com papéis de tutor, avaliador e planejador de currículo; pipeline de feedback estruturado por nível do aluno.',
            'Sistema multiagente con roles de tutor, evaluador y planificador de currículo; pipeline de feedback estructurado por nivel del estudiante.'
        ),
        'In Development': ('Em Desenvolvimento', 'En Desarrollo'),
        
        'Full-stack oncology support platform — patient tracking, clinical data, and mobile.': (
            'Plataforma full-stack de suporte oncológico — acompanhamento de pacientes, dados clínicos e mobile.',
            'Plataforma full-stack de soporte oncológico — seguimiento de pacientes, datos clínicos y mobile.'
        ),
        'React web frontend, Flutter mobile app, Node.js API, and Python auxiliary services.': (
            'Frontend web React, app mobile Flutter, API Node.js e serviços auxiliares em Python.',
            'Frontend web React, app móvil Flutter, API Node.js y servicios auxiliares en Python.'
        ),
        
        'LLM pipeline for data harmonization and enrichment with automated staged validation.': (
            'Pipeline LLM para harmonização e enriquecimento de dados com validação automatizada em estágios.',
            'Pipeline LLM para armonización y enriquecimiento de datos con validación automatizada en etapas.'
        ),
        'Staged pipeline with extraction, LLM normalization, rule-based validation, and auditable persistence.': (
            'Pipeline em estágios com extração, normalização LLM, validação baseada em regras e persistência auditável.',
            'Pipeline en etapas con extracción, normalización LLM, validación basada en reglas y persistencia auditable.'
        ),

        # Filters
        'ALL': ('TODOS', 'TODOS'),
        'AI/AGENTS': ('IA/AGENTES', 'IA/AGENTES'),
        'FULL-STACK': ('FULL-STACK', 'FULL-STACK'),
        'PIPELINE': ('PIPELINE', 'PIPELINE'),
        'AI/ML': ('IA/ML', 'IA/ML'),
        'BACKEND': ('BACKEND', 'BACKEND'),
        'DATA': ('DADOS', 'DATOS'),
        'SOFT SKILLS': ('SOFT SKILLS', 'SOFT SKILLS'),
        'DEV': ('DEV', 'DEV'),
        'OTHER': ('OUTROS', 'OTROS'),
        'PROJECTS': ('PROJETOS', 'PROYECTOS'),
        'EDUCATION': ('FORMAÇÃO', 'EDUCACIÓN'),
        'CERTIFICATIONS': ('CERTIFICAÇÕES', 'CERTIFICACIONES'),
        'COMMUNITY': ('COMUNIDADE', 'COMUNIDAD'),

        # Assistant
        "Hi! I'm vitor_ai, the portfolio assistant. I can talk about projects, tech stack, experience, education, or contact. What do you want to know?": (
            'Olá! Eu sou vitor_ai, o assistente do portfólio. Posso falar sobre projetos, stack, experiência, formação ou contato. O que você deseja saber?',
            '¡Hola! Soy vitor_ai, el asistente del portafolio. Puedo hablar sobre proyectos, stack, experiencia, educación o contacto. ¿Qué deseas saber?'
        ),
        'What is the flagship project?': ('Qual é o projeto principal?', '¿Cuál es el proyecto principal?'),
        'What is your main tech stack?': ('Qual é sua stack principal?', '¿Cuál es tu stack principal?'),
        'Experience summary': ('Resumo da experiência', 'Resumen de experiencia'),
        'How to get in touch?': ('Como entrar em contato?', '¿Cómo ponerse en contacto?'),
        "Hmm, I don't have an answer for that yet. Try asking about: projects, tech stack, experience, education, certifications, or contact — or use the suggestions above. :)": (
            'Hmm, ainda não tenho uma resposta para isso. Tente perguntar sobre: projetos, stack, experiência, formação, certificações ou contato — ou use as sugestões acima. :)',
            'Hmm, todavía no tengo una respuesta para eso. Intenta preguntar sobre: proyectos, stack, experiencia, educación, certificaciones o contacto — o usa las sugerencias anteriores. :)'
        ),

        # aria-labels (matched with the attribute so the words are not
        # replaced anywhere else on the page)
        'aria-label="Overview"': ('aria-label="Visão Geral"', 'aria-label="Visión General"'),
        'aria-label="Profile"': ('aria-label="Perfil"', 'aria-label="Perfil"'),
        'aria-label="Experience"': ('aria-label="Experiência"', 'aria-label="Experiencia"'),
        'aria-label="Education"': ('aria-label="Formação"', 'aria-label="Educación"'),
        'aria-label="Projects & Tech Stack"': ('aria-label="Projetos e Tech Stack"', 'aria-label="Proyectos y Tech Stack"'),
        'aria-label="Projects and Tech Stack"': ('aria-label="Projetos e Tech Stack"', 'aria-label="Proyectos y Tech Stack"'),
        'aria-label="Certifications"': ('aria-label="Certificações"', 'aria-label="Certificaciones"'),
        'aria-label="Achievements"': ('aria-label="Conquistas"', 'aria-label="Logros"'),
        'aria-label="Filter projects"': ('aria-label="Filtrar projetos"', 'aria-label="Filtrar proyectos"'),
        'aria-label="Filter courses by category"': ('aria-label="Filtrar cursos por categoria"', 'aria-label="Filtrar cursos por categoría"'),
        'aria-label="Filter achievements"': ('aria-label="Filtrar conquistas"', 'aria-label="Filtrar logros"'),
        'aria-label="Question for assistant"': ('aria-label="Pergunta para o assistente"', 'aria-label="Pregunta para el asistente"'),
        'aria-label="AI Assistant"': ('aria-label="Assistente de IA"', 'aria-label="Asistente de IA"'),
        'aria-label="Back to Portfolio"': ('aria-label="Voltar ao Portfólio"', 'aria-label="Volver al Portafolio"'),
        'aria-label="Open navigation menu"': ('aria-label="Abrir menu de navegação"', 'aria-label="Abrir menú de navegación"'),
        'aria-label="Main navigation"': ('aria-label="Navegação principal"', 'aria-label="Navegación principal"'),

        # project architecture notes and assistant header
        'LangGraph orchestration coordinating specialized agents; multi-LLM judge system for quality and security guardrails; RAG with embeddings for knowledge base grounding; governance and auditing layer logging and validating every response before delivery.': (
            'Orquestração LangGraph coordenando agentes especializados; sistema de júri multi-LLM para guardrails de qualidade e segurança; RAG com embeddings para ancoragem na base de conhecimento; camada de governança e auditoria registrando e validando cada resposta antes da entrega.',
            'Orquestación LangGraph coordinando agentes especializados; sistema de jurado multi-LLM para guardrails de calidad y seguridad; RAG con embeddings para anclaje en la base de conocimiento; capa de gobernanza y auditoría que registra y valida cada respuesta antes de la entrega.'
        ),
        'Two-Tower Neural Network built on PyTorch for collaborative filtering.': (
            'Rede neural Two-Tower construída em PyTorch para filtragem colaborativa.',
            'Red neuronal Two-Tower construida en PyTorch para filtrado colaborativo.'
        ),
        'Predictive churn modeling using Machine Learning, XGBoost, and FastAPI.': (
            'Modelagem preditiva de churn usando Machine Learning, XGBoost e FastAPI.',
            'Modelado predictivo de churn usando Machine Learning, XGBoost y FastAPI.'
        ),
        'vitor_ai — portfolio assistant v1.0': (
            'vitor_ai — assistente do portfólio v1.0',
            'vitor_ai — asistente del portafolio v1.0'
        ),
    # Projects added to the portfolio
    'Projects built': (
        'Projetos construídos',
        'Proyectos construidos'
    ),
    '14 years of mission-critical ops → production AI systems': (
        '14 anos de operações críticas → sistemas de IA em produção',
        '14 años de operaciones críticas → sistemas de IA en producción'
    ),
    '14 years of mission-critical operations (SLA governance, data auditing, logistics management) applied to reliable, governed, and production-ready agentic AI systems.': (
        '14 anos de operações de missão crítica (governança de SLA, auditoria de dados, gestão logística) aplicados a sistemas de IA agênticos confiáveis, governados e prontos para produção.',
        '14 años de operaciones de misión crítica (gobernanza de SLA, auditoría de datos, gestión logística) aplicados a sistemas de IA agénticos confiables, gobernados y listos para producción.'
    ),
    'Multi-tenant B2B platform in production: leads, marketplace contracts, Stripe escrow and real-time chat.': (
        'Plataforma B2B multi-tenant em produção: leads, contratos de marketplace, custódia via Stripe e chat em tempo real.',
        'Plataforma B2B multi-tenant en producción: leads, contratos de marketplace, custodia vía Stripe y chat en tiempo real.'
    ),
    'FastAPI backend and Next.js 15 frontend over PostgreSQL, with RBAC, transactional outbox, audit trail and Redis rate limiting.': (
        'Backend FastAPI e frontend Next.js 15 sobre PostgreSQL, com RBAC, transactional outbox, trilha de auditoria e rate limiting em Redis.',
        'Backend FastAPI y frontend Next.js 15 sobre PostgreSQL, con RBAC, transactional outbox, pista de auditoría y rate limiting en Redis.'
    ),
    'Medical text triage classifier served by API, with retraining orchestrated in Airflow and monitoring in Grafana.': (
        'Classificador de triagem de textos médicos servido por API, com retreino orquestrado no Airflow e monitoramento no Grafana.',
        'Clasificador de triaje de textos médicos servido por API, con reentrenamiento orquestado en Airflow y monitoreo en Grafana.'
    ),
    'TF-IDF and logistic regression baseline exported to ONNX Runtime; FastAPI service in Docker with Prometheus metrics; CI runs lint, tests and image build.': (
        'Baseline TF-IDF com regressão logística exportado para ONNX Runtime; serviço FastAPI em Docker com métricas Prometheus; o CI roda lint, testes e build da imagem.',
        'Baseline TF-IDF con regresión logística exportado a ONNX Runtime; servicio FastAPI en Docker con métricas Prometheus; el CI ejecuta lint, pruebas y build de la imagen.'
    ),
    'Workout app with personalized plans, timer-driven sessions and progress charts.': (
        'App de treino com planos personalizados, sessões com cronômetro e gráficos de evolução.',
        'App de entrenamiento con planes personalizados, sesiones con cronómetro y gráficos de evolución.'
    ),
    'Flutter app with local Hive storage, exercise search through ExerciseDB and AI suggestions with an offline fallback.': (
        'App Flutter com armazenamento local em Hive, busca de exercícios via ExerciseDB e sugestões de IA com fallback offline.',
        'App Flutter con almacenamiento local en Hive, búsqueda de ejercicios vía ExerciseDB y sugerencias de IA con fallback offline.'
    ),
    'AI tools for careers and freelancing send sensitive data to third-party clouds.': (
        'Ferramentas de IA para carreira e freelas enviam dados sensíveis para nuvens de terceiros.',
        'Las herramientas de IA para carrera y freelance envían datos sensibles a nubes de terceros.'
    ),
    'Two isolated modes: a local career pipeline on Ollama and a cloud freelance pipeline, both orchestrated in LangGraph behind FastAPI.': (
        'Dois modos isolados: um pipeline de carreira local em Ollama e um pipeline de freelas na nuvem, ambos orquestrados em LangGraph atrás do FastAPI.',
        'Dos modos aislados: un pipeline de carrera local en Ollama y un pipeline de freelance en la nube, ambos orquestados en LangGraph detrás de FastAPI.'
    ),
    # AIClinicOS
    'Clinic operating system connecting scheduling, records and AI-assisted workflows in one flow.': (
        'Sistema operacional para clínicas que conecta agenda, prontuário e fluxos assistidos por IA em um único fluxo.',
        'Sistema operativo para clínicas que conecta agenda, historia clínica y flujos asistidos por IA en un solo flujo.'
    ),
    'Next.js and TypeScript app with Tailwind, using Supabase for authentication and persistence, deployed on Vercel.': (
        'App em Next.js e TypeScript com Tailwind, usando Supabase para autenticação e persistência, publicado na Vercel.',
        'App en Next.js y TypeScript con Tailwind, usando Supabase para autenticación y persistencia, publicada en Vercel.'
    ),
    # Projects rewritten to match each repository (see the case studies)
    "Financial mentor with answers grounded in the user's data and a three-provider LLM fallback.": (
        'Mentor financeiro com respostas ancoradas nos dados do usuário e fallback entre três provedores de LLM.',
        'Mentor financiero con respuestas ancladas en los datos del usuario y fallback entre tres proveedores de LLM.'
    ),
    'Native PT-BR · Technical EN · Basic ES': ('PT-BR nativo · EN técnico · ES básico', 'PT-BR nativo · EN técnico · ES básico'),
    'cargo: "Full Stack and AI Developer"': ('cargo: "Desenvolvedor Full Stack e de IA"', 'cargo: "Desarrollador Full Stack y de IA"'),
    'org: "Independent projects"': ('org: "Projetos independentes"', 'org: "Proyectos independientes"'),
    'badge: "CURRENT"': ('badge: "ATUAL"', 'badge: "ACTUAL"'),
    'ML systems end to end: training, ONNX serving, Airflow retraining, Prometheus alerts': (
        'Sistemas de ML de ponta a ponta: treino, serving com ONNX, retreino no Airflow, alertas no Prometheus',
        'Sistemas de ML de extremo a extremo: entrenamiento, serving con ONNX, reentrenamiento en Airflow, alertas en Prometheus'
    ),
    'LLM applications with provider fallback, RAG over real catalogs and LangGraph pipelines': (
        'Aplicações com LLM com fallback de provedor, RAG sobre catálogos reais e pipelines em LangGraph',
        'Aplicaciones con LLM con fallback de proveedor, RAG sobre catálogos reales y pipelines en LangGraph'
    ),
    'Case studies where every published metric traces to a file in the repository': (
        'Estudos de caso em que cada métrica publicada aponta para um arquivo do repositório',
        'Casos de estudio en los que cada métrica publicada apunta a un archivo del repositorio'
    ),
    'MestreGrana demo live on Streamlit': ('Demo do MestreGrana no ar no Streamlit', 'Demo de MestreGrana publicada en Streamlit'),
    "Financial education assistant that answers from the user's own profile and transactions, by text or voice.": (
        'Assistente de educação financeira que responde a partir do perfil e das transações do próprio usuário, por texto ou voz.',
        'Asistente de educación financiera que responde a partir del perfil y las transacciones del propio usuario, por texto o voz.'
    ),
    "Streamlit app with prompts grounded in the user's data and one Groq → Gemini → OpenAI fallback chain shared by the text and voice chat; Neon Postgres for audit and consent records, LGPD consent flow.": (
        'App em Streamlit com prompts ancorados nos dados do usuário e uma cadeia de fallback Groq → Gemini → OpenAI compartilhada pelo chat de texto e de voz; Postgres no Neon para auditoria e consentimento, fluxo de consentimento LGPD.',
        'App en Streamlit con prompts anclados en los datos del usuario y una cadena de fallback Groq → Gemini → OpenAI compartida por el chat de texto y de voz; Postgres en Neon para auditoría y consentimiento, flujo de consentimiento LGPD.'
    ),
    'k: "LLM providers", v: "3, with fallback"': ('k: "Provedores de LLM", v: "3, com fallback"', 'k: "Proveedores de LLM", v: "3, con fallback"'),
    'English conversation tutor with grammar corrections, voice and flashcards, online and offline.': (
        'Tutor de conversação em inglês com correção gramatical, voz e flashcards, online e offline.',
        'Tutor de conversación en inglés con corrección gramatical, voz y flashcards, online y offline.'
    ),
    'Streamlit tutor behind a Groq, OpenAI, Gemini and Perplexity fallback chain; Flutter app that switches to an on-device model through MediaPipe when offline.': (
        'Tutor em Streamlit atrás de uma cadeia de fallback Groq, OpenAI, Gemini e Perplexity; app Flutter que muda para um modelo no aparelho via MediaPipe quando está offline.',
        'Tutor en Streamlit detrás de una cadena de fallback Groq, OpenAI, Gemini y Perplexity; app Flutter que cambia a un modelo en el dispositivo vía MediaPipe sin conexión.'
    ),
    'v: "PRIVATE REPO"': ('v: "REPO PRIVADO"', 'v: "REPO PRIVADO"'),
    'Two-tower neural recommender trained on 2.2M RetailRocket interactions, evaluated separately for repetition and discovery.': (
        'Recomendador neural two-tower treinado com 2,2 milhões de interações do RetailRocket, avaliado separando repetição e descoberta.',
        'Recomendador neuronal two-tower entrenado con 2,2 millones de interacciones de RetailRocket, evaluado separando repetición y descubrimiento.'
    ),
    'PyTorch two-tower model in a DVC pipeline tracked by MLflow; FAISS retrieval, Redis cache and a FastAPI service with popularity fallback, validated on a local Kubernetes cluster.': (
        'Modelo two-tower em PyTorch num pipeline DVC rastreado pelo MLflow; recuperação com FAISS, cache no Redis e API FastAPI com fallback de popularidade, validada num cluster Kubernetes local.',
        'Modelo two-tower en PyTorch en un pipeline DVC rastreado por MLflow; recuperación con FAISS, caché en Redis y API FastAPI con fallback de popularidad, validada en un clúster Kubernetes local.'
    ),
    'v: "0.123 (36× popularity)"': ('v: "0,123 (36× popularidade)"', 'v: "0,123 (36× popularidad)"'),
    'Oral-cancer risk platform where a rigorous benchmark proved the dataset had no learnable signal, and the project says so.': (
        'Plataforma de risco de câncer oral em que um benchmark rigoroso provou que o dataset não tinha sinal aprendível, e o projeto diz isso.',
        'Plataforma de riesgo de cáncer oral en la que un benchmark riguroso demostró que el dataset no tenía señal aprendible, y el proyecto lo dice.'
    ),
    'PyTorch classifier with Pandera contracts, calibration and leakage audits; FastAPI backend with an encrypted, hash-chained audit trail and a Groq → Gemini circuit breaker; Next.js frontend.': (
        'Classificador em PyTorch com contratos Pandera, calibração e auditorias de vazamento; backend FastAPI com trilha de auditoria cifrada e encadeada por hash e circuit breaker Groq → Gemini; frontend Next.js.',
        'Clasificador en PyTorch con contratos Pandera, calibración y auditorías de fuga; backend FastAPI con pista de auditoría cifrada y encadenada por hash y circuit breaker Groq → Gemini; frontend Next.js.'
    ),
    'v: "0.50 (documented null result)"': ('v: "0,50 (resultado nulo documentado)"', 'v: "0,50 (resultado nulo documentado)"'),
    'Telecom churn classifier whose decision threshold is derived from the cost of a missed customer.': (
        'Classificador de churn em telecom cujo limiar de decisão é derivado do custo de perder um cliente.',
        'Clasificador de churn en telecomunicaciones cuyo umbral de decisión se deriva del costo de perder un cliente.'
    ),
    'PyTorch MLP compared with logistic regression and XGBoost in MLflow; threshold tuned on validation cost; FastAPI with Pydantic and Pandera validation, Prometheus metrics, Docker and Nginx.': (
        'MLP em PyTorch comparado com regressão logística e XGBoost no MLflow; limiar ajustado pelo custo na validação; FastAPI com validação Pydantic e Pandera, métricas Prometheus, Docker e Nginx.',
        'MLP en PyTorch comparado con regresión logística y XGBoost en MLflow; umbral ajustado por costo en validación; FastAPI con validación Pydantic y Pandera, métricas Prometheus, Docker y Nginx.'
    ),
    'v: "89.8% at threshold 0.37"': ('v: "89,8% no limiar 0,37"', 'v: "89,8% con umbral 0,37"'),
    "Wine sommelier that answers from a real 570-label catalog instead of the model's memory.": (
        'Sommelier de vinhos que responde a partir de um catálogo real de 570 rótulos, e não da memória do modelo.',
        'Sommelier de vinos que responde a partir de un catálogo real de 570 etiquetas, y no de la memoria del modelo.'
    ),
    'ChromaDB retrieval with price and country filters parsed from the question, a LangChain agent with tools, and a multi-LLM judge mode with fallbacks.': (
        'Busca no ChromaDB com filtros de preço e país tirados da pergunta, um agente LangChain com ferramentas e um modo juiz multi-LLM com fallbacks.',
        'Búsqueda en ChromaDB con filtros de precio y país extraídos de la pregunta, un agente LangChain con herramientas y un modo juez multi-LLM con fallbacks.'
    ),
    'k: "Catalog", v: "570 wines"': ('k: "Catálogo", v: "570 vinhos"', 'k: "Catálogo", v: "570 vinos"'),
    'TF-IDF and logistic regression exported to ONNX Runtime with a parity check that blocks a bad export; FastAPI in Docker with Prometheus alerts tested by promtool; CI publishes the image to GHCR.': (
        'TF-IDF e regressão logística exportados para ONNX Runtime com checagem de paridade que barra uma exportação ruim; FastAPI em Docker com alertas do Prometheus testados pelo promtool; o CI publica a imagem no GHCR.',
        'TF-IDF y regresión logística exportados a ONNX Runtime con verificación de paridad que bloquea una exportación mala; FastAPI en Docker con alertas de Prometheus probadas con promtool; el CI publica la imagen en GHCR.'
    ),
    'v: "4.09× inference, 1.35× via API"': ('v: "4,09× inferência, 1,35× via API"', 'v: "4,09× inferencia, 1,35× vía API"'),
    'Workout app with personalized plans, timer-driven sessions and progress charts, built to work without signal.': (
        'App de treino com planos personalizados, sessões com cronômetro e gráficos de evolução, feito para funcionar sem sinal.',
        'App de entrenamiento con planes personalizados, sesiones con cronómetro y gráficos de evolución, hecha para funcionar sin señal.'
    ),
    'Flutter app, local-first on Hive with a sync queue to Firebase, posture feedback from on-device ML Kit pose detection, and AI plans under a usage quota.': (
        'App Flutter local-first no Hive com fila de sincronização para o Firebase, feedback de postura pela detecção de pose do ML Kit no aparelho e planos de IA sob cota de uso.',
        'App Flutter local-first en Hive con cola de sincronización a Firebase, feedback de postura por la detección de pose de ML Kit en el dispositivo y planes de IA con cuota de uso.'
    ),
    'Clinic operating layer (DrPilot OS) coordinating AI agents for scheduling, patient messages, clinical notes and reporting.': (
        'Camada operacional para clínicas (DrPilot OS) que coordena agentes de IA para agenda, mensagens aos pacientes, notas clínicas e relatórios.',
        'Capa operativa para clínicas (DrPilot OS) que coordina agentes de IA para agenda, mensajes a pacientes, notas clínicas e informes.'
    ),
    'Next.js frontend and FastAPI backend over PostgreSQL on Supabase with row-level security per clinic, an append-only clinical audit log and Redis workers for reminders.': (
        'Frontend Next.js e backend FastAPI sobre PostgreSQL no Supabase com row-level security por clínica, log de auditoria clínica append-only e workers Redis para lembretes.',
        'Frontend Next.js y backend FastAPI sobre PostgreSQL en Supabase con row-level security por clínica, registro de auditoría clínica append-only y workers Redis para recordatorios.'
    ),
    'label: "Case study"': ('label: "Estudo de caso"', 'label: "Caso de estudio"'),
    'label: "Product page"': ('label: "Página do produto"', 'label: "Página del producto"'),
    "The flagship project is MESTREGRANA — a financial mentor that answers from the user's own data, with a Groq → Gemini → OpenAI fallback chain. Other projects: VITORIUM (MLOps for medical text), TwinRank AI (two-tower recommender), RetentIA (cost-tuned churn model), Aether Oncology (a documented null result), Harmoniz.AI (catalog RAG), VektorWork (LangGraph pipelines), Rankium Systems (multi-tenant B2B platform), AIClinicOS, FluencyForge and Corpo em Ação. Each one has a case study linked in the Projects & Tech Stack section.": (
        'O projeto principal é o MESTREGRANA — um mentor financeiro que responde a partir dos dados do próprio usuário, com cadeia de fallback Groq → Gemini → OpenAI. Outros projetos: VITORIUM (MLOps para textos médicos), TwinRank AI (recomendador two-tower), RetentIA (churn com limiar por custo), Aether Oncology (um resultado nulo documentado), Harmoniz.AI (RAG sobre catálogo), VektorWork (pipelines em LangGraph), Rankium Systems (plataforma B2B multi-tenant), AIClinicOS, FluencyForge e Corpo em Ação. Cada um tem um estudo de caso linkado na seção Projetos & Stack.',
        'El proyecto principal es MESTREGRANA — un mentor financiero que responde a partir de los datos del propio usuario, con cadena de fallback Groq → Gemini → OpenAI. Otros proyectos: VITORIUM (MLOps para textos médicos), TwinRank AI (recomendador two-tower), RetentIA (churn con umbral por costo), Aether Oncology (un resultado nulo documentado), Harmoniz.AI (RAG sobre catálogo), VektorWork (pipelines en LangGraph), Rankium Systems (plataforma B2B multi-tenant), AIClinicOS, FluencyForge y Corpo em Ação. Cada uno tiene un caso de estudio enlazado en la sección Proyectos & Stack.'
    ),
    'Main stack: ML → PyTorch, scikit-learn, MLflow, DVC, ONNX · AI/LLM → LangGraph, LangChain, RAG · Backend → Python, FastAPI · Data → PostgreSQL, MongoDB · Frontend → Next.js, Flutter · Infra → Docker, Airflow, Prometheus, GitHub Actions.': (
        'Stack principal: ML → PyTorch, scikit-learn, MLflow, DVC, ONNX · IA/LLM → LangGraph, LangChain, RAG · Backend → Python, FastAPI · Dados → PostgreSQL, MongoDB · Frontend → Next.js, Flutter · Infra → Docker, Airflow, Prometheus, GitHub Actions.',
        'Stack principal: ML → PyTorch, scikit-learn, MLflow, DVC, ONNX · IA/LLM → LangGraph, LangChain, RAG · Backend → Python, FastAPI · Datos → PostgreSQL, MongoDB · Frontend → Next.js, Flutter · Infra → Docker, Airflow, Prometheus, GitHub Actions.'
    ),
    'Experience summary: 14 years of mission-critical operations at ECT/Correios, 2011 to 2026 (SLA governance, data auditing, fleet and logistics management), and since 2024 building ML and AI systems in independent projects with Python, FastAPI, PyTorch, LangGraph and Docker.': (
        'Resumo da experiência: 14 anos de operações de missão crítica na ECT/Correios, de 2011 a 2026 (governança de SLA, auditoria de dados, gestão de frota e logística), e desde 2024 construindo sistemas de ML e IA em projetos independentes com Python, FastAPI, PyTorch, LangGraph e Docker.',
        'Resumen de experiencia: 14 años de operaciones de misión crítica en ECT/Correios, de 2011 a 2026 (gobernanza de SLA, auditoría de datos, gestión de flota y logística), y desde 2024 construyendo sistemas de ML e IA en proyectos independientes con Python, FastAPI, PyTorch, LangGraph y Docker.'
    ),
    }

    content = join_string_literals(content)

    # The source page ships a rendered toggle; restore the placeholders so each
    # variant can mark its own link active.
    content = re.sub(r'<a href="dashboard\.en\.html" class="[^"]*">',
                     '<a href="dashboard.en.html" class="__EN_ACTIVE__">', content)
    content = re.sub(r'<a href="dashboard\.pt\.html" class="[^"]*">',
                     '<a href="dashboard.pt.html" class="__PT_ACTIVE__">', content)
    content = re.sub(r'<a href="dashboard\.es\.html" class="[^"]*">',
                     '<a href="dashboard.es.html" class="__ES_ACTIVE__">', content)

    pt_content = content
    es_content = content
    en_content = content

    # Apply toggle classes properly
    en_content = en_content.replace('__EN_ACTIVE__', 'active-lang').replace('__PT_ACTIVE__', '').replace('__ES_ACTIVE__', '')
    pt_content = pt_content.replace('__EN_ACTIVE__', '').replace('__PT_ACTIVE__', 'active-lang').replace('__ES_ACTIVE__', '')
    es_content = es_content.replace('__EN_ACTIVE__', '').replace('__PT_ACTIVE__', '').replace('__ES_ACTIVE__', 'active-lang')

    for eng, (pt, es) in replacements.items():
        pt_content = pt_content.replace(eng, pt)
        es_content = es_content.replace(eng, es)
    # Case study links: the PT dashboard opens the PT case pages; ES has none, so it keeps EN.
    pt_content = re.sub(r'url: "([\w.-]+)/"', r'url: "\1/index.pt.html"', pt_content)
        
    # Also change HTML lang attribute
    pt_content = pt_content.replace('<html lang="en"', '<html lang="pt-BR"')
    es_content = es_content.replace('<html lang="en"', '<html lang="es"')

    with open(os.path.join(base_dir, 'dashboard.en.html'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(en_content)
    with open(os.path.join(base_dir, 'dashboard.pt.html'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(pt_content)
    with open(os.path.join(base_dir, 'dashboard.es.html'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(es_content)
        
    # Default dashboard is EN + browser-language detection (see with_lang_detect)
    with open(os.path.join(base_dir, 'dashboard.html'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(with_lang_detect(en_content, 'dashboard.pt.html', 'dashboard.es.html'))

if __name__ == '__main__':
    main()
