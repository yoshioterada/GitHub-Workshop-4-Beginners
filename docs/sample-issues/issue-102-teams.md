# サンプル Issue 102: Teams 音声が出ない

- **テンプレート**: `Helpdesk Ticket`
- **SLA**: Medium (3 営業日以内)
- **Projects**: `HelpDesk Refresh Board` > 列「未着手」 / 優先度: Medium / 期限: 2025-12-12 / Slack 通知: 不要

## 入力例

| フィールド | 記入例 |
| --- | --- |
| タイトル | Teams 会議で音声が聞こえない |
| 再現手順 | 1. Outlook から会議リンクをクリック  2. ブラウザで参加  3. デバイスが「既定」になり音が出ない |
| 期待する結果 | FAQ でデバイス選択とテスト通話方法がわかる |
| SLA | Medium |
| 添付リンク | Teams 録画: `https://contoso.sharepoint.com/.../teams-audio.mp4` |

## Projects 連携メモ

```text
projects/helpdesk-refresh.json
  -> cardId: 9002
  -> column: 未着手
  -> fields:
       - 優先度: Medium
       - 期限: 2025-12-12
       - Slack 通知要否: false
```

## 次のアクション

- [ ] `docs/faq/teams.md` にテスト通話手順の動画リンクを追加
- [ ] `assets/images/teams-join.svg` を Issue に貼り付け
- [ ] 完了後に Projects 列を「レビュー」へ移動
