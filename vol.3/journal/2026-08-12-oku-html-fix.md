# 2026-08-12 oku.html修正メモ

vol.3/oku.htmlの`.stroke .meta`および未来デザインカード説明文の`white-space:nowrap`（狭い画面で右側の文字が`overflow-x:hidden`により切れる不具合）を修正。

詳細な作業記録は本リポジトリではなく、`ELITE\ELITE HOUSE\8.22SHIFTAIイベント\journal\2026-08-12_oku-html-text-overflow-fix.md`に記録済み（822-lp.htmlからのリンク先ページとして、8.22プロジェクトの作業フォルダ側にまとめて記録する運用のため）。

## 追記：折り返し2行目の字下げ（1回目・失敗）

雪舟から「TOMOYA以下9行の折り返し2行目（例：『材料を整える』）を#ffffffの下に揃えたい」と指示。`.stroke .meta`にハンギングインデント（`padding-left:170px;text-indent:-170px`）を追加したが、雪舟から「全体のバランスが崩れた」と報告。padding-leftが1行目も含めた利用可能幅を170px削ってしまい、この狭い列幅（38%/62%分割）では収まらないことが原因と判明。

## 追記2：グリッド2列構成への変更（修正版）

上記の反省を踏まえ、text-indentハックを撤回し、`<b>`（名前）と`<span class="hex">+説明文`（新設の`<span class="desc">`でラップ）を`.meta{display:grid;grid-template-columns:100px auto}`の2列として構成し直した。折り返した2行目は`desc`列自身の左端（=hexコードの開始位置）に自然に揃う。利用可能幅を余計に削らないため、狭い列幅でも成立する想定。HTML側9行すべてに`<span class="desc">`ラップを追加。

GAI行（「異端創造——雪舟だけの解を発明する」）が2行に収まらない場合は、雪舟の指示により9行すべての「——」を短縮する方針（未実施・公開後の確認待ち）。
