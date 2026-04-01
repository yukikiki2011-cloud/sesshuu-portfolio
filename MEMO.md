# sesshuu portfolio 作業メモ

## 公開URL
https://yukikiki2011-cloud.github.io/sesshuu-portfolio/

## GitHubリポジトリ
https://github.com/yukikiki2011-cloud/sesshuu-portfolio

## ホスティング
GitHub Pages（無料）
- Branch: main / root
- 設定場所: Settings → Pages

## 2026-03-30 の修正内容

### 1. Contactボタンのスムーズスクロール修正
- NAVバーの「Contact」ボタンをクリックするとページ最下部のお問い合わせ欄までスクロールするように修正
- JavaScriptで全アンカーリンク（`href="#..."`）に対してスムーズスクロールを実装
- 対象ファイル: `index.html`（`<script>`内）

### 2. フォーム送信先メールアドレス変更
- 変更前: `yukikiki2011@gmail.com`
- 変更後: `yukikiki2011+work@gmail.com`
- 対象ファイル: `index.html`（line 2096 の `<form action="mailto:...">` 部分）

## GitHub Pages 公開手順（覚え書き）
1. GitHubリポジトリの Settings → Pages を開く
2. Source: Deploy from a branch
3. Branch: main / / (root) → Save
4. 数分後に公開URL が発行される
5. ローカルの変更は `git push origin main` でサイトに反映される
