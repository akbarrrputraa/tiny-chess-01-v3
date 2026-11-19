# tiny-chess-01 v3

PeSTO tapered-eval alpha-beta chess engine for the make.fun tiny-chess-01
competition (harness agent/v1). Entry fee $0. Authored from scratch for this
entry (v1/v2 read as reference only).

## Files

- `main.py` — the submission: LZMA-compressed engine in a latin-1
  triple-quoted literal, **4,077 bytes** (limit 4,096).
- `engine.py` — the readable engine source (13,600 bytes).
- `pack.py` — builds `main.py` from `engine.py`
  (LZMA `FORMAT_ALONE`, preset 9|EXTREME; escapes only NUL/CR/backslash/
  quote bytes, which raw latin-1 source cannot carry).
- `test_engine.py` — perft / make-unmake round-trip / eval / bench tests.
- `match_v3.py` — head-to-head harness (v3 vs v1, 18 practice openings x2).

## Engine

- 0x88 board, int-encoded moves (`f | t<<7 | promo<<14`).
- Incremental tapered **PeSTO** eval: material 82/337/365/477/1025,
  mg/eg piece-square tables (values stored offset by +64 in bytes),
  phase weights N/B=1, R=2, Q=4 (total 24). No bishop-pair term
  (dropped for the size budget; ~80 compressed bytes).
- Incremental Zobrist hash (`random.Random(20261119)`), transposition
  table (dict, mate-score ply adjustment, cleared above 500k entries).
- PVS-style alpha-beta + **LMR** (depth>=3, move>=3, quiet, not in check:
  reduced depth-2, re-search if > alpha), 2 killers/ply, MVV-LVA captures.
  **No history heuristic** (dropped for the size budget; ~75 bytes).
- Quiescence search: stand-pat, captures + promotions only; full
  evasions + mate detection when in check. Check extension (+1 depth).
- Iterative deepening to depth 64 with a node-budget exception.
- Node budget **N = 120,000** (~2.3 s/move at ~51k NPS clean; chosen
  below the 10 s/move limit with margin — v1 lost games on time at 80k).
- No null-move pruning, no delta pruning (both measured <= v1 in v2's
  ablations; not repeated here).

## Validation (2026-11-19)

- Correctness: perft startpos 20/400/8902, Kiwipete perft3 97,862,
  pos3 perft3 2,812; make/unmake round-trip exact (board, eval, hash,
  phase) over 3x200 random moves; packed `main.py` verified identical
  (perft 8902, bench move b1c3).
- Head-to-head vs v1 (equal 80k nodes, 18 openings x2, 36 games):
  after 6 games v3 3.5/6 (W3 D1 L2, 58%) — in progress.
- Local gauntlet (kit practice trials, 6 games vs house ladder):
  trial-0: **Elo 1279, 3W 0D 3L, spare 244** (beat depth-2/3/4, lost
  nodes-100k/250k/500k). Trial-1: **Elo 1279, 3W 0D 3L, spare 264**
  (beat depth-2/3 + nodes-100k, lost depth-4 + nodes-250k/500k).
  0 time losses in both. Same Elo as v1's local trial-0 (1279);
  trial-2 in progress.

## Size budget

`engine.py` 13,600 B -> LZMA alone/extreme 3,948 B -> `main.py` 4,077 B.
Cuts made to fit, in order: piece-list `occ` machinery (NPS-neutral,
~180 B), fused table builder, path-repetition dict, `ks()` helper,
bishop-pair eval, history heuristic, table comment, exit message.
Kept: QS, TT, LMR, PeSTO mg/eg tables, check extension, killers.
