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

    lengths =[0] * N  # lengths[i] denotes the max length from the kid i
    to = [0] * N      # to[i] denotes the index of the first kid in
                      # the circle from the kid i
    for i in xrange(N):
        used = set()
        cur, length = i, 0
        while cur not in used:
            length += 1
            used.add(cur)
            cur = F[cur]
        lengths[i], to[i] = length, cur

    longest = [0] * N  # longest[i] denotes the max length ends with the kid i.
    for i in xrange(N):
        cur = to[i]
        longest[cur] = max(longest[cur], lengths[i] - lengths[cur])

    chains, circle = 0, 0
    used = set()
    for i in xrange(N):
        if i not in used and to[i] == i:  # Only check an unused kid in a circle.
            # Count the length of the circle and mark the kids in it as used.
            vals, cur = [], i
            while cur not in used:
                used.add(cur)
                vals.append(longest[cur])
                cur = F[cur]

            # Type 1: update the max length of the 2 chains
            #         connected with a circle of which length is 2.
            if len(vals) == 2:
                chains += vals[0] + vals[1] + 2

            # Type 2: update the max length of the circle.
            circle = max(circle, len(vals))

    return max(chains, circle)


for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, BFFs())
