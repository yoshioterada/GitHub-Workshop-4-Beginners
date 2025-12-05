# Codespaces Prebuild Checklist

このチェックリストは、ワークショップ前に Codespaces の事前ビルド（Prebuild）を確実に整備するためのものです。GitHub リポジトリの設定画面での操作が中心になるため、オーナー権限を持つメンバーが実施してください。

## 1. 前提条件

- リポジトリに `.devcontainer/devcontainer.json` と `post-create.sh` が存在し、ローカルで正しく動作している。
- GitHub Actions 等の CI が直近で成功している。
- 事前ビルドに使うブランチ（通常 `main`）が常に最新である。

## 2. Prebuild 設定手順

1. GitHub で対象リポジトリを開き、`Settings > Codespaces > Prebuild configurations` に移動。
2. `New configuration` をクリックし、以下を設定。
   - Branch: `main`
   - Region: 参加者が最も多い地域（例: East Asia）
   - Machine type: 4-core
   - Trigger: `On push` と `Scheduled (Daily)` を有効化
3. `Create` をクリックし、初回ビルドが完了するまで待機。
4. `View logs` から `post-create.sh` を含む各ステップでエラーがないか確認。

## 3. 動作検証

1. Prebuild 一覧で `Status: Succeeded` を確認。
2. 新しい Codespace を `main` ブランチで作成し、1 分以内に起動するか計測。
3. Devcontainer 起動後に `npm test` や `python scripts/update_readme.py` などの代表的なコマンドを試し、依存関係が揃っているか確認。
4. 問題があれば `.devcontainer/post-create.sh` を修正し、`Prebuilds > Rebuild now` を実行。

## 4. トラブルシューティング

- **ビルドが失敗する**: `View logs` で失敗ステージを特定し、依存パッケージのインストールや環境変数設定を見直す。
- **時間がかかる**: `node_modules` や `venv` など大きなキャッシュがある場合、`.devcontainer` の `customizations` で不要ディレクトリを除外。
- **参加者の起動が遅い**: 対象地域の Prebuild を別途追加するか、より高性能なマシンタイプを検討。

## 5. 当日運用メモ

- 開始 24 時間前に `Codespaces > Prebuild configurations` の `Last run` が最新か確認。
- もし Prebuild が止まっていたら `Rebuild now` を押しておく。
- 参加者へは「Prebuild 済み Codespace を使うので、初回起動でも 1 分以内です」と案内し、安心させる。

## 6. 設定完了の記録

- `TODO.md` などの運営用チェックリストに「Prebuild 設定済み／日付／担当者」を記入。
- 設定方法を他のメンバーに共有するため、このドキュメントのリンクを貼っておく。
