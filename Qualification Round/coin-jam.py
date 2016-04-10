# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Qualification Round - Problem C. Coin Jam
# https://code.google.com/codejam/contest/6254486/dashboard#s=p2
#
# Time:  O(N * J)
# Space: O(N)
#

def coin_jam():
    N, J = map(int, raw_input().strip().split())
    # 1xxxxxx11xxxxxx1b = 1xxxxxx1b * 100000001b
    divisors = " ".join([str(i ** (N / 2) + 1) for i in xrange(2, 11)])
    # Enumerate J numbers like 1xxxxxx from 1000000
    start = 2 ** ((N / 2) - 2)
    for i in xrange(start, start + J):
        binary = bin(i)[2:] + "1"  # 1xxxxxx1
        binary *= 2                # 1xxxxxx11xxxxxx1
        print binary, divisors
    
for case in xrange(input()):
    print 'Case #%d:' % (case+1)
    coin_jam()
