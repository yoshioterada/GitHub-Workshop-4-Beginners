# Codespaces 利用ガイド

GitHub Codespaces は、クラウド上で VS Code ベースの開発環境を数分で立ち上げられるサービスです。ローカル PC のセットアップが不安なときでも、同じ環境を全員で共有できます。

## 1. 起動手順

1. リポジトリ画面右上の **`<> Code`** ボタンをクリック。
2. `Codespaces` タブで `Create codespace on main` を選択。
3. 数十秒でブラウザ版 VS Code が開き、`.devcontainer/devcontainer.json` の設定に沿った環境が展開されます。
4. デスクトップ版 VS Code から利用したい場合は、左下の `リモート` アイコンから「Open in VS Code Desktop」を選びます。

> 事前に組織管理者へ Codespaces 利用権限（課金設定含む）が付与されているか確認してください。

## 2. devcontainer の構成

- **ベースイメージ**: `mcr.microsoft.com/devcontainers/universal:2` で Node.js / Python / Git などがあらかじめ入っています。
- **Features**: GitHub CLI / Azure CLI が追加済みなので、`gh` コマンドで Issue や PR を操作できます。
- **VS Code 拡張機能**: Copilot / Copilot Chat / Markdown All in One / Pull Requests など GUI 作業に役立つ拡張が自動で入ります。
- **forwardPorts**: 4173 番ポートを開放してあるため、簡易プレビューサーバーを起動したときブラウザから確認できます。

## 3. postCreateCommand で行っていること

`.devcontainer/post-create.sh` では次の処理を順番に実行します。

1. `npm install --global markdownlint-cli` で Markdown のチェックツールを導入。
2. `pip install -r requirements.txt`（ファイルがある場合のみ）で Python 依存を整備。
3. Git のユーザー名・メールが空の場合に暫定値をセット。
4. 最後に `markdownlint docs/**/*.md` を実行し、初期状態から lint エラーが出ないか確認します。

スクリプトの内容は必要に応じて編集できます。重い処理はここにまとめておくと Codespaces の起動が安定します。

## 4. Prebuild（事前ビルド）のすすめ

### 4.1 有効化手順（GitHub Web UI）

1. GitHub のリポジトリで `Settings > Codespaces > Prebuild configurations` を開きます。
2. `New configuration` をクリックし、以下を設定します。
    - **Branch**: `main`
    - **Region**: 参加者が最も多い地域（日本なら `East Asia` など）
    - **Machine type**: `4-core`（初期状態で十分）
3. `Trigger` では `On push` と `Scheduled (Daily)` を両方オンにし、`main` ブランチが常に最新になるようにします。
4. `Repositories access` はこのワークショップ用リポジトリのみに限定し、余計な課金を防ぎます。
5. `Create` を押すと初回 Prebuild が走るので、完了まで待機します。

### 4.2 検証フロー

1. `Codespaces > Prebuild configurations` の一覧で `Status: Succeeded` になっているか確認。
2. 任意の参加者アカウントで `Code > Codespaces > Create codespace on main` を実行し、起動時間が 1 分以内か計測。
3. `/.devcontainer/post-create.sh` のログをターミナルで確認し、エラーがなければ成功です。
4. 失敗した場合は `View logs` から該当ステップを確認し、依存ライブラリやキャッシュを更新します。

### 4.3 参加者への周知

- Prebuild が有効だと、初回起動時の `Installing...` がほぼスキップされることを説明し、安心感を与えます。
- `docs/codespaces-prebuild-checklist.md` に手順をまとめているので、当日のサポート担当は参照してください。

## 5. よくあるトラブルと対処

| 症状 | 対処 |
| --- | --- |
| 起動が 10 分以上進まない | Prebuild が失敗している可能性があります。`Codespaces > Prebuild` のログを確認し、再作成してください。 |
| `postCreate` で npm エラー | npm キャッシュが壊れている場合があるので `npm cache clean --force` を実行後、再度 `Codespaces > Rebuild Container` を試します。 |
| Copilot が動かない | 組織ポリシーで Copilot が無効の場合があります。`Help > GitHub Copilot > Sign in` を押し、ブラウザで承認してください。 |

## 6. 片付け（リソース節約）

- 作業終了後は Codespaces タブで `Stop codespace` を押すと、課金が止まります。
- 完全に不要になった場合は `Delete` を選び、ストレージも開放してください。

このガイドに沿って準備すれば、ワークショップ開始前に同じ開発体験を全員へ提供できます。
