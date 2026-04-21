# -*- coding: utf-8 -*-
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT.parent / "adobe-express-x-strategy" / "strategy-diagram.png"
OUT = ROOT / "assets" / "adobe-x-shiftpro-strategy.webp"
OUT.parent.mkdir(parents=True, exist_ok=True)

im = Image.open(SRC).convert("RGB")
w, h = im.size
mw = 920
if w > mw:
    im = im.resize((mw, int(h * mw / w)), Image.Resampling.LANCZOS)
im.save(OUT, "WEBP", quality=68, method=6)
print(OUT, OUT.stat().st_size, "bytes")
