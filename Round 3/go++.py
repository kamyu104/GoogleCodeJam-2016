# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 3 - Problem D. Go++
# https://code.google.com/codejam/contest/3224486/dashboard#s=p4
#
# Time:  O(L)
# Space: O(L)
#

def gopp():
    N, L = map(int, raw_input().strip().split())
    G = raw_input().strip().split()
    B = raw_input().strip()

    if B in G:
        return "IMPOSSIBLE"

    if L == 1:
        if B == "0":
            return "1 1?"
        else:
            return "0 0?"

    P1, P2 = [], []
    for c in B:
        if c == '0':
            P1 += "10",
            P2 += "1?",
        else:
            P1 += "01",
            P2 += "0?",
    P1.pop()
    return "".join(P1) + " " + "".join(P2)


for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, gopp())
