# -*- coding: utf-8 -*-
"""Gera uma página por serviço, reaproveitando cabeçalho, faixa de confiança e rodapé do index."""
import io, re, os

BASE = "/Users/israellino/Documents/1 - IL MKT/CLIENTES/LEONARDO - LM/SITE"
idx = io.open(os.path.join(BASE, "index.html"), encoding="utf-8").read()

def pedaco(ini, fim):
    a = idx.index(ini); b = idx.index(fim, a) + len(fim)
    trecho = idx[a:b]
    assert len(trecho) > 50, "pedaco vazio: " + ini
    return trecho

SPRITE  = pedaco('<svg width="0" height="0" style="position:absolute"', '</svg>\n')
HEADER  = pedaco('<header class="header">', '</header>')
TRUST   = pedaco('<section class="trust"', '</section>')
FOOTER  = pedaco('<footer class="footer">', '</footer>')
FLOAT   = pedaco('<a class="float-wa"', '</a>')
SCRIPT  = pedaco('<script>\n(function(){', '})();\n</script>')
ESTRELAS = '\n          '.join(['<svg aria-hidden="true"><use href="#ico-estrela"></use></svg>']*5)

# nas páginas internas as âncoras do menu apontam para a home
def para_home(html):
    return re.sub(r'href="#(?!conteudo)([a-z-]+)"', r'href="index.html#\1"', html)

HEADER, FOOTER, FLOAT = para_home(HEADER), para_home(FOOTER), para_home(FLOAT)
SCRIPT = SCRIPT.replace("  var form = document.getElementById('formEmpresa');", "  var form = null;")
SCRIPT = re.sub(r"\n  var form = null;.*?\n  \}\);", "", SCRIPT, flags=re.S)

GTM_HEAD = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-K4WRWJ3T');</script>
<!-- End Google Tag Manager -->"""

GTM_BODY = """<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-K4WRWJ3T"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->"""

ICONE_WA = '<svg viewBox="0 0 32 32" width="19" height="19" fill="#fff" aria-hidden="true"><path d="M16 3C8.8 3 3 8.8 3 16c0 2.3.6 4.5 1.8 6.4L3 29l6.8-1.8c1.9 1 4 1.6 6.2 1.6 7.2 0 13-5.8 13-13S23.2 3 16 3zm0 23.6c-2 0-3.9-.5-5.5-1.5l-.4-.2-4 1.1 1.1-3.9-.3-.4a10.5 10.5 0 1 1 9.1 4.9zm5.9-7.9c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2s-.8 1-1 1.2c-.2.2-.4.2-.7.1a8.6 8.6 0 0 1-4.3-3.7c-.3-.6.3-.5.9-1.7.1-.2 0-.4 0-.6s-.7-1.7-1-2.3c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.4-1.2 1.2-1.2 2.8s1.2 3.2 1.4 3.5c.2.2 2.4 3.7 5.9 5.1 2.2.9 3 1 4.1.8.7-.1 2-.8 2.2-1.6.3-.8.3-1.5.2-1.6-.1-.2-.3-.3-.6-.4z"/></svg>'
ICONE_TEL = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="#fff" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>'
ICONE_FORM = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 3.5h6v3H9zM15 5h3.5v15.5h-13V5H9"/><path d="M9 11.5h6M9 15.5h4"/></svg>'
SETA = '<svg viewBox="0 0 24 24" aria-hidden="true" stroke-linecap="round" stroke-linejoin="round"><path d="M15 6l-6 6 6 6"/></svg>'

