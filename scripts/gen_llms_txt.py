#!/usr/bin/env python3
"""Generate docs/llms.txt and docs/llms-full.txt (https://llmstxt.org).

llms.txt is an index (title, one-line summary, one link per page); llms-full.txt
is the whole book as plain markdown, for agents that want to read it in one go.
Both are build outputs: run this before mkdocs build, do not commit the results.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOK = json.loads((ROOT / "book.json").read_text(encoding="utf-8"))  # edition strings live here, not in code
TITLE, SUMMARY, SITE, RAW = BOOK["title"], BOOK["summary"], BOOK["site"], BOOK["raw"]
SECTIONS = [tuple(s) for s in BOOK["llms_sections"]]  # (heading, glob under docs/)
LABEL_SITE, LABEL_FULL = BOOK["llms_labels"]
DOCS = ROOT / "docs"


def title_and_blurb(md: str) -> tuple[str, str]:
    title, blurb = "", ""
    for line in md.splitlines():
        s = line.strip()
        if not title:
            if s.startswith("# "):
                title = s[2:].strip()
            continue
        if not s or line.startswith((" ", "\t")) or s.startswith(("!!!", "![", "---", "<!--", "|", "```", "#")):
            continue
        blurb = re.sub(r"[*_`>]", "", s).strip()
        blurb = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", blurb)
        break
    if len(blurb) > 200:  # cut at a word boundary so English blurbs do not end mid-word
        blurb = blurb[:200].rsplit(" ", 1)[0] if " " in blurb[:200] else blurb[:200]
    return title, blurb


def main() -> None:
    site_url = re.search(r"^site_url:\s*(\S+)", (ROOT / "mkdocs.yml").read_text(encoding="utf-8"), re.M).group(1)
    assert site_url == SITE, f"book.json site {SITE} != mkdocs.yml site_url {site_url}"
    index = [f"# {TITLE}", "", f"> {SUMMARY}", "",
             f"{LABEL_SITE}: {SITE}  ", f"{LABEL_FULL}: {SITE}llms-full.txt", ""]
    full = [f"# {TITLE}", "", f"> {SUMMARY}", ""]
    for heading, pattern in SECTIONS:
        files = sorted(DOCS.glob(pattern))
        if not files:
            continue
        index += [f"## {heading}", ""]
        for f in files:
            md = f.read_text(encoding="utf-8")
            md = re.sub(r"<!--.*?-->\n*", "", md, flags=re.S)
            title, blurb = title_and_blurb(md)
            rel = f.relative_to(DOCS).as_posix()
            index.append(f"- [{title}]({RAW}{rel}): {blurb}" if blurb else f"- [{title}]({RAW}{rel})")
            full += ["", "---", "", md.strip(), ""]
        index.append("")
    (DOCS / "llms.txt").write_text("\n".join(index).rstrip() + "\n", encoding="utf-8", newline="\n")
    (DOCS / "llms-full.txt").write_text("\n".join(full).rstrip() + "\n", encoding="utf-8", newline="\n")
    print(f"wrote docs/llms.txt ({sum(1 for l in index if l.startswith('- '))} pages) and docs/llms-full.txt")


if __name__ == "__main__":
    main()
