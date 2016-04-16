# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 1A - Problem C. BFFs
# https://code.google.com/codejam/contest/4304486/dashboard#s=p2
#
# Time:  O(N^2)
# Space: O(N)
#

def BFFs():
    N = input()
    F = [int(c) - 1 for c in raw_input().strip().split()]

    length =[0] * N  # length[i] denotes the max length from the kid i
    to = [0] * N     # to[i] denotes the index of the last kid from the kid i
    for i in xrange(N):
        used = set()
        cur, l = i, 0
        while cur not in used:
            l += 1
            used.add(cur)
            cur = F[cur]
        length[i], to[i] = l, cur

    longest = [0] * N
    for i in xrange(N):
        cur = to[i]
        longest[cur] = max(longest[cur], length[i] - length[cur])

    chains, circle = 0, 0
    used = set()
    for i in xrange(N):
        if i in used or to[i] != i:
            continue;
        val = []
        cur = i
        while cur not in used:
            used.add(cur)
            val.append(longest[cur])
            cur = F[cur]
        if len(val) == 2:
            chains += val[0] + val[1] + 2
        circle = max(circle, len(val))
    return max(chains, circle)


for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, BFFs())
