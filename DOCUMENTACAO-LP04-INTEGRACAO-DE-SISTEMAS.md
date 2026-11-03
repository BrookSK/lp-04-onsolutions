# Documentação Técnica — Landing Page 04: Integração de Sistemas

## 1. Identificação do projeto

| Item | Valor |
|------|-------|
| Nome da landing page | LP04 — Integração de Sistemas |
| Objetivo | Apresentar os serviços de integração de sistemas e APIs da ON Solutions Brasil (ERP, loja virtual, banco, pagamentos e WhatsApp), com captação de leads direta pelo WhatsApp. |
| URL prevista | `https://onsolutionsbrasil.com.br/lp/integracao-de-sistemas/` |
| Arquivo HTML de referência | `04-lp-integracao-de-sistemas.html` |
| Serviço (data-service) | `Integrações & APIs` |

---

## 2. Estrutura de arquivos

Projeto estático (HTML/CSS/JS puros). O repositório estava vazio (apenas `README.md`); **não existem LP01, LP02 ou LP03 no workspace**, portanto não há controllers/views/rotas anteriores a reutilizar. A LP04 foi implementada de forma independente, na rota que corresponde exatamente à URL prevista.

### Arquivos criados

| Arquivo | Localização | Responsabilidade |
|---------|-------------|------------------|
| `index.html` | `lp/integracao-de-sistemas/` | Marcação (estrutura) completa da página: cabeçalho, hero, desafios, benefícios, prova social, como funciona, oferta, FAQ, CTA final, rodapé e botão fixo. Metadados de SEO. |
| `styles.css` | `lp/integracao-de-sistemas/` | Toda a folha de estilos (cópia fiel do `<style>` da referência): paleta, tipografia, gradientes, componentes, animações e breakpoints responsivos. |
| `app.js` | `lp/integracao-de-sistemas/` | Comportamentos (cópia fiel do `<script>` da referência): links de WhatsApp, mensagem dinâmica, prévia de conversa, origem de anúncio, rastreamento opcional, cabeçalho que esconde/reaparece e carrossel infinito. |
| `assets/favicon.png` | `assets/` | Favicon 48×48. **(placeholder — ver seção 12)** |
| `assets/logo-on.png` | `assets/` | Logotipo ON Solutions (cabeçalho e prévia de WhatsApp). **(placeholder — ver seção 12)** |
| `assets/cliente-braziliana.png` | `assets/` | Logo de cliente (carrossel). **(placeholder)** |
| `assets/cliente-quatri.png` | `assets/` | Logo de cliente (carrossel). **(placeholder)** |
| `assets/cliente-brooks.png` | `assets/` | Logo de cliente (carrossel). **(placeholder)** |
| `assets/cliente-crosshr.png` | `assets/` | Logo de cliente (carrossel). **(placeholder)** |
| `assets/cliente-multilife.png` | `assets/` | Logo de cliente (carrossel). **(placeholder)** |
| `assets/cliente-mafedo.png` | `assets/` | Logo de cliente (carrossel). **(placeholder)** |
| `assets/extrair-imagens.py` | `assets/` | Script utilitário que extrai as 8 imagens Base64 reais do HTML de referência e grava os PNGs definitivos, substituindo os placeholders. |
| `assets/_gerar_placeholders.py` | `assets/` | Script que gerou os PNGs placeholder (mantido para rastreabilidade). |
| `DOCUMENTACAO-LP04-INTEGRACAO-DE-SISTEMAS.md` | raiz | Este documento. |

### Arquivos modificados

- Nenhum arquivo pré-existente foi modificado. O `README.md` e as demais páginas não foram tocados. Não havia LPs anteriores para impactar.

---

## 3. Arquitetura

