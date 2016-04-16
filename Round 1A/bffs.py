# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 1A - Problem C. BFFs
# https://code.google.com/codejam/contest/4304486/dashboard#s=p2
#
# Time:  O(N)
# Space: O(N)
#

def BFFs():
    N = input()
    F = [int(c) - 1 for c in raw_input().strip().split()]

    length, to = [0] * N, [0] * N
    for i in xrange(N):
        used = set()
        u, l = i, 0
        while u not in used:
            l += 1
            used.add(u)
            u = F[u]
        length[i], to[i] = l, u

    longest = [0] * N
    for i in xrange(N):
        u = to[i]
        longest[u] = max(longest[u], length[i] - length[u])

    chains, cycle = 0, 0
    used = set()
    for i in xrange(N):
        if i in used or to[i] != i:
            continue;
        val = []
        u = i
        while u not in used:
            used.add(u)
            val.append(longest[u])
            u = F[u]
        if len(val) == 2:
            chains += val[0] + val[1] + 2
        cycle = max(cycle, len(val))
    return max(chains, cycle)


for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, BFFs())
