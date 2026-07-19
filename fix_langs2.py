import re

with open('build_langs.py', 'r', encoding='utf-8') as f:
    code = f.read()

new_replacements = """
        # --- NEW HIGHLIGHTS ---
        'Engineering <span class="g">Highlights.</span>': ('Destaques de <span class="g">Engenharia.</span>', 'Aspectos Destacados de <span class="g">Ingeniería.</span>'),
        'Engineering <span class="g">Product,</span><br>Not Just <span class="g">Code.</span>': ('Engenharia de <span class="g">Produto,</span><br>Não Apenas <span class="g">Código.</span>', 'Ingeniería de <span class="g">Producto,</span><br>No Sólo <span class="g">Código.</span>'),
        'Architectures that<br><span class="g">generate business value.</span>': ('Arquiteturas que<br><span class="g">geram valor de negócio.</span>', 'Arquitecturas que<br><span class="g">generan valor de negocio.</span>'),
        
        'The real challenge isn\\'t building AI — it\\'s trusting it in production. My projects target governance, guardrails and hallucination control.': (
            'O verdadeiro desafio não é construir IA — é confiar nela em produção. Meus projetos focam em governança, guardrails e controle de alucinações.',
            'El verdadero desafío no es construir IA — es confiar en ella en producción. Mis proyectos se centran en gobernanza, guardrails y control de alucinaciones.'
        ),
        
        'With 15+ years of mission-critical operations experience, I don\\'t just write scripts—I architect resilient systems. I\\'ve spent over a decade managing high-pressure logistics where downtime means total failure. That operational maturity is the foundation of my engineering.': (
            'Com mais de 15 anos de experiência em operações de missão crítica, eu não escrevo apenas scripts — eu arquiteto sistemas resilientes. Passei mais de uma década gerenciando logística de alta pressão, onde a inatividade significa falha total. Essa maturidade operacional é a base da minha engenharia.',
            'Con más de 15 años de experiencia en operaciones de misión crítica, no solo escribo scripts — diseño sistemas resilientes. He pasado más de una década gestionando logística de alta presión donde el tiempo de inactividad significa fracaso total. Esa madurez operativa es la base de mi ingeniería.'
        ),
        'I focus on systems that are observable, gracefully degrading, and maintainable. I build solutions to solve the real business problem, not just the technical challenge.': (
            'Foco em sistemas observáveis, de degradação suave e fáceis de manter. Construo soluções para resolver o problema real de negócio, não apenas o desafio técnico.',
            'Me enfoco en sistemas observables, con degradación elegante y fáciles de mantener. Construyo soluciones para resolver el problema de negocio real, no solo el desafío técnico.'
        ),
        
        '15+ Years': ('15+ Anos', '15+ Años'),
        'Operations and reliability mindset': ('Mentalidade de operação e confiabilidade', 'Mentalidad de operación y confiabilidad'),
        'AI Systems': ('Sistemas de IA', 'Sistemas de IA'),
        'Agents, RAG, orchestration, data pipelines': ('Agentes, RAG, orquestração, pipelines de dados', 'Agentes, RAG, orquestración, pipelines de datos'),
        'Available for global opportunities': ('Disponível para oportunidades globais', 'Disponible para oportunidades globales'),
        
        'MISSION CRITICAL': ('MISSÃO CRÍTICA', 'MISIÓN CRÍTICA'),
        'I operated for 15 years in zero-tolerance-for-failure environments. That mindset translates to defensive coding, robust error handling, and architectures built for resilience.': (
            'Operei 15 anos em ambientes de tolerância zero a falhas. Essa mentalidade se traduz em código defensivo, tratamento robusto de erros e arquiteturas construídas para resiliência.',
            'Operé 15 años en entornos de tolerancia cero a fallos. Esa mentalidad se traduce en código defensivo, manejo robusto de errores y arquitecturas construidas para la resiliencia.'
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
        'Freelancers depend on high-cost cloud tools for complex workflows with no data ownership.': ('Freelancers dependem de ferramentas cloud de alto custo para fluxos de trabalho complexos, sem propriedade dos dados.', 'Los freelancers dependen de herramientas en la nube de alto costo para flujos de trabajo complejos sin propiedad de datos.'),
        'Self-Hosted Automation Platform': ('Plataforma de Automação Self-Hosted', 'Plataforma de Automatización Self-Hosted'),
        
        'B2B SAAS &middot; PREDICTIVE': ('B2B SAAS &middot; PREDITIVO', 'B2B SAAS &middot; PREDICTIVO'),
        'High churn rates in SaaS platforms due to reactive support.': ('Altas taxas de churn em plataformas SaaS devido ao suporte reativo.', 'Altas tasas de churn en plataformas SaaS debido al soporte reactivo.'),
        'Predictive Churn Engine': ('Motor Preditivo de Churn', 'Motor Predictivo de Churn'),
        
        'HEALTHTECH &middot; DATA': ('HEALTHTECH &middot; DADOS', 'HEALTHTECH &middot; DATOS'),
        'Scalably correlating complex biometric data.': ('Correlacionando de forma escalável dados biométricos complexos.', 'Correlacionando de forma escalable datos biometricos complejos.'),

        'CURRENT_PROFILE': ('PERFIL_ATUAL', 'PERFIL_ACTUAL'),
        'AVAILABLE': ('DISPONÍVEL', 'DISPONIBLE'),
        'FOCUS': ('FOCO', 'ENFOQUE'),
"""

if "    }\n\n    # Generate EN" in code:
    code = code.replace("    }\\n\\n    # Generate EN", new_replacements + "    }\\n\\n    # Generate EN")
    with open('build_langs.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Updated build_langs.py via replace")
else:
    print("Could not find replacement anchor in build_langs.py")
