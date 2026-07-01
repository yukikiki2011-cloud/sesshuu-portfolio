# motion-memo — sesshuu-portfolio-logomotion アニメーション用語メモ

作成: 2026-07-01

---

## 用語説明

| 用語 | 意味 |
|---|---|
| **スクランブル（Scramble）** | 文字がランダムな記号・カナに化けて、正しい文字に「解読」されるように戻る演出。ハッカー的なコード感が出る |
| **グリッチ（Glitch）** | 映像やデジタル信号が一瞬乱れる現象・演出。テレビのノイズやデジタル崩壊のような瞬間的な乱れ |
| **Hero** | Webページのファーストビュー（開いて最初に見える大きなエリア）。「主役」の意味でWeb用語として定着 |
| **ブリーズ / フロート（Breathe / Float）** | 文字や要素がゆっくり呼吸・浮遊するように動くアニメーション。このコードでは `navLogoDrive` という名前 |

---

## このサイトで使われているアニメーション一覧

| アニメーション名 | 種類 | 対象 | 説明 |
|---|---|---|---|
| `navBarSnap` | snap | navバー全体 | ページロード時に上からスナップイン（0.36s・1回のみ） |
| `nlMainSnap` | snap | nav ロゴ "sesshuu" | ロゴのメインテキストがスナップイン |
| `nlAccentSnap` | snap | nav ロゴ "design" | ロゴのイタリック部分がスナップイン |
| `navLinkPop` | pop | ナビリンク各項目 | 上からフェードイン（順次 delay 付き・1回のみ） |
| `navLogoDrive` | breathe | nav ロゴ全体 | letter-spacing が 0.03em → 0.16em → 0.03em を 1.55s でループ。文字が呼吸するように広がる |
| `heroTitleSnap` | snap | Hero "sesshuu" | Heroタイトルのスナップイン（0.52s・1回のみ） |
| `heroAccentSnap` | snap | Hero "design" | Heroアクセントのスナップイン（0.48s・1回のみ） |
| `typog-scramble-root--hero` | scramble | Hero タイトル文字 | スクランブル + グリッチ（3秒ON → 18秒待機のサイクル） |
| `typog-scramble-root`（nav） | glitch | nav ロゴ文字 | グリッチのみ（Hero scramble と同期して停止） |
| `heroGlowDrift` | drift | Hero 背景グロー | 背景の光が漂う（22s ループ） |
| `gridPulse` | pulse | Hero 背景グリッド | グリッドが脈打つ（14s ループ） |
| `heroOverlayBreath` | breathe | Hero ポートレートオーバーレイ | 写真のオーバーレイが呼吸する（6.2s ループ） |
| `scrollNudge` | nudge | Scroll インジケーター | 下矢印がバウンス（2.4s ループ） |

---

## JS 同期制御（2026-07-01 追加）

Hero scramble が止まるとき（`setHeroMotion(false)`）にNav glitch も同時停止するよう修正。

```javascript
var navGlitchIntervals = [];
// nav の各 .typog-scramble-root の interval ID を配列で保持
// setHeroMotion(false) 時に全件 clearInterval + clearHeroGlitchState を実行
```

**効果:** Hero の「sesshuu design」が止まったら、ナビロゴのグリッチも同時に静止する。
