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
        '15 years of mission-critical ops → production AI systems': ('15 anos de operações críticas → sistemas de IA em produção', '15 años de operaciones críticas → sistemas de IA en producción'),

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
        'AI projects': ('Projetos de IA', 'Proyectos de IA'),
        'Languages (PT · EN · ES)': ('Idiomas (PT · EN · ES)', 'Idiomas (PT · EN · ES)'),
        'Continuous education certificates': ('Certificados de educação contínua', 'Certificados de educación continua'),

        '15 years of mission-critical operations (SLA governance, data auditing, logistics management) applied to reliable, governed, and production-ready agentic AI systems.': (
            '15 anos de operações de missão crítica (governança de SLA, auditoria de dados, gestão logística) aplicados a sistemas de IA agênticos confiáveis, governados e prontos para produção.',
            '15 años de operaciones de misión crítica (gobernanza de SLA, auditoría de datos, gestión logística) aplicados a sistemas de IA agénticos confiables, gobernados y listos para producción.'
        ),
        
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
        'Freelancers rely on high-cost cloud tools for complex workflows, without data ownership.': (
            'Freelancers dependem de ferramentas cloud de alto custo para fluxos de trabalho complexos, sem propriedade dos dados.',
            'Los freelancers dependen de herramientas en la nube de alto costo para flujos de trabajo complejos, sin propiedad de los datos.'
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
        )
    }

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
