# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2016 World Finals - Problem C. Gallery of Pillars
# https://code.google.com/codejam/contest/7234486/dashboard#s=p2
#
# Time:  O(NlogN)
# Space: O(M)
#

from math import sqrt

def count(side_len, r_square):  # Time: O(side_length) = O(N/d), Space: O(1)
    # count pairs of |(x, y)|^2 <= r_square and
    # 0 <= x, y <= min(side_len, int(sqrt(r_square))) and (x, y) != (0, 0)
    result = 0
    y = side_len
    if r_square < y*y:
        y = int(sqrt(r_square))  # Time: O(log(N/d))
    for x in xrange(y+1):
        while x*x + y*y > r_square:
            y -= 1  # Time: O(N/d)
        result += y+1  # (x, 0) ~ (x, y)
    return result-1  # exclude (0, 0)

def gallery_of_pillars():
    N, R = map(int, raw_input().strip().split())
    # count pairs of |(x, y)| < M/R and 0 <= x, y <= N-1 and gcd(x, y) = 1
    result = 0
    r_square = (M*M-1)//(R*R)
    for d in xrange(1, min(N-1, int(sqrt(r_square)))+1):  # Time: sum of O(N/d) = O(NlogN), see https://math.stackexchange.com/questions/306371/simple-proof-of-showing-the-harmonic-number-h-n-theta-log-n
        if MU[d]:  # see https://artofproblemsolving.com/wiki/index.php/Mobius_function
            result += MU[d] * count((N-1)//d, r_square//(d*d))
    return result

def sieve_of_eratosthenes(n):  # Time: O(Mlog(logM)), Space: O(M)
    is_prime = [True]*n
    mu = [1]*n
    for i in xrange(2, n):
        if not is_prime[i]:
            continue
        for j in xrange(i+i, n, i):
            is_prime[j] = False
        for j in xrange(i, n, i):
            mu[j] = -mu[j]
        if i <= n//i:
            for j in xrange(i*i, n, i*i):
                mu[j] = 0
    return mu

M = 10**6
MU = sieve_of_eratosthenes(M)
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, gallery_of_pillars())
