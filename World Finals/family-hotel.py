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
s = [0] * MAX_N
f[0] = 1
s[0], s[1] = 1, 1
for i in xrange(2, MAX_N):
    f[i] = mul(s[i - 2], inv(i))
    s[i] = add(s[i - 1], f[i])

def family_hotel():
    N, K = map(int, raw_input().strip().split())
    left, right = K - 1, N - K
    return sub(1, mul(f[left], f[right]))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, family_hotel())
