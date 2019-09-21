# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2016 World Finals - Problem C. Gallery of Pillars
# https://code.google.com/codejam/contest/7234486/dashboard#s=p2
#
# Time:  O(NlogN)
# Space: O(N)
#

from math import sqrt

def count(max_x, r_square):
    # for 0 <= x, y <= max_x, (x, y) != (0, 0), count (x, y) s.t. x^2 + y^2 <= r^2
    result = 0
    y = min(max_x, int(sqrt(r_square)))
    for x in xrange(y+1):
        while x*x + y*y > r_square:
            y -= 1
        result += y+1  # (x, 0) ~ (x, y)
    result -= 1  # exclude (0, 0)
    return result

def gallery_of_pillars():
    N, R = map(int, raw_input().strip().split())
    result = 0
    r_square = (M*M-1)//R//R
    for k in xrange(1, int(sqrt(r_square))+1):
        if MOBIOUS[k] and (N-1)//k >= 1:
            result += MOBIOUS[k] * count((N-1)//k, r_square//k//k)
    return result

def sieve_of_eratosthenes(N):
    is_prime = [True]*N
    mobious = [1]*N
    for i in xrange(2, N):
        if not is_prime[i]:
            continue
        for j in xrange(i+i, N, i):
            is_prime[j] = False
        for j in xrange(i, N, i):
            mobious[j] = -mobious[j]
        if i <= N//i:
            for j in xrange(i*i, N, i*i):
                mobious[j] = 0
    return mobious

M = 10**6
MOBIOUS = sieve_of_eratosthenes(M)
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, gallery_of_pillars())
