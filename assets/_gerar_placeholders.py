#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera PNGs placeholder (dimensoes corretas) para a LP04 ate que as imagens
reais do HTML de referencia sejam extraidas com extrair-imagens.py."""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.dirname(os.path.abspath(__file__))

INK = (11, 18, 32, 255)
NAVY = (15, 45, 58, 255)
TEAL = (19, 78, 74, 255)
MINT = (94, 234, 212, 255)
SLATE = (82, 98, 122, 255)
WHITE = (255, 255, 255, 255)

def font(size):
    for name in ("segoeuib.ttf", "arialbd.ttf", "DejaVuSans-Bold.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except Exception:
            continue
    return ImageFont.load_default()

def centered(draw, box, text, fnt, fill):
    l, t, r, b = draw.textbbox((0, 0), text, font=fnt)
    w, h = r - l, b - t
    x = box[0] + (box[2] - box[0] - w) / 2 - l
    y = box[1] + (box[3] - box[1] - h) / 2 - t
    draw.text((x, y), text, font=fnt, fill=fill)

def logo_on(path, size=96):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([2, 2, size - 2, size - 2], radius=20, fill=INK)
    centered(d, (0, 0, size, size), "ON", font(int(size * 0.42)), MINT)
    img.save(path)
    print("ok", os.path.basename(path))

def favicon(path, size=48):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([1, 1, size - 1, size - 1], radius=10, fill=INK)
    centered(d, (0, 0, size, size), "ON", font(int(size * 0.42)), MINT)
    img.save(path)
    print("ok", os.path.basename(path))

def cliente(path, nome, w=272, h=84):
    # 2x das dimensoes do slot (.chip img ~136x42) para nitidez
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    centered(d, (0, 0, w, h), nome, font(26), NAVY)
    img.save(path)
    print("ok", os.path.basename(path))

favicon(os.path.join(OUT, "favicon.png"))
logo_on(os.path.join(OUT, "logo-on.png"))
cliente(os.path.join(OUT, "cliente-braziliana.png"), "Braziliana")
cliente(os.path.join(OUT, "cliente-quatri.png"), "Quatri")
cliente(os.path.join(OUT, "cliente-brooks.png"), "Brooks")
cliente(os.path.join(OUT, "cliente-crosshr.png"), "CrossHR")
cliente(os.path.join(OUT, "cliente-multilife.png"), "MultiLife")
cliente(os.path.join(OUT, "cliente-mafedo.png"), "Mafedo")
print("placeholders gerados")
