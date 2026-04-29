# -*- coding: utf-8 -*-
"""assets の WebP を縮小→base64 で index.html に埋め込み（相対パス切れ対策）"""
import base64
import io
import re
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"
ASSETS = ROOT / "assets"

# (ファイル名, max_width, quality)
SPECS = [
    ("g-cert-before.webp", 420, 54),
    ("g-cert-after.webp", 420, 54),
    ("adobe-x-shiftpro-strategy.webp", 640, 56),
]


def to_data_uri(name: str, max_w: int, q: int) -> str:
    path = ASSETS / name
    if not path.exists():
        raise FileNotFoundError(path)
    im = Image.open(path).convert("RGB")
    w, h = im.size
    if w > max_w:
        im = im.resize((max_w, int(h * max_w / w)), Image.Resampling.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format="WEBP", quality=q, method=6)
    b = buf.getvalue()
    print(f"{name}: {len(b)} bytes")
    return "data:image/webp;base64," + base64.b64encode(b).decode("ascii")


def main():
    html = INDEX.read_text(encoding="utf-8")
    for name, mw, q in SPECS:
        uri = to_data_uri(name, mw, q)
        pat = re.compile(r'src="assets/' + re.escape(name) + r'"')
        html, n = pat.subn('src="' + uri + '"', html, count=1)
        if n != 1:
            raise SystemExit(f"replace failed for {name}, n={n}")
    INDEX.write_text(html, encoding="utf-8")
    print("OK:", INDEX)


if __name__ == "__main__":
    main()
