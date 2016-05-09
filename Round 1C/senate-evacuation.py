# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 1C - Problem A. Senate Evacuation
# https://code.google.com/codejam/contest/4314486/dashboard#s=p1
#
# Time:  O(PlogP)
# Space: O(P)
#

from heapq import heappush, heappop

def senate_evacuation():
    N = int(input())
    P = map(int, raw_input().strip().split())
    heap, res = [], []
    for i, n in enumerate(P):
        heappush(heap, (-n, chr(ord('A') + i)))

    while heap:
        if len(heap) >= 3:
            # Evacuating a single senator from the largest party.
            n1, p1 = heappop(heap)
            res.append(str(p1))
            if n1 + 1 != 0:
                heappush(heap, (n1 + 1, p1))
        else:
            # The last two parties must have equal numbers of senators.
            # We can evacuate them in pairs.
            n1, p1 = heappop(heap)
            n2, p2 = heappop(heap)
            res.append(str(p1) + str(p2))
            if n1 + 1 != 0:
                heappush(heap, (n1 + 1, p1))
                heappush(heap, (n2 + 1, p2))
        
    return " ".join(res)


for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, senate_evacuation())
