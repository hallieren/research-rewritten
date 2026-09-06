#!/usr/bin/env bash
# Build the whole-book EPUB (18 chapters, 17 template pages, the experiment ledger) for offline reading. Requires pandoc.
# Title, author, language and output name come from book.json.
set -euo pipefail
cd "$(dirname "$0")/.."
meta() { python3 -c 'import json,sys;print(json.load(open("book.json"))[sys.argv[1]])' "$1"; }
mkdir -p build
chapters=(docs/chapters/ch-preface.md docs/chapters/ch00-start-here.md)
for i in 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16; do
  chapters+=("docs/chapters/ch${i}.md")
done
chapters+=(docs/appendices/template-index.md)
for i in 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16; do
  chapters+=("docs/appendices/ch${i}-templates.md")
done
chapters+=(docs/experiments.md)
out="build/$(meta slug).epub"
pandoc "${chapters[@]}" \
  --metadata title="$(meta epub_title)" \
  --metadata author="$(meta author)" --metadata lang="$(meta epub_lang)" \
  --toc --toc-depth=2 --resource-path=docs:docs/chapters:docs/appendices \
  -o "$out"
echo "OK: $out"
