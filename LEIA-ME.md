# Site LM Ar Condicionado

Site institucional de página única, HTML autocontido. Objetivo único: levar a pessoa para o WhatsApp.
O único formulário do site é o de proposta de contrato, na seção de condomínios e empresas, e ele
não envia nada para servidor nenhum: monta a mensagem e abre o WhatsApp já preenchido.

## Arquivos

- `index.html` : o site inteiro (HTML, CSS e JS no mesmo arquivo, sem dependência externa)
- `assets/logo-300.png` : logo do cabeçalho, do rodapé e favicon
- `assets/logo.png` : logo original, usado na imagem de compartilhamento (Open Graph)
- `assets/fotos/` : as fotos usadas no site

## De onde veio cada foto

| Onde aparece | Arquivo | Origem |
|---|---|---|
| Topo, foto principal | `hero-carro-lm.jpg` | foto real do carro da LM em Saquarema |
| Topo, foto menor | `hero-equipe-lm.jpg` | foto real do técnico com aparelhos novos |
| Instalação | `servico-instalacao.jpg` | banco de imagens enviado pelo cliente |
| Manutenção e conserto | `servico-manutencao.jpg` | banco de imagens enviado pelo cliente |
| Higienização e limpeza | `servico-higienizacao.jpg` | banco de imagens enviado pelo cliente |
| Recarga de gás | `servico-gas.jpg` | banco de imagens enviado pelo cliente |
| Projeto e orçamento | `servico-projeto.jpg` | foto real da caixa de ferramentas da LM |
| Empresas e condomínios | sem foto | card azul-escuro com ícone, para destacar o serviço |

Para trocar qualquer uma, salve a nova em `assets/fotos/` com o mesmo nome. Use JPG de no máximo
1000px no maior lado, para o site continuar leve no 4G. Se a foto for vertical, ajuste o
`object-position` daquela imagem no HTML para escolher a parte que aparece no recorte.

## Fotos que ainda valem a pena pedir ao cliente

1. Serviço executado em condomínio, prédio ou empresa. É o card de maior valor e hoje é o único
   sem foto, está com um card azul-escuro no lugar.
2. Equipe uniformizada em serviço, de frente, para o topo do site.
3. Antes e depois de uma higienização.

## Antes de publicar, confirmar com o cliente

1. **Domínio**: o `<link rel="canonical">`, as tags Open Graph e o JSON-LD estão com
   `https://www.lmarcondicionado.com.br/` como exemplo. Troque pelo domínio real.
2. **Coordenadas do mapa**: o JSON-LD usa latitude e longitude aproximadas de Saquarema. Pegue as
   exatas no Perfil da Empresa no Google e substitua.
3. **Nome, endereço e telefone** estão escritos exatamente como no cadastro do Google. Se mudar lá,
   mude aqui também, caractere por caractere.

## Regras que o site segue

- Nenhum valor, faixa de preço, promoção ou parcelamento. Todo orçamento é fechado no WhatsApp.
- Nenhuma promessa de prazo ou condição de garantia.
- Nenhum travessão no texto.
- Sobre marcas, só "trabalhamos com Gree, Midea, Hitachi e Agratto". Nunca "autorizada" nem
  "credenciada".
- Serviços que a empresa não faz não aparecem em lugar nenhum.

## Como publicar

É um site estático. Suba a pasta inteira (`index.html` mais `assets`) em qualquer hospedagem, ou
arraste a pasta para Netlify, Vercel ou Cloudflare Pages. Não precisa de banco de dados nem servidor.