SERVICOS = [
{
 "arq": "instalacao-ar-condicionado",
 "titulo": "Instalação de Ar-Condicionado em Saquarema e Araruama | LM Ar Condicionado",
 "desc": "Instalação de ar-condicionado split, inverter, piso-teto e multi-split em Saquarema, Araruama e municípios vizinhos. Equipe própria. Orçamento pelo WhatsApp.",
 "h1": "Instalação de ar-condicionado em Saquarema e Araruama",
 "sub": "Split de parede, inverter, piso-teto, cassete e multi-split, instalados pela nossa equipe. Manda uma foto do cômodo no WhatsApp que a gente passa o orçamento.",
 "foto": "servico-instalacao.jpg", "alt": "Técnico instalando a evaporadora de um ar-condicionado split na parede",
 "inclui": ["Dreno com o caimento certo, para não pingar na parede",
            "Vácuo antes de liberar o gás",
            "Tubulação embutida na obra, antes do acabamento",
            "Aparelho novo, se você ainda não comprou",
            "Aparelho ligado e testado na sua frente"],
 "quando_t": "Antes de comprar o aparelho",
 "quando": "Vale conferir quantos BTUs o cômodo precisa antes da compra. Aparelho pequeno demais não gela, grande demais gasta à toa. A gente faz esse cálculo pela foto no WhatsApp ou em visita técnica.",
 "msg": "Ol%C3%A1!%20Quero%20um%20or%C3%A7amento%20de%20instala%C3%A7%C3%A3o%20de%20ar-condicionado.",
},
{
 "arq": "manutencao-ar-condicionado",
 "titulo": "Manutenção e Conserto de Ar-Condicionado em Saquarema e Araruama | LM Ar Condicionado",
 "desc": "Conserto de ar-condicionado que não gela, pinga água, faz barulho ou desliga sozinho, em Saquarema, Araruama e municípios vizinhos. Orçamento pelo WhatsApp.",
 "h1": "Manutenção e conserto de ar-condicionado em Saquarema e Araruama",
 "sub": "Parou de gelar, pinga na parede, faz barulho ou desliga sozinho? A gente abre, testa e mostra o que está acontecendo antes de consertar.",
 "foto": "servico-manutencao.jpg", "alt": "Técnico medindo a parte elétrica de uma condensadora de ar-condicionado durante a manutenção",
 "inclui": ["Diagnóstico com o aparelho aberto, na sua frente",
            "Troca de placa eletrônica, compressor, capacitor e controle",
            "Manutenção preventiva programada",
            "Revisão antes do verão, para não parar no calor",
            "Aparelho testado antes da equipe sair"],
 "quando_t": "Quando chamar",
 "quando": "Se o aparelho parou de gelar, se está pingando água dentro de casa, se começou a fazer barulho diferente ou se desliga sozinho depois de alguns minutos. Quanto antes olhar, menor costuma ser o serviço.",
 "msg": "Ol%C3%A1!%20Quero%20um%20or%C3%A7amento%20de%20manuten%C3%A7%C3%A3o%20de%20ar-condicionado.",
},
{
 "arq": "higienizacao-ar-condicionado",
 "titulo": "Higienização e Limpeza de Ar-Condicionado em Saquarema e Araruama | LM Ar Condicionado",
 "desc": "Higienização de ar-condicionado com desmontagem da evaporadora e bactericida, em Saquarema, Araruama e municípios vizinhos. Orçamento pelo WhatsApp.",
 "h1": "Higienização e limpeza de ar-condicionado em Saquarema e Araruama",
 "sub": "Aquele cheiro que sai quando liga é sujeira acumulada lá dentro. A limpeza é completa, com desmontagem da evaporadora, não é só trocar o filtro.",
 "foto": "servico-higienizacao.jpg", "alt": "Técnico higienizando a evaporadora de um ar-condicionado split com lavadora e capa de proteção",
 "inclui": ["Limpeza completa com desmontagem da evaporadora",
            "Limpeza da condensadora, a parte que fica do lado de fora",
            "Aplicação de bactericida"],
 "quando_t": "Quando chamar",
 "quando": "Varia com o uso e com o ambiente: aparelho ligado muitas horas por dia, casa perto da praia ou de rua de terra e cozinha sujam bem mais rápido. Se está saindo cheiro, se o ar saiu fraco ou se começou a pingar, é hora de higienizar.",
 "msg": "Ol%C3%A1!%20Quero%20um%20or%C3%A7amento%20de%20higieniza%C3%A7%C3%A3o%20de%20ar-condicionado.",
},
{
 "arq": "recarga-de-gas-ar-condicionado",
 "titulo": "Recarga de Gás de Ar-Condicionado em Saquarema e Araruama | LM Ar Condicionado",
 "desc": "Carga e recarga de gás, reparo de vazamento e conversão de R22 para R410A em Saquarema, Araruama e municípios vizinhos. Orçamento pelo WhatsApp.",
 "h1": "Recarga de gás de ar-condicionado em Saquarema e Araruama",
 "sub": "Está limpo e mesmo assim gela pouco? Pode ser falta de gás. Antes de completar, a gente acha o vazamento, senão o gás vai embora de novo.",
 "foto": "servico-gas.jpg", "alt": "Manifold de manômetros conectado à condensadora para carga de gás do ar-condicionado",
 "inclui": ["Carga e recarga de gás",
            "Localização e reparo de vazamento",
            "Teste de estanqueidade e vácuo",
            "Conversão de R22 para R410A"],
 "quando_t": "Por que achar o vazamento primeiro",
 "quando": "Sistema de ar-condicionado é fechado. Se o gás acabou, ele vazou em algum ponto. Completar sem achar o vazamento resolve por pouco tempo e você paga a carga de novo mais para frente.",
 "msg": "Ol%C3%A1!%20Quero%20um%20or%C3%A7amento%20de%20carga%20de%20g%C3%A1s%20do%20ar-condicionado.",
},
{
 "arq": "projeto-e-orcamento-ar-condicionado",
 "titulo": "Cálculo de BTUs e Orçamento de Ar-Condicionado em Saquarema e Araruama | LM Ar Condicionado",
 "desc": "Cálculo de BTUs, visita técnica e projeto de climatização para obra em Saquarema, Araruama e municípios vizinhos. Orçamento por foto no WhatsApp.",
 "h1": "Cálculo de BTUs e orçamento de ar-condicionado em Saquarema e Araruama",
 "sub": "Antes de comprar, saiba quantos BTUs o seu cômodo precisa. Aparelho pequeno demais não gela, grande demais gasta à toa.",
 "foto": "servico-projeto.jpg", "alt": "Ferramentas da LM Ar Condicionado prontas para a visita técnica, com manifold, flangeador e parafusadeira",
 "inclui": ["Cálculo de BTUs pelo tamanho do cômodo e pelo sol que bate",
            "Orçamento por foto no WhatsApp",
            "Visita técnica quando precisa olhar de perto",
            "Projeto de climatização para obra"],
 "quando_t": "Como funciona o orçamento por foto",
 "quando": "Manda pelo WhatsApp uma foto do cômodo, do ponto onde o aparelho vai ficar e, se já tiver um instalado, do aparelho. Com isso a gente já consegue avaliar a maior parte dos casos e passar o orçamento.",
 "msg": "Ol%C3%A1!%20Quero%20uma%20visita%20t%C3%A9cnica%20para%20or%C3%A7amento%20de%20ar-condicionado.",
},
{
 "arq": "contrato-empresas-e-condominios",
 "titulo": "Contrato de Manutenção de Ar-Condicionado para Empresas e Condomínios | LM Ar Condicionado",
 "desc": "Contrato de manutenção mensal, PMOC e atendimento de urgência para condomínio, prédio, loja, clínica e restaurante em Saquarema e Araruama.",
 "h1": "Contrato de manutenção de ar-condicionado para empresas e condomínios",
 "sub": "Condomínio residencial, prédio de apartamentos, prédio empresarial, loja, clínica, escritório e restaurante: a gente assume o ar-condicionado do lugar em contrato mensal.",
 "foto": None, "alt": None,
 "inclui": ["Contrato de manutenção mensal, com visita programada",
            "PMOC",
            "Atendimento de urgência para cliente com contrato",
            "Ar central e VRF",
            "Um time só para instalação e manutenção"],
 "quando_t": "Como a proposta é montada",
 "quando": "A gente marca uma visita, levanta quantos aparelhos existem e em que estado eles estão, e monta a proposta em cima disso. Cada prédio tem uma realidade diferente.",
 "msg": "Ol%C3%A1!%20Quero%20falar%20sobre%20contrato%20de%20manuten%C3%A7%C3%A3o%20para%20minha%20empresa.",
 "cta_box": ("index.html#empresas", "Pedir orçamento", "form"),
},
]

