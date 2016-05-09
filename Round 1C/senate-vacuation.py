import heapq

def senate_evacuation():
    N = int(input())
    P = map(int, raw_input().strip().split())
    heap, res = [], []
    for i, n in enumerate(P):
        heapq.heappush(heap, (-n, chr(ord('A') + i)))
    total = sum(P)
    while heap:
        n1, p1 = heapq.heappop(heap)
        if heap:
            n2, p2 = heapq.heappop(heap)
            if n1 == n2:
                if heap:
                    n3, p3 = heapq.heappop(heap)
                    if n2 == n3:
                        res.append(str(p1))
                        if n1 + 1 != 0:
                            heapq.heappush(heap, (n1 + 1, p1))
                        heapq.heappush(heap, (n2, p2))
                        heapq.heappush(heap, (n3, p3))
                    else:
                        res.append(str(p1) + str(p2))
                        if n1 + 1 != 0:
                            heapq.heappush(heap, (n1 + 1, p1))
                        if n2 + 1 != 0:
                            heapq.heappush(heap, (n2 + 1, p2))
                        heapq.heappush(heap, (n3, p3))
                else:
                    res.append(str(p1) + str(p2))
                    if n1 + 1 != 0:
                        heapq.heappush(heap, (n1 + 1, p1))
                    if n2 + 1 != 0:
                        heapq.heappush(heap, (n2 + 1, p2))
            else:
                res.append(str(p1))
                if n1 + 1 != 0:
                    heapq.heappush(heap, (n1 + 1, p1))
                heapq.heappush(heap, (n2, p2))
        else:
            res.append(str(p1))
            if n1 + 1 != 0:
                heapq.heappush(heap, (n1 + 1, p1))
        
    return " ".join(res)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, senate_evacuation())