- **Tipo:** site estático. A referência é um único HTML autocontido; aqui o conteúdo foi dividido em três arquivos (`index.html`, `styles.css`, `app.js`) e os recursos de imagem foram externalizados para `/assets`, melhorando organização, cache e performance, sem alterar comportamento ou identidade visual.
- **Rota:** `lp/integracao-de-sistemas/` → serve `index.html`, reproduzindo a URL prevista.
- **Controllers/Views:** não se aplica (não há framework no projeto).
- **Dependências externas:** apenas a fonte Poppins via Google Fonts (`preconnect` + `stylesheet`), exatamente como na referência. Nenhuma biblioteca JS/CSS adicional.
- **Caminhos relativos:** CSS/JS são relativos ao `index.html` (`styles.css`, `app.js`); imagens apontam para `assets/…` a partir da raiz de publicação.

---

## 4. Identidade visual

- **Tipografia:** Poppins (pesos 400, 500, 600, 700, 800), com fallback `"Segoe UI", system-ui, -apple-system, sans-serif`.
- **Paleta (variáveis CSS):** `--ink #0B1220`, `--navy #0F172A`, `--bg #F5F8FB`, `--line #E2E8F0`, `--text #0F172A`, `--soft #52627A`, `--mint #5EEAD4`, `--teal #0D9488`, `--tealD #0F766E`, `--wa #25D366`, `--waD #1EBE5B`.
- **Gradientes:** hero e CTA final com gradientes escuros (ink → teal) e brilhos em mint/turquesa; cards de oferta em gradiente `#0F2D3A → #134E4A`.
- **Elementos visuais:** botões WhatsApp com sombra e brilho animado; cards com cantos arredondados e bordas suaves; contraste entre seções claras (`.sec-w`) e escuras (`.proof`, `.final`).
- **Responsivo:** `width:min(1120px, 100% - margem)`; grids que passam de 1 coluna (mobile) para 2–4 colunas (desktop).

---

## 5. Estrutura das seções (ordem preservada)

1. **Cabeçalho** (`header.top`) — logo, telefone, botão "Orçamento", sticky, esconde/reaparece na rolagem.
2. **Hero** (`.hero`) — badge, H1, descrição, benefícios, selos de confiança e prévia de conversa de WhatsApp.
3. **Desafios** (`#dores`) — 4 botões selecionáveis (multi-seleção).
4. **Benefícios** (`#beneficios`) — 4 cards.
5. **Prova social** (`#clientes`) — indicadores (100+, 50+, Brasil e exterior) e carrossel de clientes (inclui Central RZ).
6. **Como funciona** (`#como-funciona`) — 3 passos numerados.
7. **Oferta** (`#oferta`) — 3 itens, fundo em gradiente escuro.
8. **FAQ** (`#duvidas`) — 3 perguntas em acordeão (`<details>`).
9. **CTA final** (`#conversa`) — título, texto e nota.
10. **Rodapé** (`.foot`) — assinatura, e-mail e links LGPD/Privacidade.
11. **Botão fixo** (`.sticky`) — "Pedir orçamento no WhatsApp".

Todos os textos, títulos e microcópias são cópia fiel da referência.

---

## 6. Funcionalidades

- **Seleção múltipla de desafios:** cada `.pain` alterna `aria-pressed` true/false ao clicar (marca/desmarca); permite várias simultâneas.
- **Atualização dinâmica da mensagem:** `sync()` recompõe a mensagem do WhatsApp a partir dos desafios marcados (sem duplicações, sem resíduo antigo):
  - 0 selecionados → mensagem base.
  - 1 → base + `Meu maior desafio hoje: [desafio].`
  - 2+ → base + `Meus maiores desafios hoje: [d1]; [d2]; …`.
- **Mensagens auxiliares (`data-hint`, `aria-live="polite"`):** vazia sem seleção; "Pronto! Agora toque em 'Pedir orçamento no WhatsApp' para enviar." com 1; "Você marcou [N]. Isso tem solução: …" com 2+.
- **Prévia de conversa (hero):** a bolha `data-bubble` acompanha a mesma mensagem.
- **Links de WhatsApp:** todos os `[data-wa]` recebem `href` via `waLink()`, com `target="_blank"` e `rel="noopener"`. Os três botões principais usam `data-wa-main` e refletem a MESMA mensagem dinâmica.
- **Botão fixo:** barra inferior com animação de entrada; respeita `safe-area-inset-bottom`.
- **Carrossel de clientes:** duplica os itens para loop infinito contínuo; calcula a velocidade pela largura; pausa ao toque; respeita `prefers-reduced-motion` (não anima).
- **Acordeão de FAQ:** `<details>/<summary>` nativo; ícone +/– via CSS.
- **Cabeçalho:** esconde ao rolar para baixo, reaparece ao rolar para cima, fica visível perto do topo (`y < 80`) e ao receber foco de teclado (`focusin`). Usa `requestAnimationFrame` (sem travar a rolagem).
- **Reset ao navegar por âncora (`hashchange`):** limpa seleção e hints.

