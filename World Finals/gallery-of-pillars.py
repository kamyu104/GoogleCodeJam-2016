# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2016 World Finals - Problem C. Gallery of Pillars
# https://code.google.com/codejam/contest/7234486/dashboard#s=p2
#
# Time:  O(NlogN)
# Space: O(M)
#

from math import sqrt

def count(side_len, r_square):  # Time: O(side_length) = O(N/k), Space: O(1)
    # for 0 <= x, y <= side_len, (x, y) != (0, 0), count (x, y) s.t. x^2 + y^2 <= r^2
    result = 0
    y = side_len
    if r_square < y*y:
        y = int(sqrt(r_square))
    for x in xrange(y+1):
        while x*x + y*y > r_square:
            y -= 1
        result += y+1  # (x, 0) ~ (x, y)
    result -= 1  # exclude (0, 0)
    return result

def gallery_of_pillars():
    N, R = map(int, raw_input().strip().split())
    # count pairs of |(x, y)| < M/R and gcd(x, y) = 1
    result = 0
    r_square = (M*M-1)//R//R
    for k in xrange(1, int(sqrt(r_square))+1):  # sum of O(N/k) = O(NlogN)
        if MOBIOUS[k] and (N-1)//k >= 1:
            result += MOBIOUS[k] * count((N-1)//k, r_square//k//k)
    return result

def sieve_of_eratosthenes(n):  # Time: O(M), Space: O(M)
    is_prime = [True]*n
    mobious = [1]*n
    for i in xrange(2, n):
        if not is_prime[i]:
            continue
        for j in xrange(i+i, n, i):
            is_prime[j] = False
        for j in xrange(i, n, i):
            mobious[j] = -mobious[j]
        if i <= n//i:
            for j in xrange(i*i, n, i*i):
                mobious[j] = 0
    return mobious

M = 10**6
MOBIOUS = sieve_of_eratosthenes(M)
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, gallery_of_pillars())
