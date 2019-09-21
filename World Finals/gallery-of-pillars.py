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
    # count pairs of |(x, y)|^2 <= r_square and
    # 1 <= x, y <= min(side_len, int(sqrt(r_square)))
    result = 0
    y = side_len
    if r_square < y*y:
        y = int(sqrt(r_square))  # Time: O(log(N/k))
    for x in xrange(1, y+1):
        while x*x + y*y > r_square:
            y -= 1  # Time: O(N/k)
        result += y  # (x, 1) ~ (x, y)
    return result

def gallery_of_pillars():
    N, R = map(int, raw_input().strip().split())
    # result = count of [(1, 0), (0, 1)] + [pairs of |(x, y)| < M/R and 1 <= x, y <= N-1 and gcd(x, y) = 1]
    result = 2
    r_square = (M*M-1)//R//R
    for k in xrange(1, min(N-1, int(sqrt(r_square)))+1):  # sum of O(N/k) = O(NlogN)
        if MOBIOUS[k]:
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
