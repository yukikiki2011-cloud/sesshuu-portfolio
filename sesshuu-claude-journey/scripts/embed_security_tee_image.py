# -*- coding: utf-8 -*-
"""Discord スクショ（セキュリティTシャツ）を縮小→ index.html の Security tee 直下に data URI 埋め込み"""
import base64
import io
import re
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"

# Cursor に保存された添付 PNG（必要ならパスを差し替え）
SRC = Path(
    r"C:\Users\USER\.cursor\projects\c-Users-USER-OneDrive-GitHub\assets"
    r"\c__Users_USER_AppData_Roaming_Cursor_User_workspaceStorage_56f421f9659f5700abb246586b3a0750_images_image-17cdcd73-69d7-4ff3-aee4-afd35a119045.png"
)

OLD = r'<li><strong>Security tee</strong> — セキュリティTシャツのグレードアップチャレンジ。</li>'

NEW_TEMPLATE = """<li>
          <strong>Security tee</strong> — セキュリティTシャツのグレードアップチャレンジ。
          <figure class="security-tee-capture">
            <img src="{uri}" alt="SHIFT AI コミュニティ Discord：セキュリティTシャツ案の共有画面" loading="lazy" decoding="async" />
            <figcaption>Discord 共有例（デザイン改定・リアクション）</figcaption>
          </figure>
        </li>"""


def main():
    if not SRC.exists():
        raise SystemExit(f"Source image not found: {SRC}")
    im = Image.open(SRC).convert("RGB")
    w, h = im.size
    mw = 640
    if w > mw:
        im = im.resize((mw, int(h * mw / w)), Image.Resampling.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "WEBP", quality=58, method=6)
    raw = buf.getvalue()
    print("webp bytes:", len(raw))
    uri = "data:image/webp;base64," + base64.b64encode(raw).decode("ascii")
    html = INDEX.read_text(encoding="utf-8")
    if OLD not in html:
        raise SystemExit("OLD marker not found — Security tee line may have changed")
    if '<figure class="security-tee-capture">' in html:
        raise SystemExit("Already embedded — skip")
    html = html.replace(OLD, NEW_TEMPLATE.format(uri=uri), 1)
    INDEX.write_text(html, encoding="utf-8")
    print("OK", INDEX)


if __name__ == "__main__":
    main()
