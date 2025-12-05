# サンプル Issue 101: VPN エラー 619 対応

- **テンプレート**: `Helpdesk Ticket`
- **SLA**: High (本日中)
- **Projects**: `HelpDesk Refresh Board` > 列「作業中」 / 優先度: High / 期限: 2025-12-07 / Slack 通知: 要

## 入力例

| フィールド | 記入例 |
| --- | --- |
| タイトル | VPN エラー 619 が出て接続できない |
| 再現手順 | 1. 社外 Wi-Fi から VPN クライアント起動  2. ワンタイムパスワードを入力  3. エラー 619 |
| 期待する結果 | FAQ で接続前チェックとエラー一覧を確認できる |
| SLA | High |
| 添付リンク | OneDrive: `https://example.sharepoint.com/.../vpn-error.mp4` |

## Projects 連携メモ

```text
projects/helpdesk-refresh.json
  -> cardId: 9001
  -> column: 作業中
  -> fields:
       - 優先度: High
       - 期限: 2025-12-07
       - Slack 通知要否: true
```

## 次のアクション

- [ ] `docs/faq/vpn.md` にエラーコード表を追加
- [ ] `assets/images/vpn-status.svg` を Issue へ貼り付け
- [ ] PR #201 でレビュー依頼
