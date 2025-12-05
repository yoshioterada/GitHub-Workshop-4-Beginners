# サンプル Issue 103: プリンタ紙詰まり FAQ 追加

- **テンプレート**: `Helpdesk Ticket`
- **SLA**: Low (1 週間以内)
- **Projects**: `HelpDesk Refresh Board` > 列「レビュー」 / 優先度: Low / 期限: 2025-12-18 / Slack 通知: 不要

## 入力例

| フィールド | 記入例 |
| --- | --- |
| タイトル | 共有プリンタ PRN-B2 の紙詰まり FAQ を追記したい |
| 再現手順 | 1. 月次会計資料を印刷  2. トレイ 2 で紙詰まり  3. 再起動しても解除できない |
| 期待する結果 | FAQ で `PAPER JAM` 表示時の写真と対処が見られる |
| SLA | Low |
| 添付リンク | 参考画像: `https://contoso.sharepoint.com/.../printer-jam.jpg` |

## Projects 連携メモ

```text
projects/helpdesk-refresh.json
  -> cardId: 9003
  -> column: レビュー
  -> fields:
       - 優先度: Low
       - 期限: 2025-12-18
       - Slack 通知要否: false
```

## 次のアクション

- [ ] `docs/faq/printer.md` に `assets/images/printer-panel.svg` を参照する説明を追記（済）
- [ ] PR #205 のレビューコメントに沿って表現を調整
- [ ] Projects で列「公開済み」に移動し、Issue を close
