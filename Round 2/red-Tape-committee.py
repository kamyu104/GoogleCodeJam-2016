# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 2 - Problem B. Red Tape Committee
# https://code.google.com/codejam/contest/10224486/dashboard#s=p1
#
# Time:  O(NlogN + K^3)
# Space: O(K)
#

def red_tape_committee():
    N, K = map(int, raw_input().strip().split())
    P = sorted(map(float, raw_input().strip().split()))
    result = 0
    for i in xrange(K+1):
        V = P[:i] + P[N-K+i:]
        dp = [[1.0], []]
        for j in xrange(1, K + 1):
            dp[j % 2] = [0] * (len(dp[(j - 1) % 2])+1)
            for l in xrange(j):
                dp[j % 2][l] += dp[(j - 1) % 2][l] * (1 - V[j - 1])
                dp[j % 2][l + 1] += dp[(j - 1) % 2][l] * V[j - 1]
        result = max(result, dp[K % 2][K / 2])
    return result


for case in xrange(input()):
    print 'Case #%d: %.10f' % (case+1, red_tape_committee())
