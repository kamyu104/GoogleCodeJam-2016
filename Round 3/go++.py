# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 3 - Problem D. Go++
# https://code.google.com/codejam/contest/3224486/dashboard#s=p3
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
        # Because executing each matchable pair of ("10", "1?") and ("01", "0?")
        # could result in either 1 or 0, the written P1 and P2 produce a set of
        # all possible strings consisting of 0s and/or 1s.
        if c == '0':
            P1 += "10",
            P2 += "1?",
        else:
            P1 += "01",
            P2 += "0?",
    # Remove the last "01"/"10" of P1 to reduce the count of matchable 0s and 1s by one.
    # It could still produce a set of all possible strings consisting of 0s and/or 1s
    # except for B because the count of matchable 0s/1s is not enough to make.
    P1.pop()

    return "".join(P1) + " " + "".join(P2)


for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, gopp())