MODELO = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

{gtm_head}

<title>{titulo}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#071A2B">
<link rel="canonical" href="https://lm-ar-condicionado.vercel.app/{arq}">
<link rel="icon" href="assets/logo-300.png" type="image/png">
<link rel="apple-touch-icon" href="assets/logo-300.png">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="LM Ar Condicionado">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://lm-ar-condicionado.vercel.app/assets/logo.png">
<link rel="stylesheet" href="assets/estilo.css">
</head>
<body>
{gtm_body}

<a class="sr-only" href="#conteudo">Ir para o conteúdo</a>

{sprite}
{header}

<main id="conteudo">

<section class="page-hero">
  <div class="wrap">
    <a class="voltar" href="index.html#servicos">{seta} Todos os serviços</a>
    <h1>{h1}</h1>
    <p class="hero-sub">{sub}</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="https://wa.me/5522999297477?text={msg}" target="_blank" rel="noopener">{ico_wa} Chamar no WhatsApp</a>
      <a class="btn btn-light" href="tel:+5522999297477">{ico_tel} Ligar: (22) 99929-7477</a>
    </div>
    <div class="rating">
      <span class="rating-score">5,0</span>
      <span class="stars" aria-hidden="true">
          {estrelas}
      </span>
      <span class="rating-text"><strong>161 avaliações</strong><br>nota 5,0 no Google</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap page-grid">
    {coluna_foto}
    <div>
      <div class="page-box">
        <h2>O que está incluído</h2>
        <ul class="list">
{itens}
        </ul>
        {cta_box}
      </div>
      <div class="page-box">
        <h2>{quando_t}</h2>
        <p style="margin:0;font-size:.92rem">{quando}</p>
      </div>
    </div>
  </div>
