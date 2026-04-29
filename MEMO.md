# sesshuu portfolio 作業メモ

## 公開URL�E�ブラウザで見る�E�E

**ポ�Eトフォリオ全体（トチE�E�E�E*  
https://yukikiki2011-cloud.github.io/sesshuu-portfolio/

**完�Eスライド！Elaude Code チE��キ・全画面�E�E*  
https://yukikiki2011-cloud.github.io/sesshuu-portfolio/atelier-slide/index.html  

トップ�Eージの **Works** セクションからも同じデチE��に遷移できる、E

## GitHubリポジトリ
https://github.com/yukikiki2011-cloud/sesshuu-portfolio

## ホスチE��ング
GitHub Pages�E�無料！E
- Branch: main / root
- 設定場所: Settings ↁEPages

## 2026-03-30 の修正冁E��

### 1. Contactボタンのスムーズスクロール修正
- NAVバ�Eの「Contact」�EタンをクリチE��するとペ�Eジ最下部のお問ぁE��わせ欁E��でスクロールするように修正
- JavaScriptで全アンカーリンク�E�Ehref="#..."`�E�に対してスムーズスクロールを実裁E
- 対象ファイル: `index.html`�E�E<script>`冁E��E

### 2. フォーム送信先メールアドレス変更
- 変更剁E `yukikiki2011@gmail.com`
- 変更征E `yukikiki2011+work@gmail.com`
- 対象ファイル: `index.html`�E�Eine 2096 の `<form action="mailto:...">` 部刁E��E

## GitHub Pages 公開手頁E��覚え書き！E
1. GitHubリポジトリの Settings ↁEPages を開ぁE
2. Source: Deploy from a branch
3. Branch: main / / (root) ↁESave
4. 数刁E��に公開URL が発行される
5. ローカルの変更は `git push origin main` でサイトに反映されめE
