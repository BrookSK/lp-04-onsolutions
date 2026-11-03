#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extrai as 8 imagens Base64 do HTML de referência (04-lp-integracao-de-sistemas.html)
e grava os PNGs reais em /assets, substituindo os placeholders.

USO:
    python assets/extrair-imagens.py CAMINHO_DO_HTML_DE_REFERENCIA

Exemplo:
    python assets/extrair-imagens.py "04-lp-integracao-de-sistemas.html"

O script identifica as imagens pela ordem em que aparecem no HTML original:
  1. favicon           -> assets/favicon.png        (<link rel="icon" ...>)
  2. logo ON (brand)   -> assets/logo-on.png        (1a imagem data:image dentro de .brand/.chat-head)
  3..8. logos clientes -> assets/cliente-*.png       (imagens dentro de .chip, na ordem do carrossel)

As imagens do carrossel são mapeadas pelo atributo alt:
  "Braziliana"->cliente-braziliana  "Quatri"->cliente-quatri  "Brooks"->cliente-brooks
  "CrossHR"->cliente-crosshr        "MultiLife"->cliente-multilife  "Mafedo"->cliente-mafedo
"""
import sys, os, re, base64

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    ref = sys.argv[1]
    if not os.path.isfile(ref):
        print(f"Arquivo não encontrado: {ref}")
        sys.exit(1)

    html = open(ref, "r", encoding="utf-8").read()
    out_dir = os.path.dirname(os.path.abspath(__file__))

    def save(name, b64):
        data = base64.b64decode(b64)
        path = os.path.join(out_dir, name)
        with open(path, "wb") as f:
            f.write(data)
        print(f"  gravado: {name} ({len(data)} bytes)")

    # 1) favicon — no atributo href do <link rel="icon">
    m = re.search(r'rel=["\']icon["\'][^>]*href=["\']data:image/png;base64,([A-Za-z0-9+/=]+)["\']', html)
    if m:
        save("favicon.png", m.group(1))
    else:
        print("  AVISO: favicon não encontrado")

    # 2) logo ON — primeira imagem data:image dentro de <img ...> (brand). Reusada no chat-head.
    imgs = re.findall(r'<img[^>]*src=["\']data:image/png;base64,([A-Za-z0-9+/=]+)["\'][^>]*alt=["\']([^"\']*)["\']', html)
    # a tag do brand tem alt="" ; a do chat-head também alt="". Pegamos a 1a ocorrência como logo ON.
    m_logo = re.search(r'class=["\']brand["\'][^>]*>\s*<img[^>]*src=["\']data:image/png;base64,([A-Za-z0-9+/=]+)["\']', html)
    if m_logo:
        save("logo-on.png", m_logo.group(1))
    else:
        print("  AVISO: logo ON não encontrado")

    # 3) logos dos clientes — imagens dentro de .chip, mapeadas pelo alt
    mapa = {
        "braziliana": "cliente-braziliana.png",
        "quatri": "cliente-quatri.png",
        "brooks": "cliente-brooks.png",
        "crosshr": "cliente-crosshr.png",
        "multilife": "cliente-multilife.png",
        "mafedo": "cliente-mafedo.png",
    }
    chips = re.findall(r'<div class=["\']chip["\']>\s*<img[^>]*src=["\']data:image/png;base64,([A-Za-z0-9+/=]+)["\'][^>]*alt=["\']([^"\']*)["\']', html)
    for b64, alt in chips:
        low = alt.lower()
        for chave, nome in mapa.items():
            if chave in low:
                save(nome, b64)
                break

    print("Concluído. Os placeholders SVG podem ser removidos se desejar.")

if __name__ == "__main__":
    main()
