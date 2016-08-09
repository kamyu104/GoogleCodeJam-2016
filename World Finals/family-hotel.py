# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 World Finals - Problem B. Family Hotel
# https://code.google.com/codejam/contest/7234486/dashboard#s=p1
#
# Time:  O(N)
# Space: O(N)
#

prime = 1000000007
MAX_N = 10 ** 7

def add(a, b):
    return (a + b) % prime

def sub(a, b):
    return (a - b) % prime

def mul(a, b):
    return (a * b) % prime

# Euler's Theorem: x^(p - 1) mod p = 1
# For p prime, the inverse of any number x mod p is x^(p - 2) mod p.
def inv(x):
    return pow(x, prime - 2, prime)

f = [0] * MAX_N
s = [0] * 3
f[0] = 1
s[0], s[1] = f[0], f[0] + f[1]
for n in xrange(2, MAX_N):
    # f[n]: the probability of the first two rooms are assigned in the n rooms.
    # f[0] = 1, f[1] = 0
    # f[n] = 1/n * (1 + f[1] + f[2] + ... + f[n-2])
    f[n] = mul(inv(n), s[(n-2) % 3])
    # s[n] = 1 + f[1] + f[2] + ... + f[n]
    s[n % 3] = add(s[(n-1) % 3], f[n])

def family_hotel():
    N, K = map(int, raw_input().strip().split())
    left, right = K - 1, N - K
    # 1 - P(left & right both assigned)
    return sub(1, mul(f[left], f[right]))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, family_hotel())
