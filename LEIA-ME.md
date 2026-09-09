# Site LM Ar Condicionado

Site institucional de página única, HTML autocontido, sem build e sem dependência externa.
Objetivo único: levar a pessoa para o WhatsApp.

No ar em https://lm-ar-condicionado.vercel.app
Repositório: https://github.com/israelino02/LM---Ar-Condicionado (a Vercel publica sozinha a cada push na `main`)

## Arquivos

- `index.html` : a página principal
- seis páginas de serviço, uma por bloco, usadas como sitelink na campanha:
  `instalacao-ar-condicionado.html`, `manutencao-ar-condicionado.html`,
  `higienizacao-ar-condicionado.html`, `recarga-de-gas-ar-condicionado.html`,
  `projeto-e-orcamento-ar-condicionado.html`, `contrato-empresas-e-condominios.html`
- `assets/estilo.css` : o estilo de todas as páginas, num arquivo só
- `gerar-paginas.py` : opcional, regera as seis páginas de serviço (ver abaixo)
- `assets/logo-300.png` : logo do cabeçalho, do rodapé e favicon
- `assets/logo.png` : logo original, usado na imagem de compartilhamento
- `assets/qrcode-google.svg` : QR code do perfil no Google, na seção de avaliações
- `assets/fotos/` : as cinco fotos dos cards de serviço
- `vercel.json` : cache de um ano nas imagens, `index.html` sempre revalidado

## As páginas de serviço

Cada card de serviço na home tem, no rodapé do card, a barra "Ver detalhes do serviço", que leva
para a página daquele serviço. Como o `vercel.json` está com `cleanUrls`, os endereços publicados
ficam sem o `.html`, e é assim que eles entram nos sitelinks da campanha:

```
/instalacao-ar-condicionado
/manutencao-ar-condicionado
/higienizacao-ar-condicionado
/recarga-de-gas-ar-condicionado
/projeto-e-orcamento-ar-condicionado
/contrato-empresas-e-condominios
```

Cada página tem cinco blocos: faixa azul com o título do serviço, os dois botões e a nota do
Google; foto ao lado de "O que está incluído" com o botão de orçamento; um quadro curto de
contexto; a faixa de confiança; e o bloco azul de área de atendimento.

O cabeçalho e o rodapé são iguais nas sete páginas, ou seja, estão repetidos nos sete arquivos.
Se mudar um item do menu, ou mude nos sete na mão, ou rode:

```
python3 gerar-paginas.py
```

O script lê o cabeçalho, a faixa de confiança e o rodapé do `index.html` e reescreve as seis
páginas de serviço com o conteúdo que está dentro dele. O site não precisa do script para
funcionar, ele é só uma conveniência de manutenção.

## Medição

O Google Tag Manager está instalado nas sete páginas, container `GTM-K4WRWJ3T`: o script no
`<head>`, logo depois da tag de viewport, e o `noscript` logo depois do `<body>`. O script
`gerar-paginas.py` já coloca as duas tags nas páginas que ele gera.

Daqui para frente, GA4, Google Ads e Clarity entram por dentro do GTM, sem precisar mexer no
código do site. O que ainda falta no código para a medição ficar completa: um `data-origem` em
cada botão de contato, para separar topo, cards, rodapé e botão flutuante, e um `dataLayer.push`
dentro da função do formulário, que hoje envia por JavaScript e por isso não dispara o gatilho
de formulário do GTM.

## Quem fala com quem

O site inteiro fala com o dono da casa. As duas únicas partes que falam com empresa são o card
"Empresas e condomínios" e a seção de contrato com o formulário. Se for escrever texto novo,
mantenha essa divisão.

## Fotos

| Onde aparece | Arquivo | Origem |
|---|---|---|
| Instalação | `servico-instalacao.jpg` | banco de imagens enviado pelo cliente |
| Manutenção e conserto | `servico-manutencao.jpg` | banco de imagens enviado pelo cliente |
| Higienização e limpeza | `servico-higienizacao.jpg` | banco de imagens enviado pelo cliente |
| Recarga de gás | `servico-gas.jpg` | banco de imagens enviado pelo cliente |
| Projeto e orçamento | `servico-projeto.jpg` | foto real da caixa de ferramentas da LM |
| Empresas e condomínios | sem foto | card azul-escuro com ícone, para destacar o serviço |

O topo não tem imagem nenhuma, é só tipografia sobre o azul-escuro.

Fotos que ainda valem a pena pedir ao cliente: serviço executado em condomínio, prédio ou empresa
(hoje o único card sem foto), equipe uniformizada em serviço, e um antes e depois de higienização.

## Avaliações e QR code

As seis avaliações são reais, copiadas do perfil da empresa no Google, na íntegra. Se for trocar
alguma, copie do perfil, sem editar o texto.

O QR code aponta para https://www.google.com/maps?cid=14544561927351388928 , que é o perfil da LM
no Google. Quem escaneia cai na página onde dá para ler as avaliações e escrever a sua.

Para gerar um QR novo, caso o link mude:

```
pip3 install segno
python3 -c "import segno; segno.make('COLE_O_LINK_AQUI', error='m').save('assets/qrcode-google.svg', scale=10, border=2, dark='#0B2439', light='#FFFFFF')"
```

Se o Leonardo quiser o link curto que abre direto a janela de avaliação, ele pega no painel do
Perfil da Empresa, em "Peça avaliações", e é só trocar nos dois lugares (o botão e o QR).

## Dados do Google que estão no site

- Nome, endereço e telefone escritos exatamente como no cadastro
- Coordenadas do JSON-LD: -22.9309573, -42.5307135, tiradas do próprio perfil
- Horário: segunda a sábado, das 8h às 18h

Se mudar qualquer um deles no Google, mude aqui também, caractere por caractere.

## Se entrar um domínio próprio

Trocar `https://lm-ar-condicionado.vercel.app` em três lugares do `index.html`: o `canonical`, as
tags `og:` e o JSON-LD.

## Regras que o site segue

- Nenhum valor, faixa de preço, promoção ou parcelamento. Todo orçamento é fechado no WhatsApp.
- Nenhuma promessa de prazo ou condição de garantia.
- Nenhum travessão no texto.
- Sobre marcas, só "trabalhamos com Gree, Midea, Hitachi e Agratto". Nunca "autorizada" nem
  "credenciada".
- Serviços que a empresa não faz não aparecem em lugar nenhum.
