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

    for M in xrange(K+1):
        # The best way to create a tie is to choose department members
        # from one or both extremes.
        V = P[:M] + P[N-K+M:]

        # dp[i][j]: the probability of i members with j yes votes.
        dp = [[1.0], []]
        for i in xrange(1, K + 1):
            dp[i % 2] = [0] * (len(dp[(i - 1) % 2]) + 1)
            for j in xrange(i):
                dp[i % 2][j] += dp[(i - 1) % 2][j] * (1 - V[i - 1])  # vote no
                dp[i % 2][j + 1] += dp[(i - 1) % 2][j] * V[i - 1]  # vote yes

        # The probability of tie is the probability of
        # K members with (K/2) yes votes.
        result = max(result, dp[K % 2][K / 2])

    return result


for case in xrange(input()):
    print 'Case #%d: %.10f' % (case+1, red_tape_committee())
