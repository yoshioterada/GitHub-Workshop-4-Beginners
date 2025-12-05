# GitHub Desktop 操作ガイド（初心者向け）

GitHub Desktop は、コマンドを使わずにブランチの作成やコミット、プッシュができる公式アプリです。ここではワークショップで必要な操作だけをまとめました。専門用語には補足を入れているので、初めて触る方でも安心してください。

## 1. 画面構成のおさらい

- 左上: **Current Repository**（現在開いているリポジトリ）と **Current Branch**（作業中の枝）。
- 左側: ステータス欄。変更されたファイルが一覧で表示されます。
- 右側: 選択したファイルの差分プレビュー。
- 下部: コミットメッセージ入力欄と `Commit to <branch>` ボタン。

## 2. 基本フロー（Issue から PR まで）

1. **フォルダを開く**  
   GitHub Desktop のメニュー `File > Open` からローカルに clone 済みの `helpdesk-faq-sample` を選びます。
2. **ブランチを切り替える / 作成する**  
   画面上部の `Current Branch` をクリックし、`Choose a branch to merge into` から `issue-xxx` を選択。存在しない場合は `New Branch` で作成し、`Create branch based on:` を `main` にしておきます。
3. **ファイルを編集**  
   `Open in Visual Studio Code` ボタンで VS Code を開き、`docs/faq/` など該当ファイルを編集します。
4. **変更を確認する**  
   Desktop に戻ると変更ファイルが左側に表示されます。チェックボックスにチェックを入れるとコミット対象になります。
5. **コミットする**  
   下部の `Summary` に「#101 VPN 手順を更新」のように短く書き、`Description` に補足を入れたら `Commit to <branch>` をクリック。
6. **Push（プッシュ）する**  
   上部バーに `Push origin` ボタンが出るので押します。Push とはローカルの変更を GitHub に送ることです。
7. **Pull Request を作成**  
   Push 後に表示される `Create Pull Request` ボタンを押すとブラウザが開き、PR テンプレートに沿って内容を入力できます。

## 3. 便利な補助機能

- **Discard changes**（変更を戻す）: ファイルを選択し、右クリック > `Discard Changes`。誤編集をなかったことにできます。
- **History タブ**: 過去のコミット一覧。ダブルクリックで差分を確認できます。
- **Repository > Repository Settings...**: `Default branch for new pull requests` を設定しておくと PR の向き先を間違えにくくなります。

## 4. よくあるつまずき

| 症状 | 解決策 |
| --- | --- |
| `Push origin` ボタンがグレーのまま | まだコミットがない可能性があります。`Changes` タブでコミットしてください。 |
| 想定外のファイルまでコミットしそう | コミット前に左側リストから不要ファイルのチェックを外してください。 |
| ブランチ名を間違えた | `Branch > Rename <branch>` で後から修正できます。 |
| main ブランチの最新が欲しい | `Branch > Merge into Current Branch...` で `main` を選ぶと最新変更を取り込めます。 |

## 5. 次の一歩

- Pull（プル）と Fetch（フェッチ）の違いを掘り下げたい方は `Help > GitHub Desktop Help` を参照。
- CLI（コマンドライン）も試したい場合は `docs/cli-cheatsheet.md` に補足を用意予定です。
