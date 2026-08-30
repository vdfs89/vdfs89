#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
═══════════════════════════════════════════════════════════════════
 AGREGADOR DE CERTIFICADOS — Vitor Silva
 Consolida certificações de LinkedIn, Alura, DIO e Udemy em um
 JSON no formato esperado pelo objeto DATA do dashboard.html
═══════════════════════════════════════════════════════════════════

USO:
    pip install requests beautifulsoup4 lxml

    python agregar_certificados.py \
        --linkedin Certifications.csv \
        --alura https://cursos.alura.com.br/user/SEU_USUARIO \
        --dio https://web.dio.me/users/mkmillhouse89 \
        --udemy udemy_manual.json \
        --saida certificados.json

  Todas as fontes são OPCIONAIS — rode só com as que tiver:
    python agregar_certificados.py --dio dio_salvo.html

FONTES E ESTRATÉGIAS:
  • LinkedIn → CSV "Certifications.csv" do export oficial de dados
                (Configurações → Privacidade de dados → Obter cópia)
  • Alura    → perfil público é HTML renderizado no servidor;
               raspagem direta com requests + BeautifulSoup
  • DIO      → o site é uma SPA Next.js: requisição direta pode
               retornar 404/HTML vazio. O script tenta, nesta ordem:
                 1. Extrair o JSON embutido em __NEXT_DATA__
                 2. Raspar o HTML renderizado (se houver)
                 3. Se você passar um ARQUIVO .html local (página
                    salva com Ctrl+S no navegador), usa ele — método
                    100% confiável
  • Udemy    → sem API de certificados de aluno; mantenha um JSON
               manual simples (modelo gerado por --gerar-modelo-udemy)

SAÍDAS:
  1. certificados.json — formato completo (auditoria/backup):
     [
       {
         "nome": "...",
         "instituicao": "Alura | DIO | Udemy | ...",
         "categoria": "AI/ML | BACKEND | CLOUD | DATA | FULLSTACK | OUTROS",
         "cargaHoraria": 12,            # horas (int) ou null
         "data": "2026-05-28",          # ISO ou null
         "urlCertificado": "https://..."  # ou null
       }, ...
     ]
  2. dashboard_data.json — formato EXATO do objeto DATA do
     dashboard.html: chaves "cursos" (cole em DATA.cursos) e
     "horasPorArea" (cole em DATA.horasPorArea).

