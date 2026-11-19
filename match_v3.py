# Head-to-head: v2 engine vs v1 engine, alternating colours, practice openings.
import importlib.util, json, math, os, sys, time

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

V1 = load('v1', os.path.expanduser('~/workspace/makefun/bounties/tiny-chess-01/engine.py'))
V2 = load('v2', os.path.expanduser('~/workspace/makefun/bounties/tiny-chess-01-v3/engine.py'))
KIT = os.path.expanduser('~/workspace/makefun/tiny-chess-01-kit/tiny-chess-01-kit')

def openings():
    out = []
    for t in (0, 1, 2):
        g = json.load(open(f'{KIT}/practice/trial-{t}/input/env/gauntlet.json'))
        for game in g['games']:
            out.append(game['opening']['moves'])
    return out

OPENINGS = openings()
START = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

def material(e):
    s = 0
    for p in e.b:
        if p: s += (1 if p > 0 else -1) * [0, 1, 3, 3, 5, 9, 0][abs(p)]
    return s

def play_game(opening, nodes_v3, nodes_v1, v3_white):
    # board: v2 engine drives legality/adjudication; two side engines stay in sync.
    board = V2.Engine()
    eng_w = (V2.Engine() if v3_white else V1.Engine())
    eng_b = (V1.Engine() if v3_white else V2.Engine())
    nodes_w = nodes_v3 if v3_white else nodes_v1
    nodes_b = nodes_v1 if v3_white else nodes_v3
    board.fen(START); eng_w.fen(START); eng_b.fen(START)
    counts = {}
    def apply_all(uci):
        for e, mod in ((board, V2), (eng_w, V2 if v3_white else V1), (eng_b, V1 if v3_white else V2)):
            m = mod.pu(e, uci)
            assert m is not None, f'illegal {uci}'
            e.mk(m); e.y.append(e.ky()); e.z.add(e.y[-1])
    for u in opening:
        apply_all(u)
        counts[board.ky()] = counts.get(board.ky(), 0) + 1
    plies = 8
    while plies < 200:
        moves = board.lg()
        side = board.s
        if not moves:
            if board.at(board.w if side>0 else board.v, -side):
                return (1.0 if side < 0 else 0.0, plies, 'mate')
            return (0.5, plies, 'stalemate')
        k = board.ky()
        counts[k] = counts.get(k, 0) + 1
        if counts[k] >= 3:
            return (0.5, plies, 'repetition')
        if board.h >= 100:
            return (0.5, plies, 'fifty')
        eng = eng_w if side > 0 else eng_b
        nodes = nodes_w if side > 0 else nodes_b
        before = eng.ky()
        m = eng.bm(nodes)
        assert eng.ky() == before, 'board corrupted by search'
        if m is None:
            return (0.5, plies, 'no-move')
        u = (V2.uc if (side > 0) == v3_white else V1.uc)(m)
        apply_all(u)
        plies += 1
    mat = material(board)
    if mat >= 5: return (1.0, plies, 'adjudication')
    if mat <= -5: return (0.0, plies, 'adjudication')
    return (0.5, plies, 'adjudication-draw')

if __name__ == '__main__':
    nodes_v3 = int(sys.argv[1]); nodes_v1 = int(sys.argv[2])
    worker = int(sys.argv[3]); nworkers = int(sys.argv[4])
    rounds = int(sys.argv[5]) if len(sys.argv) > 5 else 3
    # game list: rounds x openings x colours
    games = []
    for r in range(rounds):
        for i, op in enumerate(OPENINGS):
            games.append((r, i, True)); games.append((r, i, False))
    mine = [g for j, g in enumerate(games) if j % nworkers == worker]
    out = open(f'match_v3_{nodes_v3}_vs_v1_{nodes_v1}_w{worker}.jsonl', 'a')
    score = 0.0
    for (r, i, v3w) in mine:
        t0 = time.time()
        res, plies, why = play_game(OPENINGS[i], nodes_v3, nodes_v1, v3w)
        v3pts = res if v3w else 1.0 - res
        score += v3pts
        rec = {'round': r, 'opening': i, 'v3_white': v3w, 'v3pts': v3pts,
               'plies': plies, 'why': why, 'secs': round(time.time() - t0, 1)}
        out.write(json.dumps(rec) + '\n'); out.flush()
        print(f'w{worker} r{r} op{i} v2{"W" if v3w else "B"}: {v3pts} ({why}, {plies} plies, {rec["secs"]}s) cum {score}', flush=True)
    print(f'worker {worker} done: v2 score {score}/{len(mine)}')
