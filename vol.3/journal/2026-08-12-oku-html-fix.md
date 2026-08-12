# 2026-08-12 oku.html修正メモ

vol.3/oku.htmlの`.stroke .meta`および未来デザインカード説明文の`white-space:nowrap`（狭い画面で右側の文字が`overflow-x:hidden`により切れる不具合）を修正。

詳細な作業記録は本リポジトリではなく、`ELITE\ELITE HOUSE\8.22SHIFTAIイベント\journal\2026-08-12_oku-html-text-overflow-fix.md`に記録済み（822-lp.htmlからのリンク先ページとして、8.22プロジェクトの作業フォルダ側にまとめて記録する運用のため）。

## 追記：折り返し2行目の字下げ

雪舟から「TOMOYA以下9行の折り返し2行目（例：『材料を整える』）を#ffffffの下に揃えたい」と指示。`.stroke .meta`にハンギングインデント（`padding-left:170px;text-indent:-170px`）を追加。170pxは名前欄100px＋余白＋hexコード分の推定値のため、公開後に実機で確認し必要なら微調整する。