NOTA ÉTICA/LEGAL: raspe apenas SEUS PRÓPRIOS perfis públicos,
com intervalo entre requisições. Não use para dados de terceiros.
"""

import argparse
import csv
import json
import re
import sys
import unicodedata
from datetime import datetime
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("Instale as dependências:  pip install requests beautifulsoup4 lxml")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/125.0 Safari/537.36"
    ),
    "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8",
}

# ──────────────────────────────────────────────────────────────────
# Utilidades
# ──────────────────────────────────────────────────────────────────

def normalizar(txt: str) -> str:
    """minúsculas, sem acentos — para matching de categoria."""
    txt = unicodedata.normalize("NFD", txt or "")
    return "".join(c for c in txt if unicodedata.category(c) != "Mn").lower()


# Palavras-chave → categoria do dashboard (ordem importa: 1º match vence)
CATEGORIAS = [
    ("SOFT SKILLS", ["lideranca", "coaching", "emocional", "produtividade", "pnl",
                     "timidez", "negocie", "vendas", "gamificacao",
                     "desenvolvimento pessoal", "positividade", "storytelling",
                     "gerencia", "colaboradores", "carreira", "alto potencial",
                     "ingles", "fortemente", "inclusiv"]),
    ("AI/ML",     ["inteligencia artificial", " ia ", " ia:", " ias",
                   "machine learning", "deep learning", "llm", "langchain",
                   "langgraph", "rag", "prompt", "copilot", "chatgpt", "gemini",
                   "claude", "rede neural", "nlp", "linguagem natural", "genai",
                   "generativ", "bedrock", "agentes", "agents",
                   "visao computacional", "notebooklm", "whisper", "xai",
                   "aprendizado de maquina", "low-code", "modelos de linguagem"]),
    ("DATA",      ["dados", "data ", "neo4j", "grafos", "graph", "power bi",
                   "power query", "analytics", "sql", "etl", "pandas", "excel",
                   "estatistica", "business intelligence", "banco de dados",
                   "spark", "databricks", "visualizacao"]),
    ("CLOUD",     ["aws", "azure", "gcp", "google cloud", "cloud", "docker",
                   "kubernetes", "devops", "terraform", "serverless"]),
    ("BACKEND",   ["python", "java", "node", "api", "fastapi", "rust", "spring",
                   "backend", "c#", ".net", "golang", "php", "git", "github",
                   "versionamento", "programacao", "codigo", "logica",
                   "computacional", "operadores", "estruturas"]),
    ("FULLSTACK", ["react", "javascript", "typescript", "front", "html", "css",
                   "flutter", "mobile", "angular", "vue", "fullstack", "web"]),
    ("DEV",       ["bootcamp", "santander", "portfolio", "desafio"]),
]

# Categoria interna → id de filtro usado em DATA.cursos[].cat no dashboard
CAT_PARA_DASHBOARD = {
    "AI/ML": "ai",
    "BACKEND": "backend",
    "CLOUD": "cloud",
    "DATA": "data",
    "FULLSTACK": "fullstack",
    "SOFT SKILLS": "soft",
    "DEV": "dev",
    "OUTROS": "outros",
}


def classificar(nome_curso: str) -> str:
    alvo = f" {normalizar(nome_curso)} "
    for categoria, chaves in CATEGORIAS:
        if any(chave in alvo for chave in chaves):
            return categoria
    return "OUTROS"


def parse_data(txt: str):
    """Tenta converter datas em formatos comuns BR/EN → ISO. None se falhar."""
    if not txt:
        return None
    txt = txt.strip()
    formatos = ["%d/%m/%Y", "%d/%m/%y", "%Y-%m-%d", "%b %Y", "%B %Y",
                "%m/%Y", "%d %b %Y", "%d de %B de %Y"]
    meses_pt = {"janeiro": "January", "fevereiro": "February", "março": "March",
                "abril": "April", "maio": "May", "junho": "June", "julho": "July",
                "agosto": "August", "setembro": "September", "outubro": "October",
                "novembro": "November", "dezembro": "December"}
    txt_en = txt.lower()
    for pt, en in meses_pt.items():
        txt_en = txt_en.replace(pt, en)
    for fmt in formatos:
        for candidato in (txt, txt_en):
            try:
                return datetime.strptime(candidato, fmt).date().isoformat()
            except ValueError:
                continue
    return None


def extrair_horas(txt: str):
    """'12h', '12 horas', '12hrs' → 12 (int). None se não achar."""
    m = re.search(r"(\d+)\s*h", normalizar(txt or ""))
    return int(m.group(1)) if m else None


def cert(nome, instituicao, carga=None, data=None, url=None) -> dict:
    return {
        "nome": (nome or "").strip(),
        "instituicao": instituicao,
        "categoria": classificar(nome or ""),
        "cargaHoraria": carga,
        "data": data,
        "urlCertificado": url,
    }


def obter_html(fonte: str) -> str:
    """Aceita URL (http...) ou caminho de arquivo .html local."""
    if fonte.lower().startswith("http"):
        resp = requests.get(fonte, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        return resp.text
    caminho = Path(fonte)
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {fonte}")
    return caminho.read_text(encoding="utf-8", errors="ignore")


# ──────────────────────────────────────────────────────────────────
# 1) LINKEDIN — CSV do export oficial
# ──────────────────────────────────────────────────────────────────

def puxar_linkedin(caminho_csv: str) -> list:
    """
    Lê o Certifications.csv do export do LinkedIn.
    Colunas típicas: Name, Url, Authority, Started On, Finished On, License Number
    (os nomes podem variar levemente conforme o idioma da conta)
    """
    certs = []
    with open(caminho_csv, newline="", encoding="utf-8-sig") as f:
        for linha in csv.DictReader(f):
            # tolera variação de nomes de coluna PT/EN; coluna presente
            # porém vazia NÃO bloqueia o fallback para a próxima opção
            def col(*opcoes):
                for o in opcoes:
                    for k, v in linha.items():
                        if normalizar(k) == normalizar(o) and (v or "").strip():
                            return v.strip()
                return ""

            nome = col("Name", "Nome")
            if not nome:
                continue
            certs.append(cert(
                nome=nome,
                instituicao=col("Authority", "Autoridade", "Emissor") or "LinkedIn",
                data=parse_data(col("Started On", "Finished On",
                                    "Data de início", "Data de conclusão")),
                url=col("Url", "URL") or None,
            ))
    print(f"  [linkedin] {len(certs)} certificações lidas do CSV")
    return certs


# ──────────────────────────────────────────────────────────────────
# 2) ALURA — perfil público (HTML server-side)
# ──────────────────────────────────────────────────────────────────

def raspar_alura(fonte: str) -> list:
    """
    Perfil público: https://cursos.alura.com.br/user/SEU_USUARIO
    Estrutura típica: lista de cursos concluídos com nome + carga horária.
    Os seletores abaixo cobrem o layout atual e variações conhecidas;
    se a Alura mudar o HTML, salve a página (Ctrl+S) e passe o .html.
    """
    html = obter_html(fonte)
    sopa = BeautifulSoup(html, "lxml")
    certs = []

    # Layout atual: <li class="course-card ..."> com nome e horas
    cartoes = sopa.select(
        "li.course-card, .course-card, li[class*='curso'], "
        ".profile-courses li, ul.courses li"
    )
    for c in cartoes:
        nome_el = c.select_one(
            ".course-card__name, .course-card-name, h3, h4, [class*='name']"
        )
        nome = nome_el.get_text(strip=True) if nome_el else None
        if not nome:
            continue
        horas = extrair_horas(c.get_text(" ", strip=True))
        link_el = c.select_one("a[href*='certificate'], a[href*='certificado']")
        url = link_el["href"] if link_el and link_el.has_attr("href") else None
        if url and url.startswith("/"):
            url = "https://cursos.alura.com.br" + url
        certs.append(cert(nome, "Alura", carga=horas, url=url))

    # Fallback genérico: âncoras de certificado soltas na página
    if not certs:
        for a in sopa.select("a[href*='/certificate/'], a[href*='certificado']"):
            nome = a.get_text(strip=True)
            if nome:
                url = a["href"]
                if url.startswith("/"):
                    url = "https://cursos.alura.com.br" + url
                certs.append(cert(nome, "Alura", url=url))

    print(f"  [alura] {len(certs)} cursos/certificados extraídos")
    if not certs:
        print("  [alura] ⚠ nada encontrado — o perfil é público? "
              "Tente salvar a página logado (Ctrl+S) e passar o arquivo .html")
    return certs


# ──────────────────────────────────────────────────────────────────
# 3) DIO — SPA Next.js (estratégia em camadas)
# ──────────────────────────────────────────────────────────────────

def raspar_dio(fonte: str) -> list:
    """
    A DIO renderiza o perfil via JavaScript, então a requisição direta
    pode vir vazia ou 404. Estratégia:
      1. Procurar o JSON embutido <script id="__NEXT_DATA__"> e navegar
         nele atrás de cursos/certificados (chaves variam entre versões).
      2. Raspar âncoras /certificate/XXXX/share se o HTML tiver vindo.
      3. Se tudo falhar → instruir a salvar a página logado (Ctrl+S)
         e passar o .html local (caminho que sempre funciona).
    """
    try:
        html = obter_html(fonte)
    except Exception as e:
        print(f"  [dio] ⚠ falha ao acessar ({e}).")
        print("  [dio] → Abra seu perfil no navegador, salve com Ctrl+S e rode:")
        print("          python agregar_certificados.py --dio pagina_dio.html")
        return []

    sopa = BeautifulSoup(html, "lxml")
    certs = []

    # 1) __NEXT_DATA__ (ouro: dados estruturados)
    tag = sopa.find("script", id="__NEXT_DATA__")
    if tag and tag.string:
        try:
            dados = json.loads(tag.string)
            certs.extend(_dio_varrer_json(dados))
        except json.JSONDecodeError:
            pass

    # 2) HTML renderizado: links públicos de certificado
    if not certs:
        for a in sopa.select("a[href*='/certificate/']"):
            nome = a.get_text(strip=True) or "Certificado DIO"
            url = a["href"]
            if url.startswith("/"):
                url = "https://www.dio.me" + url
            certs.append(cert(nome, "DIO", url=url))

    print(f"  [dio] {len(certs)} certificados extraídos")
    if not certs:
        print("  [dio] ⚠ nada encontrado (SPA sem render no servidor).")
        print("  [dio] → Método garantido: perfil aberto e logado no navegador,")
        print("          Ctrl+S (salvar como 'Página completa'), depois:")
        print("          python agregar_certificados.py --dio pagina_dio.html")
    return certs


def _dio_varrer_json(obj, encontrados=None) -> list:
    """
    Varre recursivamente o __NEXT_DATA__ procurando objetos que pareçam
    cursos/certificados (têm 'name'/'title' + alguma pista de certificado).
    Robusto a mudanças de schema da DIO.
    """
    if encontrados is None:
        encontrados = []
    if isinstance(obj, dict):
        chaves = {normalizar(k) for k in obj.keys()}
        tem_nome = chaves & {"name", "title", "nome", "courename", "coursename"}
        tem_pista = chaves & {"certificate", "certificateurl", "certificateid",
                              "slug", "workload", "finishedat", "completedat"}
        if tem_nome and tem_pista:
            nome = obj.get("name") or obj.get("title") or obj.get("courseName")
            url = (obj.get("certificateUrl") or obj.get("certificate") or None)
            if isinstance(url, dict):
                url = url.get("url") or url.get("shareUrl")
            cid = obj.get("certificateId") or obj.get("id")
            if not url and cid:
                url = f"https://www.dio.me/certificate/{cid}/share"
            horas = obj.get("workload")
            if isinstance(horas, str):
                horas = extrair_horas(horas)
            data = parse_data(str(obj.get("finishedAt") or
                                  obj.get("completedAt") or "")[:10])
            if nome:
                encontrados.append(cert(str(nome), "DIO",
                                        carga=horas, data=data, url=url))
        for v in obj.values():
            _dio_varrer_json(v, encontrados)
    elif isinstance(obj, list):
        for item in obj:
            _dio_varrer_json(item, encontrados)
    return encontrados


# ──────────────────────────────────────────────────────────────────
# 4) UDEMY — lista manual em JSON
# ──────────────────────────────────────────────────────────────────

MODELO_UDEMY = [
    {"nome": "Ultimate AWS Certified AI Practitioner AIF-C01",
     "cargaHoraria": 14, "data": "2026-05-01",
     "urlCertificado": "https://ude.my/UC-XXXXXXXX"},
    {"nome": "[PREENCHER nome do curso]",
     "cargaHoraria": None, "data": None,
     "urlCertificado": "https://ude.my/UC-XXXXXXXX"},
]


def puxar_udemy(caminho_json: str) -> list:
    itens = json.loads(Path(caminho_json).read_text(encoding="utf-8"))
    certs = [cert(i.get("nome"), "Udemy",
                  carga=i.get("cargaHoraria"),
                  data=i.get("data"),
                  url=i.get("urlCertificado"))
             for i in itens if i.get("nome") and "[PREENCHER" not in i["nome"]]
    print(f"  [udemy] {len(certs)} certificados lidos do JSON manual")
    return certs


# ──────────────────────────────────────────────────────────────────
# Consolidação
# ──────────────────────────────────────────────────────────────────

def deduplicar(certs: list) -> list:
    """Remove duplicatas por nome normalizado (LinkedIn costuma repetir
    cursos que também vêm da fonte original). Mantém o registro mais
    completo (mais campos preenchidos)."""
    melhores = {}
    for c in certs:
        chave = normalizar(c["nome"])
        score = sum(1 for v in c.values() if v)
        if chave not in melhores or score > melhores[chave][0]:
            melhores[chave] = (score, c)
    return [c for _, c in melhores.values()]


def exportar_dashboard(certs: list, caminho: str) -> dict:
    """
    Converte para o formato EXATO do dashboard.html:
      DATA.cursos       → { nome, inst, horas: "12h", data, cat: "ai" }
      DATA.horasPorArea → [ { area: "AI/ML", horas: 120 }, ... ]
    """
    cursos = [{
        "nome": c["nome"],
        "inst": c["instituicao"],
        "horas": f"{c['cargaHoraria']}h" if c["cargaHoraria"] else "—",
        "data": c["data"] or "—",
        "cat": CAT_PARA_DASHBOARD.get(c["categoria"], "outros"),
    } for c in certs]

    horas_area = {}
    for c in certs:
        horas_area[c["categoria"]] = horas_area.get(c["categoria"], 0) + (c["cargaHoraria"] or 0)
    horas_por_area = [{"area": a, "horas": h}
                      for a, h in sorted(horas_area.items(), key=lambda x: -x[1])
                      if h > 0]

    dados = {"cursos": cursos, "horasPorArea": horas_por_area}
    Path(caminho).write_text(
        json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")
    return dados


def main():
    p = argparse.ArgumentParser(description="Agrega certificados em JSON para o dashboard")
    p.add_argument("--linkedin", help="Caminho do Certifications.csv do export do LinkedIn")
    p.add_argument("--alura", help="URL do perfil público da Alura OU arquivo .html salvo")
    p.add_argument("--dio", help="URL do perfil DIO OU arquivo .html salvo (recomendado)")
    p.add_argument("--udemy", help="Caminho do JSON manual da Udemy")
    p.add_argument("--saida", default="certificados.json", help="Arquivo JSON de saída")
    p.add_argument("--saida-dashboard", default="dashboard_data.json",
                   help="JSON no formato do objeto DATA do dashboard.html")
    p.add_argument("--gerar-modelo-udemy", action="store_true",
                   help="Gera udemy_manual.json de exemplo e sai")
    args = p.parse_args()

    if args.gerar_modelo_udemy:
        Path("udemy_manual.json").write_text(
            json.dumps(MODELO_UDEMY, ensure_ascii=False, indent=2), encoding="utf-8")
        print("Modelo gravado em udemy_manual.json — edite e rode com --udemy")
        return

    if not any([args.linkedin, args.alura, args.dio, args.udemy]):
        p.error("informe ao menos uma fonte (--linkedin / --alura / --dio / --udemy)")

    print("Coletando certificados…")
    todos = []
    if args.linkedin:
        todos += puxar_linkedin(args.linkedin)
    if args.alura:
        todos += raspar_alura(args.alura)
    if args.dio:
        todos += raspar_dio(args.dio)
    if args.udemy:
        todos += puxar_udemy(args.udemy)

    finais = deduplicar(todos)
    finais.sort(key=lambda c: (c["data"] or "0000"), reverse=True)

    Path(args.saida).write_text(
        json.dumps(finais, ensure_ascii=False, indent=2), encoding="utf-8")

    dados_dash = exportar_dashboard(finais, args.saida_dashboard)

    # Resumo por categoria — útil pro gráfico de barras do dashboard
    print(f"\n✔ {len(finais)} certificados únicos → {args.saida}")
    print(f"✔ formato do dashboard (cursos + horasPorArea) → {args.saida_dashboard}")
    resumo = {}
    for c in finais:
        resumo.setdefault(c["categoria"], [0, 0])
        resumo[c["categoria"]][0] += 1
        resumo[c["categoria"]][1] += c["cargaHoraria"] or 0
    for cat, (qtd, horas) in sorted(resumo.items(), key=lambda x: -x[1][1]):
        print(f"   {cat:<10} {qtd:>3} certificados  {horas:>4}h")
    print("\nNo dashboard.html: cole o array 'cursos' em DATA.cursos e o "
          "'horasPorArea' em DATA.horasPorArea")


if __name__ == "__main__":
    main()