---

## 7. Integração com WhatsApp

- **Número:** `5511972243329`.
- **Base dos links:** `https://wa.me/5511972243329?text=` + mensagem codificada com `encodeURIComponent`.
- **Pontos de integração:** telefone do cabeçalho (`topo-telefone`), botão Orçamento do cabeçalho (`topo`), botão fixo inferior (`barra-fixa`). Todos abrem em nova aba com atributos de segurança.
- **Parâmetros de origem (anúncios):** lê `utm_term`, `kw`, `utm_campaign`, `gclid`. Com `ON_APPEND_ORIGIN = true` e havendo dados, acrescenta à mensagem: `Origem: anúncio | Termo: [termo] | Campanha: [campanha]` (apenas os dados disponíveis).

---

## 8. Rastreamento

- **Configuração (vazia por padrão):** `ON_TRACKING = { gtmId:"", ga4Id:"", gadsId:"", gadsConversionLabel:"" }`. Nada é carregado enquanto os IDs estiverem vazios. **Nenhum ID fictício foi inserido.**
- **Carregamento condicional:** GTM, GA4 e Google Ads só são injetados quando os respectivos IDs forem preenchidos.
- **Eventos:** `whatsapp_click` (dataLayer) e `generate_lead` (gtag) com `service` ("Integrações & APIs") e `position` (`topo-telefone` | `topo` | `barra-fixa`). Conversão do Google Ads disparada somente se `gadsId` e `gadsConversionLabel` estiverem preenchidos.
- **Robustez:** o disparo ocorre em listener de captura e não bloqueia a abertura do WhatsApp.

---

## 9. Responsividade

- **Breakpoints presentes:** `max-width:340px`, `380px`, `400px`, `430px` e `min-width:860px` (todos preservados da referência).
- **Mobile:** cabeçalho compacto (60px), hero em coluna única, cards empilhados, botões com área de toque ampla, carrossel por toque, botão fixo sem sobrepor conteúdo (o rodapé reserva espaço com `padding-bottom`), respeito à safe-area.
- **Desktop (≥860px):** hero em 2 colunas, benefícios em 4 colunas, passos/indicadores em 3 colunas, oferta em 2 colunas, telefone visível no cabeçalho, maior respiro vertical.

---

## 10. SEO e acessibilidade

- **Title:** `Integração de Sistemas | ON Solutions Brasil`.
- **Description:** `Conectamos ERP, loja virtual, banco, pagamentos e WhatsApp para a informação fluir sozinha.`
- **Canonical:** `https://onsolutionsbrasil.com.br/lp/integracao-de-sistemas/`.
- **Robots:** `noindex,follow` (mantido).
- **Theme-color:** `#0B1220`. **Viewport:** com `viewport-fit=cover`.
- **Hierarquia:** 1 H1 (hero) + 7 H2 (seções) + H3 nos cards.
- **Acessibilidade:** `aria-pressed` nos desafios; `aria-live="polite"` nas dicas; `role="group"` no conjunto de desafios; `aria-hidden` nos clones do carrossel; foco visível (`:focus-visible`); o cabeçalho reaparece ao foco por teclado; `alt` nas imagens; botões com nome acessível.

---

## 11. Testes realizados

Ambiente: servidor estático local (`python -m http.server`), Node 22 e Python 3.14.

