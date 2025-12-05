# `update-readme` ワークフロー検証手順

ローカル環境では GitHub Actions を実行できないため、以下の手順でクラウド（GitHub ホストランナー）上で一度実行してください。

1. `main` ブランチに最新の変更を push する。
2. GitHub 上でリポジトリを開き、`Actions` タブ → `Update README` ワークフローを選択。
3. 右上の **Run workflow** をクリックし、`main` を指定して手動実行（`workflow_dispatch`）。
4. 実行ログで以下を確認:
   - `runs-on: ubuntu-latest` が表示され、Self-hosted でないこと。
   - `python scripts/update_readme.py` ステップが成功し、差分がない場合は "README の FAQ 一覧を更新する必要があります" が出ていないこと。
   - `Auto commit changes` ステップがスキップ or 正常終了していること。
5. `main` へ push 後に自動実行されるシナリオも確認したい場合は、`docs/faq/*.md` を編集し push → ワークフロー実行結果を確認する。
6. すべて成功したら、このファイルに実行日時と結果を追記して記録する。

例:

```text
- 2025-12-05 14:20 JST: 手動実行 OK（ubuntu-latest）。差分なし。
```
