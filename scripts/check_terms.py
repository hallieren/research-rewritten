#!/usr/bin/env python3
"""Text gate for docs/, README.md and CONTRIBUTING.md. Rules switch on book.json "lang".
zh: no em dash outside term-gate/zh-emdash-allow.txt, no ??? collapsible blocks.
en: no em dash, no non-ASCII outside a small allowlist, no near-miss names (term-gate/en-banned.txt), no ??? blocks.
Usage: python3 scripts/check_terms.py [files...]; no args scans everything."""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GATE = os.path.join(ROOT, 'scripts', 'term-gate')
LANG = json.load(open(os.path.join(ROOT, 'book.json'), encoding='utf-8'))['lang']
TEXT_EXT = ('.md', '.svg')
EXCLUDE = ('llms.txt', 'llms-full.txt')

EM_DASH = re.compile(r'[—―]')
COLLAPSIBLE = re.compile(r'^\?\?\?\+? ')
NON_ASCII = re.compile(r'[^\x00-\x7f]')
# en dash (ranges), middot (H1 and Part titles), ellipsis, arrows, math and stat symbols, boxes, the three emoji of the companion block
EN_ALLOWED = set('–·…→↔×±≈≤≥≠ε†Δ₁₂−☐⬜📋🗂💻')


def load(name):
    p = os.path.join(GATE, name)
    return [l.strip() for l in open(p, encoding='utf-8') if l.strip() and not l.startswith('#')] if os.path.exists(p) else []


def check_zh(base, l, allow):
    out = []
    if base not in allow:
        out += [f'em dash U+{ord(m.group(0)):04X}' for m in EM_DASH.finditer(l)]
    return out


def check_en(base, l, banned):
    out = [f'em dash U+{ord(m.group(0)):04X}, rewrite with period, comma or parentheses' for m in EM_DASH.finditer(l)]
    out += [f"non-ASCII U+{ord(c):04X} '{c}'" for c in dict.fromkeys(NON_ASCII.findall(l))
            if c not in EN_ALLOWED and not EM_DASH.match(c)
            and not (0x2460 <= ord(c) <= 0x2473 or 0x2500 <= ord(c) <= 0x25FF)]  # circled digits, box drawing, shapes
    low = l.lower()
    out += [f'banned near-miss "{b}"' for b in banned if b.lower() in low]
    return out


def main():
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(ROOT, 'docs', '**', '*'), recursive=True)
                                   + [os.path.join(ROOT, 'README.md'), os.path.join(ROOT, 'CONTRIBUTING.md')])
    files = [p for p in files if os.path.isfile(p) and p.endswith(TEXT_EXT) and os.path.basename(p) not in EXCLUDE]
    allow, banned = load('zh-emdash-allow.txt'), load('en-banned.txt')
    bad = 0
    for path in files:
        base = os.path.basename(path)
        for i, l in enumerate(open(path, encoding='utf-8').read().split('\n'), 1):
            problems = check_zh(base, l, allow) if LANG == 'zh' else check_en(base, l, banned)
            if COLLAPSIBLE.match(l):
                problems.append('??? collapsible block, pymdownx.details is not enabled')
            for msg in problems:
                bad += 1
                print(f'{os.path.relpath(path, ROOT)}:{i}: {msg}  {l.strip()[:60]}')
    print(f'{"FAIL" if bad else "OK"}: {bad} problem(s)')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
