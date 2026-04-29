# -*- coding: utf-8 -*-
"""Resize PNGs from SHIFTpro folder → small WebP in ../assets/"""
from pathlib import Path
from PIL import Image

SRC = Path(r"C:\Users\USER\OneDrive\デスクトップ\AI遊び場\SHIFTproプレゼン0421")
OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(parents=True, exist_ok=True)

# デッキ用のサムネイル相当（GitHub 容量を抑える）
MAX_W = 480
QUALITY = 58

def pick_paths():
    pngs = sorted(SRC.glob("*.png"))
    if len(pngs) < 2:
        raise SystemExit(f"Need 2 PNGs in {SRC}, found: {pngs}")
    # 名前に含まれる文字で Before / After を判定（文字化け時はサイズ順などにしない）
    before = after = None
    for p in pngs:
        n = p.name
        if "パスポート" in n or "\u30d1\u30b9\u30dd" in n:
            before = p
        if "G検定" in n or "G\u691c\u5b9a" in n or "G" in n:
            after = p
    if before is None:
        before = pngs[0]
    if after is None:
        after = pngs[1] if pngs[1] != before else pngs[0]
    if before == after and len(pngs) >= 2:
        before, after = pngs[0], pngs[1]
    return before, after


def save_webp(src: Path, dest: Path) -> None:
    im = Image.open(src).convert("RGB")
    w, h = im.size
    if w > MAX_W:
        nh = int(h * (MAX_W / w))
        im = im.resize((MAX_W, nh), Image.Resampling.LANCZOS)
    im.save(dest, "WEBP", quality=QUALITY, method=6, optimize=True)
    print(f"{src.name} → {dest.name} ({dest.stat().st_size // 1024} KB)")


def main():
    b, a = pick_paths()
    save_webp(b, OUT / "g-cert-before.webp")
    save_webp(a, OUT / "g-cert-after.webp")


if __name__ == "__main__":
    main()
