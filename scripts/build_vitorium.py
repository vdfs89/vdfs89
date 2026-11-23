# -*- coding: utf-8 -*-
"""Build the VITORIUM case study pages (vitorium/index.html and index.pt.html).

The page text lives here, one entry per key as (English, Portuguese), and the
markup lives in scripts/vitorium_case/template.html. Every number on the page
comes from a versioned file in github.com/vdfs89/vitorium-mednlp-mlops; the
source path is printed under each figure.

Usage: python scripts/build_vitorium.py
"""

import io
import json
import os
import re

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(REPO_DIR, "scripts", "vitorium_case", "template.html")
OUT_DIR = os.path.join(REPO_DIR, "vitorium")

LANGS = {
    "en": {"file": "index.html", "html_lang": "en", "canonical": "https://vitorsilva.page/vitorium/",
           "home_href": "../", "en_on": "on", "pt_on": ""},
    "pt": {"file": "index.pt.html", "html_lang": "pt-BR", "canonical": "https://vitorsilva.page/vitorium/index.pt.html",
           "home_href": "../index.pt.html", "en_on": "", "pt_on": "on"},
}

S = {
    "title": ("VITORIUM — End-to-end MLOps for medical text triage | Vitor Silva",
              "VITORIUM — MLOps ponta a ponta para triagem de textos médicos | Vitor Silva"),
    "og_title": ("VITORIUM — End-to-end MLOps for medical text triage",
                 "VITORIUM — MLOps ponta a ponta para triagem de textos médicos"),
    "meta_desc": ("Case study: a medical-text classifier retrained by Airflow, shipped by GitHub Actions, served with ONNX Runtime and monitored with Prometheus and Grafana. Live in-browser demo.",
                  "Case: classificador de textos médicos retreinado pelo Airflow, publicado pelo GitHub Actions, servido com ONNX Runtime e monitorado com Prometheus e Grafana. Demo ao vivo no navegador."),
    "nav_label": ("Case study sections", "Seções do case"),
    "nav_demo": ("Demo", "Demo"),
    "nav_arch": ("Architecture", "Arquitetura"),
    "nav_video": ("Video", "Vídeo"),
    "nav_back": ("← All projects", "← Todos os projetos"),
    "crumb_projects": ("Projects", "Projetos"),
    "crumb_tag": ("Healthcare · MLOps", "Saúde · MLOps"),
    "phase": ("Phase 3", "Fase 3"),
    "chip_grade": ("Graded 90/90", "Nota 90/90"),
    "hero_sub": ("An end-to-end MLOps pipeline that sorts medical texts by urgency: retrained by Airflow, shipped by GitHub Actions, served with ONNX Runtime and watched by Prometheus and Grafana.",
                 "Um pipeline de MLOps ponta a ponta que classifica textos médicos por urgência: retreinado pelo Airflow, publicado pelo GitHub Actions, servido com ONNX Runtime e vigiado por Prometheus e Grafana."),
    "hero_copy": ("The model is deliberately simple (TF-IDF and logistic regression). What this project shows is the engineering around it: parity checks that block a bad export, latency measured end to end instead of in isolation, and alert rules that are unit-tested before they ever fire.",
                  "O modelo é propositalmente simples (TF-IDF e regressão logística). O que o projeto mostra é a engenharia em volta dele: checagens de paridade que barram uma exportação ruim, latência medida de ponta a ponta e não isolada, e regras de alerta testadas antes de dispararem pela primeira vez."),
    "btn_demo": ("▶ Try the live demo", "▶ Testar a demo ao vivo"),
    "btn_video": ("Watch the 4-min video", "Ver o vídeo de 4 min"),
    "notice_k": ("Not a clinical tool.", "Não é uma ferramenta clínica."),
    "notice": ("The dataset (Medical Abstracts TC Corpus, 14,438 abstracts) has no urgency labels. The three tiers are a heuristic regrouping of its five condition categories, made for an MLOps exercise. They do not reflect real triage protocols such as Manchester or ESI.",
               "O dataset (Medical Abstracts TC Corpus, 14.438 abstracts) não tem rótulos de urgência. Os três níveis são um reagrupamento heurístico das suas cinco categorias de condição, feito para um exercício de MLOps. Eles não refletem protocolos reais de triagem, como Manchester ou ESI."),

    "num_prompt": ("Results", "Resultados"),
    "num_h2a": ("Measured, not estimated.", "Medido, não estimado."),
    "num_h2b": ("Including the numbers that look worse.", "Inclusive os números que parecem piores."),
    "num_lead": ("Each figure comes from a versioned file in the repository, written by a script you can rerun. The source path is under every number.",
                 "Cada número vem de um arquivo versionado no repositório, gerado por um script que pode ser rodado de novo. O caminho da fonte está embaixo de cada número."),
    "v1": ("4.09×", "4,09×"),
    "v2": ("1.35×", "1,35×"),
    "v3": ("2,888/2,888", "2.888/2.888"),
    "v4": ("0.62", "0,62"),
    "n1_k": ("Faster pure inference with ONNX", "Inferência pura mais rápida com ONNX"),
    "n1_d": ("1.084 ms → 0.265 ms per text, scikit-learn vs ONNX Runtime, same process, no HTTP.",
             "1,084 ms → 0,265 ms por texto, scikit-learn vs. ONNX Runtime, no mesmo processo, sem HTTP."),
    "n2_k": ("Faster through the real API (p50)", "Mais rápido na API real (p50)"),
    "n2_d": ("3.40 ms → 2.51 ms per request. HTTP, FastAPI and Pydantic dominate the response time, so the end-to-end gain is smaller. Both numbers are published.",
             "3,40 ms → 2,51 ms por requisição. HTTP, FastAPI e Pydantic dominam o tempo de resposta, então o ganho de ponta a ponta é menor. Os dois números estão publicados."),
    "n3_k": ("Same label from ONNX and scikit-learn", "Mesmo rótulo no ONNX e no scikit-learn"),
    "n3_d": ("Every test text, max probability difference 1.6e-7. The export fails the build if parity breaks.",
             "Todos os textos de teste, diferença máxima de probabilidade de 1,6e-7. A exportação quebra o build se a paridade falhar."),
    "n4_k": ("Macro F1 on held-out data", "Macro F1 no conjunto de teste"),
    "n4_d": ("Accuracy 0.62 on 2,888 texts. The weak class is “normal” (F1 0.46), a catch-all category that overlaps the others. Fine for an MLOps exercise, not for triage.",
             "Acurácia de 0,62 em 2.888 textos. A classe fraca é “normal” (F1 0,46), uma categoria genérica que se sobrepõe às outras. Serve para um exercício de MLOps, não para triagem."),
    "n5_k": ("Alert rules unit-tested with promtool", "Regras de alerta testadas com promtool"),
    "n5_d": ("API down, 5xx rate, p95 latency and a prediction-mix shift that works as a live drift proxy.",
             "API fora do ar, taxa de 5xx, latência p95 e um desvio na distribuição das predições que funciona como proxy de drift em tempo real."),
    "n6_k": ("Airflow DAG tasks succeeded", "Tasks da DAG do Airflow com sucesso"),
    "n6_d": ("A real Airflow 2.10.5 run reproduced the versioned metrics exactly and re-checked ONNX parity.",
             "Uma execução real no Airflow 2.10.5 reproduziu exatamente as métricas versionadas e conferiu de novo a paridade do ONNX."),

    "demo_prompt": ("Live demo", "Demo ao vivo"),
    "demo_h2a": ("The trained model,", "O modelo treinado,"),
    "demo_h2b": ("running in your browser.", "rodando no seu navegador."),
    "demo_lead": ("No server and nothing to wake up. The page downloads the trained weights once (about 340 KB compressed) and classifies on your device, so your text never leaves it. The model was trained on English abstracts, so write in English.",
                  "Sem servidor e sem nada para acordar. A página baixa os pesos treinados uma vez (cerca de 340 KB comprimidos) e classifica no seu aparelho, então o texto nunca sai dele. O modelo foi treinado com abstracts em inglês, então escreva em inglês."),
    "demo_input": ("Medical text (English)", "Texto médico (em inglês)"),
    "demo_placeholder": ("Paste or type a clinical description in English…", "Cole ou digite uma descrição clínica em inglês…"),
    "demo_samples": ("Example texts", "Textos de exemplo"),
    "s_cardiac": ("Chest pain", "Dor no peito"),
    "s_stroke": ("Stroke", "AVC"),
    "s_cancer": ("Colon cancer", "Câncer de cólon"),
    "s_ulcer": ("Gastric ulcer", "Úlcera gástrica"),
    "s_sepsis": ("Inflammation study", "Estudo de inflamação"),
    "s_ood": ("Portuguese text (known failure)", "Texto em português (falha conhecida)"),
    "demo_loading": ("Loading model…", "Carregando o modelo…"),
    "demo_output": ("Predicted urgency tier", "Nível de urgência previsto"),
    "demo_terms": ("Terms that pushed this prediction", "Termos que puxaram esta predição"),
    "demo_meta_idle": ("Pick an example or write your own, then classify.", "Escolha um exemplo ou escreva o seu e classifique."),
    "demo_warn": ("Low confidence: the model found few words it knows. It falls back to “normal” on text it does not understand, which is the most dangerous error in triage and one reason this is not a clinical tool.",
                  "Confiança baixa: o modelo encontrou poucas palavras que conhece. Em texto que ele não entende, ele cai para “normal”, que é o erro mais perigoso em triagem e um dos motivos para não ser uma ferramenta clínica."),
    "demo_foot": ("How it works: the same TF-IDF vocabulary, IDF weights and logistic-regression coefficients as models/model.joblib, re-implemented in about 80 lines of JavaScript. Checked against scikit-learn on all 2,888 test texts: 100% same label, max probability difference 9e-7 (from rounding the weights).",
                  "Como funciona: o mesmo vocabulário TF-IDF, os mesmos pesos IDF e coeficientes da regressão logística do models/model.joblib, reimplementados em cerca de 80 linhas de JavaScript. Conferido contra o scikit-learn nos 2.888 textos de teste: 100% de rótulos iguais, diferença máxima de probabilidade de 9e-7 (do arredondamento dos pesos)."),

    "arch_prompt": ("Architecture", "Arquitetura"),
    "arch_h2a": ("A pipeline,", "Um pipeline,"),
    "arch_h2b": ("not an isolated endpoint.", "não um endpoint isolado."),
    "arch_lead": ("Batch retraining and real-time serving run the same training code. Training is deterministic (seed 42): the Airflow run reproduced the versioned metrics exactly, and every push retrains, exports and tests the model before packing it into the image the API serves.",
                  "O retreino em batch e a inferência em tempo real usam o mesmo código de treino. O treino é determinístico (seed 42): a execução no Airflow reproduziu exatamente as métricas versionadas, e cada push retreina, exporta e testa o modelo antes de empacotá-lo na imagem que a API serve."),
    "svg_title": ("VITORIUM architecture", "Arquitetura do VITORIUM"),
    "svg_desc": ("Three lanes. Retraining: an Airflow DAG runs ingest_data, train_model, export_onnx and save_model_report weekly. CI/CD: GitHub Actions runs ruff, trains and exports the model, runs pytest with Pandera schemas, builds and smoke-tests the Docker image and pushes it to GHCR tagged by commit SHA. Serving: the FastAPI app serves the ONNX model, Prometheus scrapes its metrics and evaluates four alert rules, and Grafana shows a provisioned dashboard.",
                 "Três faixas. Retreino: uma DAG do Airflow roda ingest_data, train_model, export_onnx e save_model_report toda semana. CI/CD: o GitHub Actions roda o ruff, treina e exporta o modelo, roda o pytest com schemas Pandera, faz o build e o smoke test da imagem Docker e publica no GHCR com a tag do SHA do commit. Serviço: a API FastAPI serve o modelo ONNX, o Prometheus coleta as métricas e avalia quatro regras de alerta, e o Grafana mostra um dashboard provisionado."),
    "lane1": ("RETRAINING · AIRFLOW DAG · @WEEKLY", "RETREINO · DAG DO AIRFLOW · @WEEKLY"),
    "l1a": ("14,438 abstracts", "14.438 abstracts"),
    "l1c": ("fails if parity breaks", "falha sem paridade"),
    "lane2": ("CI/CD · GITHUB ACTIONS · EVERY PUSH", "CI/CD · GITHUB ACTIONS · A CADA PUSH"),
    "l2b": ("parity check vs sklearn", "paridade vs. sklearn"),
    "l2c": ("+ Pandera schemas", "+ schemas Pandera"),
    "l2e": ("tag = commit SHA", "tag = SHA"),
    "lane3": ("SERVING · DOCKER COMPOSE", "SERVIÇO · DOCKER COMPOSE"),
    "l3a": ("non-root slim image · sklearn fallback", "imagem slim sem root · fallback sklearn"),
    "l3b1": ("4 alert rules + recording rules", "4 regras de alerta + recording rules"),
    "l3b2": ("unit-tested with promtool", "testadas com promtool"),
    "l3c1": ("“VITORIUM API” dashboard", "dashboard “VITORIUM API”"),
    "l3c2": ("provisioned as code", "provisionado como código"),

    "story_prompt": ("Engineering decisions", "Decisões de engenharia"),
    "story_h2a": ("Four calls worth explaining", "Quatro decisões que valem explicar"),
    "story_h2b": ("in an interview.", "numa entrevista."),
    "st1_k": ("Errata", "Errata"),
    "st1_h": ("The 7.70× speedup was wrong, so I took it down.", "O ganho de 7,70× estava errado, então eu tirei do ar."),
    "st1_p1": ("Up to v0.1.1 the README claimed a 7.70× ONNX speedup. Then a parity check showed that the stock skl2onnx export was not the same model: it dropped the stop words, and 35 of 2,888 labels (about 1.2%) disagreed. It also failed to load in the slim Docker image because it depended on a system locale.",
               "Até a v0.1.1 o README dizia que o ONNX era 7,70× mais rápido. Uma checagem de paridade mostrou que a exportação padrão do skl2onnx não era o mesmo modelo: ela descartava as stop words, e 35 de 2.888 rótulos (cerca de 1,2%) divergiam. Ela também não carregava na imagem Docker slim, porque dependia de um locale do sistema."),
    "st1_p2": ("I rewrote the exporter, made the export fail whenever parity breaks, re-measured everything and kept the errata in the README. A faster model that answers differently is not the same model.",
               "Reescrevi o exportador, fiz a exportação falhar sempre que a paridade quebra, medi tudo de novo e mantive a errata no README. Um modelo mais rápido que responde diferente não é o mesmo modelo."),
    "st2_k": ("Latency", "Latência"),
    "st2_h": ("4× in isolation, 1.35× where users feel it.", "4× isolado, 1,35× onde o usuário sente."),
    "st2_p1": ("Pure inference got 4.09× faster. Through the API, the median request improved 1.35×, because HTTP, FastAPI and Pydantic take most of the 2.5 ms. I measured with two identical uvicorn servers that differed only in the backend, over five interleaved rounds of 300 requests.",
               "A inferência pura ficou 4,09× mais rápida. Pela API, a requisição mediana melhorou 1,35×, porque HTTP, FastAPI e Pydantic ocupam a maior parte dos 2,5 ms. Medi com dois servidores uvicorn idênticos, que só diferiam no backend, em cinco rodadas intercaladas de 300 requisições."),
    "st2_p2": ("Publishing only the 4× would have been easy. The 1.35× is the number that tells you where the next optimization has to go.",
               "Publicar só o 4× seria fácil. O 1,35× é o número que diz onde a próxima otimização precisa acontecer."),
    "st3_k": ("Observability", "Observabilidade"),
    "st3_h": ("Alerts are code, so they get tests.", "Alerta é código, então tem teste."),
    "st3_p1": ("Four Prometheus rules cover the API being down, a 5xx rate above 5%, p95 latency above 50 ms and a shift of more than 15 points in the share of any predicted class over an hour. That last one is a drift proxy that needs no ground-truth labels in production.",
               "Quatro regras do Prometheus cobrem a API fora do ar, taxa de 5xx acima de 5%, latência p95 acima de 50 ms e um desvio de mais de 15 pontos na participação de qualquer classe prevista em uma hora. Essa última é um proxy de drift que não precisa de rótulos reais em produção."),
    "st3_p2": ("Each rule has a unit test run by promtool, and each has a response in the monitoring playbook. The Grafana dashboard is provisioned as code and comes up with the stack.",
               "Cada regra tem um teste unitário rodado pelo promtool e uma resposta no playbook de monitoramento. O dashboard do Grafana é provisionado como código e sobe junto com a stack."),
    "st4_k": ("Cloud", "Nuvem"),
    "st4_h": ("Cloud Run over a cluster.", "Cloud Run em vez de um cluster."),
    "st4_p1": ("For one stateless, CPU-only API with a 1 MB model, the design picks Google Cloud Run: it runs the container as is, scales to zero when idle and avoids the networking and IAM work of a Kubernetes or ECS cluster.",
               "Para uma única API stateless, só com CPU e um modelo de 1 MB, o desenho escolhe o Google Cloud Run: ele roda o container como está, escala a zero quando ocioso e evita o trabalho de rede e IAM de um cluster Kubernetes ou ECS."),
    "st4_p2": ("The bridge is built: every push to main publishes the image to GHCR, ready for gcloud run deploy. The cloud deploy itself was an optional bonus and was not done; the graded stack runs locally with Docker Compose.",
               "A ponte já existe: cada push na main publica a imagem no GHCR, pronta para um gcloud run deploy. O deploy em nuvem em si era um bônus opcional e não foi feito; a stack avaliada roda localmente com Docker Compose."),

    "ev_prompt": ("Evidence", "Evidências"),
    "ev_h2a": ("Screenshots from", "Prints da"),
    "ev_h2b": ("the running stack.", "stack rodando."),
    "ev_lead": ("Captured from the Docker Compose stack, with the logs and outputs versioned in docs/evidence/.",
                "Capturados da stack em Docker Compose, com logs e saídas versionados em docs/evidence/."),
    "ev1_alt": ("Grafana dashboard “VITORIUM API” with request rate, latency percentiles and predictions per class",
                "Dashboard do Grafana “VITORIUM API” com taxa de requisições, percentis de latência e predições por classe"),
    "ev1_cap": ("Grafana with real traffic: 178 requests to /predict (60 urgent, 60 attention, 58 normal), zero errors.",
                "Grafana com tráfego real: 178 requisições ao /predict (60 urgente, 60 atenção, 58 normal), zero erros."),
    "ev2_alt": ("Prometheus alerts page listing the four VITORIUM alert rules, all inactive",
                "Página de alertas do Prometheus listando as quatro regras do VITORIUM, todas inativas"),
    "ev2_cap": ("The four alert rules loaded in Prometheus, inactive because there was no incident.",
                "As quatro regras de alerta carregadas no Prometheus, inativas porque não havia incidente."),

    "vid_prompt": ("Video", "Vídeo"),
    "vid_h2a": ("The stack, live,", "A stack ao vivo,"),
    "vid_h2b": ("in 4 minutes 34 seconds.", "em 4 minutos e 34 segundos."),
    "vid_lead": ("Presented with the STAR method: green CI, the API in Swagger, alerts in Prometheus, the Grafana dashboard, the Airflow DAG run and the image in GHCR.",
                 "Apresentado pelo método STAR: CI verde, a API no Swagger, os alertas no Prometheus, o dashboard do Grafana, a execução da DAG do Airflow e a imagem no GHCR."),
    "vid_play": ("Play the VITORIUM presentation video", "Assistir ao vídeo de apresentação do VITORIUM"),
    "vid_note": ("The player loads from YouTube only when you press play.", "O player só carrega do YouTube quando você aperta o play."),

    "lim_prompt": ("Limitations", "Limitações"),
    "lim_h2a": ("What this project", "O que este projeto"),
    "lim_h2b": ("is not.", "não é."),
    "lim1": ("Not clinically validated. The urgency tiers are a heuristic proxy, and the classifier must not be used for real triage.",
             "Não tem validação clínica. Os níveis de urgência são um proxy heurístico, e o classificador não deve ser usado em triagem real."),
    "lim2": ("Trained only on English abstracts. Portuguese reports, or any text unlike the corpus, fall outside its distribution, as the demo shows.",
             "Treinado só com abstracts em inglês. Laudos em português, ou qualquer texto diferente do corpus, ficam fora da distribuição, como a demo mostra."),
    "lim3": ("The “normal” class is weak (precision 0.49) and is also the fallback for unknown text, which is the worst failure mode in triage.",
             "A classe “normal” é fraca (precisão 0,49) e também é o destino de texto desconhecido, que é o pior modo de falha em triagem."),
    "lim4": ("The API has no authentication, and there is no Alertmanager: alerts show up in Prometheus but notify no one.",
             "A API não tem autenticação e não há Alertmanager: os alertas aparecem no Prometheus, mas não notificam ninguém."),
    "lim5": ("The API does not log the submitted text, but real patient data would still need a LGPD review, access control and a retention policy.",
             "A API não registra em log o texto enviado, mas dados reais de pacientes ainda exigiriam avaliação de LGPD, controle de acesso e política de retenção."),
    "cta_repo": ("Read the code →", "Ver o código →"),
    "cta_contact": ("Get in touch", "Entrar em contato"),
}

