# HelpDesk Motor Company FAQ 刷新ハンズオン用リポジトリ

このリポジトリは、2 時間の GitHub + Copilot 初心者向けワークショップで利用するサンプルデータです。HelpDesk Motor Company の FAQ を最新化しながら、GUI（GitHub Desktop / Web UI）中心の開発フローを体験します。

## このリポジトリでできること

1. 変更 → コミット → プッシュをすべて GUI で体験できます。
2. Issue からブランチを作り、Pull Request（変更内容を共有するための仕組み）を送る手順を学べます。
3. GitHub Projects でタスクを動かし、作業状況を可視化できます。
4. GitHub Copilot / Copilot Chat を使い、FAQ 文書の下書きやレビューをサポートさせられます。
5. GitHub Actions + Pages を使って、更新した FAQ を公開する流れを確認できます。

## フォルダ構成

```text
docs/faq/        ワークショップで編集する FAQ 記事
assets/          画像・テンプレートなど補助ファイル
.github/         Issue テンプレート、Pull Request テンプレ、Actions
projects/        GitHub Projects（カンバン）の定義
.devcontainer/   Codespaces 用の開発環境設定
```

## クイックスタート

1. このリポジトリを **Fork**（自分のアカウントにコピー）し、GitHub Desktop で clone するか **Codespaces** を起動します。Codespaces 手順は `docs/codespaces-guide.md` に詳しく記載しています。
2. `Helpdesk Ticket` Issue テンプレートから問い合わせを作成し、「Create branch」ボタンで作業ブランチを作ります。
3. `docs/faq/` 以下の該当ファイルを編集し、GitHub Desktop の GUI だけでコミットします。操作に迷ったら `docs/desktop-guide.md` を参照してください。
4. 変更をプッシュし、Pull Request テンプレートに沿って内容・確認方法を記載します。
5. Copilot の提案やレビューコメントを取り込み、Approve（承認）後にマージします。
6. GitHub Actions と GitHub Pages が正しく動き、README / FAQ 一覧が更新されるか確認します。

## FAQ 一覧（README 自動更新対象）

<!-- FAQ-LIST:START -->
- [プリンタで印刷できないときの基本手順](docs/faq/printer.md)
- [パソコンの電源が入らないときの基本手順](docs/faq/stop-pc.md)
- [Teams 会議に参加できないとき](docs/faq/teams.md)
- [VPN 接続ができないときのチェックリスト](docs/faq/vpn.md)
- [WiFi に接続できない場合の基本手順](docs/faq/wifi-connection-fail.md)
<!-- FAQ-LIST:END -->

## 関連リンク

- [ワークショップ構成案](./plan.md)
- [GitHub Desktop ガイド](docs/desktop-guide.md)
- [Copilot プロンプト集](docs/prompts.md)
- [CLI クイックリファレンス](docs/cli-cheatsheet.md)
- [Codespaces ガイド](docs/codespaces-guide.md)
- [Codespaces Prebuild チェックリスト](docs/codespaces-prebuild-checklist.md)
- [ワークショップ操作手順書](docs/workshop-operation.md)
- [サンプル Issue 一覧](docs/sample-issues)
- [Projects 定義 (JSON)](projects/helpdesk-refresh.json)

楽しみながら FAQ をリフレッシュしていきましょう！
