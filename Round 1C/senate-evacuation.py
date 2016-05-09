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

    # Try to get the top 3 parties (n1, n2, n3)
    while heap:
        n1, p1 = heappop(heap)
        if heap:
            n2, p2 = heappop(heap)
            if n1 == n2:
                if heap:
                    n3, p3 = heappop(heap)
                    if n2 == n3:
                        # Evacuate the top 1 party if n1 = n2 = n3
                        res.append(str(p1))
                        if n1 + 1 != 0:
                            heappush(heap, (n1 + 1, p1))
                        heappush(heap, (n2, p2))
                        heappush(heap, (n3, p3))
                    else:
                        # Evacuate the top 2 parties if n1 = n2 > n3
                        res.append(str(p1) + str(p2))
                        if n1 + 1 != 0:
                            heappush(heap, (n1 + 1, p1))
                        if n2 + 1 != 0:
                            heappush(heap, (n2 + 1, p2))
                        heappush(heap, (n3, p3))
                else:
                    # Evacuate the last two parties if n1 = n2
                    res.append(str(p1) + str(p2))
                    if n1 + 1 != 0:
                        heappush(heap, (n1 + 1, p1))
                    if n2 + 1 != 0:
                        heappush(heap, (n2 + 1, p2))
            else:
                # Evacuate the top 1 party if n1 > n2
                res.append(str(p1))
                if n1 + 1 != 0:
                    heappush(heap, (n1 + 1, p1))
                heappush(heap, (n2, p2))
        else:
            # Evacuate the last one party.
            res.append(str(p1))
            if n1 + 1 != 0:
                heappush(heap, (n1 + 1, p1))
        
    return " ".join(res)


for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, senate_evacuation())
