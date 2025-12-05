#!/usr/bin/env python3
"""docs/faq/ 以下のファイルから README の FAQ 一覧を自動生成するスクリプト。"""
from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
README_PATH = REPO_ROOT / "README.md"
FAQ_DIR = REPO_ROOT / "docs" / "faq"
START_TAG = "<!-- FAQ-LIST:START -->"
END_TAG = "<!-- FAQ-LIST:END -->"


def extract_title(md_path: Path) -> str:
    for line in md_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("# ")
    return md_path.stem


def build_block() -> str:
    items: list[str] = []
    for md_file in sorted(FAQ_DIR.glob("*.md")):
        title = extract_title(md_file)
        rel_path = md_file.relative_to(REPO_ROOT).as_posix()
        items.append(f"- [{title}]({rel_path})")
    body = "\n".join(items) if items else "- FAQ はまだ追加されていません"
    return f"{START_TAG}\n{body}\n{END_TAG}\n"


def main() -> None:
    faq_block = build_block()
    content = README_PATH.read_text(encoding="utf-8")
    if START_TAG in content and END_TAG in content:
        pattern = re.compile(
            rf"{START_TAG}.*?{END_TAG}\n?",
            flags=re.DOTALL,
        )
        new_content = pattern.sub(faq_block, content)
    else:
        new_content = content.strip() + "\n\n## FAQ 一覧\n\n" + faq_block
    README_PATH.write_text(new_content, encoding="utf-8")


if __name__ == "__main__":
    main()
