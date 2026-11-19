import sys, time, random
sys.path.insert(0, '/home/hatch/workspace/makefun/bounties/tiny-chess-01-v3')
import engine as E

# table lengths
for a in range(1, 7):
    assert len(E.PM[a]) == 64, (a, len(E.PM[a]))
    assert len(E.PE[a]) == 64, (a, len(E.PE[a]))
for a in (2, 3, 4, 5):
    assert E.PM[a] == E.PE[a], a
print('tables ok')

def perft(e, d):
    if d == 0:
        return 1
    n = 0
    for m in e.lg():
        u = e.mk(m)
        n += perft(e, d - 1)
        e.un(m, u)
    return n

e = E.Engine()
for d, want in ((1, 20), (2, 400), (3, 8902)):
    got = perft(e, d)
    print('startpos perft', d, got, 'want', want, 'OK' if got == want else 'FAIL')
    assert got == want
e.fen('r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1')
print('kiwipete perft3', perft(e, 3), 'want 97862')
assert perft(E.Engine(), 0) == 1
e.fen('8/2p5/3p4/KP5r/1R3p1k/8/4P1P1/8 w - - 0 1')
print('pos3 perft3', perft(e, 3), 'want 2812')

# mk/un roundtrip: board, eval, hash, phase, counts must restore exactly
random.seed(1)
for trial in range(3):
    e = E.Engine()
    e.fen('r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1')
    for step in range(200):
        ms = e.lg()
        if not ms:
            break
        m = random.choice(ms)
        snap = (e.b[:], e.s, e.c, e.e, e.h, e.w, e.v, e.mg, e.eg, e.ph, e.zh, e.ev())
        u = e.mk(m)
        e.un(m, u)
        now = (e.b[:], e.s, e.c, e.e, e.h, e.w, e.v, e.mg, e.eg, e.ph, e.zh, e.ev())
        assert snap == now, ('roundtrip fail', trial, step, E.uc(m))
        # also make the move for real half the time
        if step % 2 == 0:
            e.mk(m)
    print('roundtrip trial', trial, 'ok')

# eval sanity: startpos ~0; white up a knight should be ~+337ish
e = E.Engine()
print('start ev', e.ev())
e.fen('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
print('start ev2', e.ev())
e.fen('4k3/8/8/8/8/8/8/4K2N w - - 0 1')
print('WN vs bare ev (expect ~337+PST)', e.ev())
e.fen('rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2')
print('after e4 e5 ev', e.ev())

# speed bench
for fen in ('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1',
            'r1bqk2r/pppp1ppp/2n2n2/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 4 4',
            'r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1'):
    e = E.Engine(); e.fen(fen)
    t0 = time.time(); m = e.bm(100000); dt = time.time() - t0
    print('bench 100k nodes: %.2fs -> %d nps, move %s' % (dt, 100000 / max(dt, 1e-9), E.uc(m)))
print('ALL OK')
