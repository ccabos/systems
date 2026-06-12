#!/usr/bin/env python3
"""Rewrite plain-text `knowledge/...` paths in the book's docs into clickable
GitHub URLs.

Why: 53 references to the knowledge/ tree exist in projects/systems-introduction-book/docs/
but none of them are clickable. The knowledge/ tree is outside the MkDocs
site root, so we can't link relatively; absolute GitHub URLs are what the
rest of the book already uses (see ai-stpa.md's link to projects/problems/...).

Rule:
  `knowledge/foo/bar.md`   →  [`knowledge/foo/bar.md`](https://github.com/.../blob/main/knowledge/foo/bar.md)
  `knowledge/foo/`         →  [`knowledge/foo/`](https://github.com/.../tree/main/knowledge/foo/)
  `knowledge/foo`          →  [`knowledge/foo`](https://github.com/.../tree/main/knowledge/foo)
"""
import re
import sys
from pathlib import Path

DOCS = Path("projects/systems-introduction-book/docs")
REPO = "https://github.com/ccabos/systems"

# Inline code containing a knowledge/ path. We anchor on backticks because
# every existing reference is wrapped in them — so this is safe.
PATTERN = re.compile(r"(?<!\]\()`(knowledge/[^`]+)`")


def to_url(path: str) -> str:
    if path.endswith(".md"):
        return f"{REPO}/blob/main/{path}"
    return f"{REPO}/tree/main/{path.rstrip('/')}"


def rewrite(text: str) -> tuple[str, int]:
    count = 0

    def sub(m: re.Match) -> str:
        nonlocal count
        path = m.group(1)
        count += 1
        return f"[`{path}`]({to_url(path)})"

    return PATTERN.sub(sub, text), count


def main() -> int:
    total = 0
    touched = 0
    for md in DOCS.rglob("*.md"):
        original = md.read_text()
        rewritten, n = rewrite(original)
        if n:
            md.write_text(rewritten)
            total += n
            touched += 1
            print(f"  {md.relative_to(DOCS)}  ({n} link{'s' if n != 1 else ''})")
    print(f"\nRewrote {total} references across {touched} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