</section>

{trust}

<section class="section section--navy">
  <div class="wrap">
    <p class="eyebrow">Onde atendemos</p>
    <h2>Saquarema, Araruama e municípios vizinhos da Região dos Lagos</h2>
    <p>A base fica no Boqueirão, em Saquarema. Atendemos de segunda a sábado, das 8h às 18h. Ficou na dúvida se atendemos o seu endereço? Chama no WhatsApp que a gente confirma.</p>
    <a class="btn btn-primary" href="https://wa.me/5522999297477?text={msg}" target="_blank" rel="noopener">{ico_wa} Chamar no WhatsApp</a>
  </div>
</section>

</main>

{footer}
{float}
{script}
</body>
</html>
'''

for sv in SERVICOS:
    if sv["foto"]:
        coluna = '<figure class="page-foto"><img src="assets/fotos/{f}" width="900" height="600" alt="{a}" fetchpriority="high"></figure>'.format(f=sv["foto"], a=sv["alt"])
    else:
        coluna = '''<div class="page-box" style="background:var(--navy-800);color:#C2D5E6;border-color:var(--navy-800)">
        <h2 style="color:#fff">Fale com o time comercial</h2>
        <p style="font-size:.92rem;color:#B7CDE0">Preencha o formulário na página inicial com o nome, o condomínio ou a empresa, o telefone e o tipo de imóvel, que o WhatsApp abre com tudo escrito.</p>
        <a class="btn btn-light btn-block" href="index.html#empresas">Abrir o formulário</a>
      </div>'''
    if sv.get("cta_box"):
        href, rotulo, _ = sv["cta_box"]
        cta_box = '<a class="btn btn-primary btn-block" href="{h}">{i} {r}</a>'.format(h=href, i=ICONE_FORM, r=rotulo)
    else:
        cta_box = '<a class="btn btn-primary btn-block" href="https://wa.me/5522999297477?text={m}" target="_blank" rel="noopener">{i} Pedir orçamento</a>'.format(m=sv["msg"], i=ICONE_WA)
    itens = "\n".join('          <li>{}</li>'.format(i) for i in sv["inclui"])
    html = MODELO.format(titulo=sv["titulo"], desc=sv["desc"], arq=sv["arq"], h1=sv["h1"], sub=sv["sub"],
                         msg=sv["msg"], itens=itens, quando_t=sv["quando_t"], quando=sv["quando"],
                         coluna_foto=coluna, cta_box=cta_box, sprite=SPRITE, header=HEADER, trust=TRUST, footer=FOOTER,
                         float=FLOAT, script=SCRIPT, gtm_head=GTM_HEAD, gtm_body=GTM_BODY, estrelas=ESTRELAS, ico_wa=ICONE_WA, ico_tel=ICONE_TEL, seta=SETA)
    caminho = os.path.join(BASE, sv["arq"] + ".html")
    io.open(caminho, "w", encoding="utf-8").write(html)
    print("gerada:", sv["arq"] + ".html", len(html), "bytes")