| # | Teste | Resultado |
|---|-------|-----------|
| 1 | HTTP 200 de `index.html`, `styles.css`, `app.js` e assets | **OK** (todos 200, tamanhos conferidos) |
| 2 | Metadados (title, description, robots, canonical, theme-color) | **OK** |
| 3 | Hierarquia de títulos (1×H1, 7×H2) | **OK** |
| 4 | Presença das 11 seções/elementos na ordem correta | **OK** |
| 5 | 4 desafios com `aria-pressed="false"` inicial e textos exatos | **OK** |
| 6 | 4 benefícios, indicadores (100+, 50+, Brasil e exterior) e "Central RZ" | **OK** |
| 7 | FAQ com 3 `<details>`/`<summary>` | **OK** |
| 8 | Rodapé: e-mail e links LGPD/Privacidade | **OK** |
| 9 | 3 botões `data-wa-main` nas posições topo-telefone / topo / barra-fixa | **OK** |
| 10 | Número `5511972243329`, base `wa.me`, `encodeURIComponent` | **OK** |
| 11 | Parâmetros de origem (`utm_term`, `kw`, `utm_campaign`, `gclid`) e texto "Origem: anúncio" | **OK** |
| 12 | IDs de rastreamento vazios (sem IDs fictícios); eventos `whatsapp_click` e `generate_lead` | **OK** |
| 13 | CSS `.top.hide` + JS de esconder/foco do cabeçalho | **OK** |
| 14 | Breakpoints 340/380/400/430/860 e `prefers-reduced-motion` (CSS e JS) | **OK** |
| 15 | **Lógica de mensagem dinâmica (Node):** 0/1/2/4 desafios + origem de anúncio; plural/singular; sem duplicar pontuação; link final codificado em UTF-8 | **OK (7/7 asserts)** |

**Observações sobre o que foi e o que não foi verificado:**
- Verificado automaticamente: estrutura, metadados, acessibilidade (atributos ARIA), presença/forma dos links de WhatsApp e a lógica de composição da mensagem/links (execução real em Node).
- **Não verificado em navegador gráfico:** inspeção visual pixel a pixel, teste tátil real do carrossel em dispositivo físico e leitura por leitor de tela real. Recomenda-se um passo manual de QA visual (seção 30 da demanda) antes de publicar.
- Console: não foram encontrados erros estáticos; não foi possível capturar o console de um navegador real neste ambiente.

---

## 12. Pendências e observações

1. **Imagens placeholder (pendência principal).** As 8 imagens do original estão embutidas como Base64 no HTML de referência. Neste ambiente não foi possível transportar com segurança essas strings Base64 (muito extensas) para arquivos. Para não entregar imagens quebradas, foram gerados **placeholders PNG com as dimensões corretas** (favicon 48×48, logo ON, e logos de clientes 272×84). Eles mantêm o layout e as proporções, mas **não são os logotipos reais**.

   **Como colocar as imagens reais (1 comando):**
   ```bash
   python assets/extrair-imagens.py "caminho/para/04-lp-integracao-de-sistemas.html"
   ```
   O script lê o HTML de referência, extrai os 8 Base64 e grava os PNGs definitivos em `/assets`, substituindo os placeholders. Nenhuma outra alteração é necessária — os caminhos em `index.html` já apontam para esses arquivos.

   > Alternativa equivalente: reinserir os `data:image/png;base64,…` originais diretamente nos `src` das imagens em `index.html` (forma idêntica à da referência).

2. **IDs de rastreamento.** `gtmId`, `ga4Id`, `gadsId` e `gadsConversionLabel` estão **vazios por decisão de projeto** (como na referência). Preencher em `app.js` quando os identificadores oficiais forem fornecidos. Nada é carregado até lá.

3. **Links do rodapé (LGPD / Política de privacidade).** Apontam para `#`, como na referência (não há rotas válidas no projeto). Atualizar para as URLs reais quando existirem.

4. **QA visual.** Recomendado comparar a página renderizada com a referência em mobile e desktop (seção 30 da demanda) antes da publicação — não executado em navegador gráfico neste ambiente.

5. **Publicação.** Não foi publicada em servidor; nenhuma ação de deploy foi realizada (conforme a demanda, sem autorização).
