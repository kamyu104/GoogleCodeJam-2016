# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 1C - Problem A. Senate Evacuation
# https://code.google.com/codejam/contest/4314486/dashboard#s=p1
#
# Time:  O(PlogP)
# Space: O(P)
#

import heapq

def senate_evacuation():
    N = int(input())
    P = map(int, raw_input().strip().split())
    heap, res = [], []
    for i, n in enumerate(P):
        heapq.heappush(heap, (-n, chr(ord('A') + i)))

    while heap:
        if len(heap) >= 3:
            # Evacuating a single senator from the largest party.
            n1, p1 = heapq.heappop(heap)
            res.append(str(p1))
            if n1 + 1 != 0:
                heapq.heappush(heap, (n1 + 1, p1))
        else:
            if len(heap) == 2:
                # The two parties must have equal numbers of senators.
                # We can evacuate them in pairs.
                n1, p1 = heapq.heappop(heap)
                n2, p2 = heapq.heappop(heap)
                res.append(str(p1) + str(p2))
                if n1 + 1 != 0:
                    heapq.heappush(heap, (n1 + 1, p1))
                    heapq.heappush(heap, (n2 + 1, p2))
        
    return " ".join(res)


for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, senate_evacuation())