JS = {
    "labels": ({"urgente": "Urgent", "atencao": "Attention", "normal": "Normal"},
               {"urgente": "Urgente", "atencao": "Atenção", "normal": "Normal"}),
    "comma": (False, True),
    "run": ("Classify ▶", "Classificar ▶"),
    "failed": ("Model failed to load — reload the page", "O modelo não carregou — recarregue a página"),
    "none": ("no known terms", "nenhum termo conhecido"),
    "meta": ("Classified in {ms} on your device · {n} active TF-IDF features · Ctrl+Enter to rerun",
             "Classificado em {ms} no seu aparelho · {n} features TF-IDF ativas · Ctrl+Enter para rodar de novo"),
    "video_title": ("VITORIUM — STAR presentation", "VITORIUM — apresentação STAR"),
}


def render(lang):
    idx = 0 if lang == "en" else 1
    cfg = LANGS[lang]
    values = {k: v[idx] for k, v in S.items()}
    values.update({k: v for k, v in cfg.items() if k != "file"})
    values["js_i18n"] = json.dumps({k: v[idx] for k, v in JS.items()}, ensure_ascii=False)
    with io.open(TEMPLATE, encoding="utf-8") as f:
        html = f.read()

    def sub(m):
        key = m.group(1)
        if key not in values:
            raise KeyError("template key without text: " + key)
        return values[key]

    html = re.sub(r"\{\{(\w+)\}\}", sub, html)
    if "{{" in html:
        raise ValueError("unrendered placeholder left in " + cfg["file"])
    return html


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for lang, cfg in LANGS.items():
        path = os.path.join(OUT_DIR, cfg["file"])
        with io.open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(render(lang))
        print("wrote", os.path.relpath(path, REPO_DIR))


if __name__ == "__main__":
    main()
