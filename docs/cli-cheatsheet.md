# CLI クイックリファレンス（初心者向け）

GitHub Desktop / Web がメインですが、ターミナル操作を試したい方向けに最小限のコマンドだけをまとめました。各コマンドの前に `git` や `gh`（GitHub CLI）を付けて実行します。わからない用語には補足を付けています。

## 1. リポジトリの取得と初期設定

```bash
# 自分のフォークを clone する（<your-name> を自分のアカウントに置き換え）
git clone https://github.com/<your-name>/helpdesk-faq-sample.git
cd helpdesk-faq-sample

# Git のユーザー名・メールを設定（初回だけ）
git config user.name "Your Name"
git config user.email "your.name@example.com"
```

> clone = リポジトリを手元にコピーすること。

## 2. Issue からブランチを作る

```bash
# main を最新にしてからブランチを作成
git checkout main
git pull origin main

git checkout -b issue-101-update-vpn-guide
```

- `checkout -b` は「新しいブランチを作って移動する」ショートカットです。

## 3. 変更内容をコミット→プッシュ

```bash
# 変更を確認
git status

# すべての変更をステージ（変更を記録する準備）
git add docs/faq/vpn.md

# コミット（変更履歴を作る）
git commit -m "docs: update VPN FAQ"

# GitHub へアップロード
git push -u origin issue-101-update-vpn-guide
```

- `-u` は次回以降の push が短くなるオプションです。

## 4. Issue / PR を CLI で作成（任意）

```bash
# GitHub CLI (gh) で Issue を作る
gh issue create --title "VPN エラー 619" --body-file docs/sample-issues/issue-101-vpn.md

# 現在のブランチから PR を作る
gh pr create --fill --base main --head issue-101-update-vpn-guide
```

- `--fill` を付けるとコミットメッセージなどから自動で本文を生成してくれます。

## 5. PR のチェックとマージ

```bash
# PR のステータス確認
gh pr status

# 差分をローカルで確認
gh pr checkout <PR番号>

# 承認してマージ（権限がある場合のみ）
gh pr review <PR番号> --approve
gh pr merge <PR番号> --merge
```

## 6. トラブル時のヒント

| 症状 | コマンド |
| --- | --- |
| ファイル変更をやり直したい | `git checkout -- <ファイル名>` （最新コミットに戻す） |
| 直前のコミットを修正したい | `git commit --amend`（GUI で難しい場合のみ推奨） |
| 余計なブランチを消したい | `git branch -d <ブランチ名>` / `git push origin --delete <ブランチ名>` |

> 迷ったときは GUI（GitHub Desktop）に戻るのが安全です。CLI はあくまで補助として活用してください。
