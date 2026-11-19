#!/usr/bin/env python3
"""Pack engine.py into main.py (<=4096 bytes) using lzma FORMAT_ALONE + latin-1 literal."""
import lzma, sys

src = open('engine.py', 'rb').read()
blob = lzma.compress(src, format=lzma.FORMAT_ALONE, preset=9 | lzma.PRESET_EXTREME)
print('engine bytes:', len(src), 'lzma blob:', len(blob))

def esc_sq(b):
    # single-quoted latin-1 literal, escape \ ' \n \r \x00 (v1 pattern)
    out = []
    for ch in b:
        if ch == 0x5C: out.append('\\\\')
        elif ch == 0x27: out.append("\\'")
        elif ch == 0x0A: out.append('\\n')
        elif ch == 0x0D: out.append('\\r')
        elif ch == 0x00: out.append('\\x00')
        else: out.append(chr(ch))
    return ''.join(out)

def esc_tq(b):
    # triple-single-quoted literal: escape backslash, NUL, CR, and quotes.
    # NUL -> \0 (or \x00 if next byte is an octal digit, else \0 would swallow it)
    out = []
    for i, ch in enumerate(b):
        if ch == 0x5C: out.append('\\\\')
        elif ch == 0x00:
            nxt = b[i+1] if i+1 < len(b) else None
            out.append('\\x00' if nxt is not None and 0x30 <= nxt <= 0x37 else '\\0')
        elif ch == 0x0D: out.append('\\r')
        elif ch == 0x27: out.append("\\'")
        else: out.append(chr(ch))
    return ''.join(out)

hdr = "#coding:l1\nimport lzma;exec(lzma.decompress("
cands = {
    'single': hdr + "'" + esc_sq(blob) + "'.encode('l1')))\n",
    'triple': hdr + "'''" + esc_tq(blob) + "'''.encode('l1')))\n",
}
best = min(cands.items(), key=lambda kv: len(kv[1]))
print('single-quote packed:', len(cands['single']), 'triple-quote packed:', len(cands['triple']))
print('chosen:', best[0], len(best[1]))
if len(best[1]) > 4096:
    print('OVER BUDGET by', len(best[1]) - 4096)
    sys.exit(1)
open('main.py', 'w', encoding='latin-1').write(best[1])
print('wrote main.py', len(best[1]), 'bytes')
