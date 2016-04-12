# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Qualification Round - Problem A. Counting Sheep
# https://code.google.com/codejam/contest/6254486/dashboard#s=p0
#
# Time:  O(PlogP) = O(10 * N * log(10 * N)) = O(NlogN), P is the smallest power of 10 greater than N
# Space: O(logP) = O(logN)
#

def counting_sheep():
    N = int(input())
    if N == 0:
        return "INSOMNIA"

    digits = set([])
    cnt = 0
    while len(digits) != 10:  # At most O(P) times.
        cnt += N
        tmp = cnt
        while tmp:  # O(logP) times.
            digits.add(tmp % 10)
            tmp /= 10
    return cnt

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, counting_sheep())
