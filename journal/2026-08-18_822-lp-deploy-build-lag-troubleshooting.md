# 2026-08-18 822/index.html デプロイ反映待ちの切り分け

## 経緯
`822/index.html`へのモバイル質問文折返し修正（commit `1f7161b`）をmain・gh-pages双方にpush後、雪舟が公開URLをモバイル実機で確認したところ「直ってない」との報告があった。

## 切り分け（Claudeが実施）
1. `curl`で公開URLのCSSを直接確認 → `.exp-q{font-size:var(--fs-8);...}`のまま。旧版が配信されていた
2. `git fetch origin gh-pages`でgh-pagesブランチの実際の中身を確認 → 修正版（`clamp(18px,6vw,28px)`）が正しく格納されていることを確認。push自体は成功していた
3. レスポンスヘッダーを確認 → `Last-Modified: 2026-08-17`のままでビルド未反映、`Cache-Control: max-age=600`
4. `gh api repos/yukikiki2011-cloud/sesshuu-portfolio/pages/builds/latest`でGitHub Pagesのビルド状態を確認 → `status:"building"`（commit `1f7161b`をビルド中）
5. 15秒間隔でポーリングし、`status:"built"`になったことを確認
6. 再度`curl`で確認 → `Last-Modified`が反映時刻に更新され、修正版CSSが配信されていることを確認

## 結論
不具合の再発ではなく、GitHub Pagesのビルド反映タイムラグ（今回は1分未満）が原因だった。push直後に確認すると数十秒〜数分は旧版が配信され続けることがある。雪舟が確認し直し「OK」で解決確認済み。

## 教訓
- gh-pages公開直後の確認は、pushの成功だけでなく`gh api .../pages/builds/latest`のビルド状態も見る方が誤診断を防げる
- 配信キャッシュ（Cache-Control: max-age=600）もあるため、確認時はキャッシュバスター付きcurlやブラウザのプライベートウィンドウを使うと切り分けが早い
