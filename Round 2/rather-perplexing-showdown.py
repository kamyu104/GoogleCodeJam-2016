# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 2 - Problem A. Rather Perplexing Showdown
# https://code.google.com/codejam/contest/10224486/dashboard#s=p0
#
# Time:  O(2^N)
# Space: O(2^N)
#

def rather_perplexing_showdown():
    N, R, P, S = map(int, raw_input().strip().split())

    # Init the 3 possible lineups at the end.
    a, b, c = 'P', 'R', 'S'

    # Build the 3 possible lineups alphabetically earlier
    # at the beginning. a < b < c in alphabetical order.
    for _ in xrange(N):
        a, b, c = a + b, a + c, b + c

    for lineup in (a, b, c):
        # Check if the limit is matched.
        if lineup.count('R') == R and \
           lineup.count('P') == P and \
           lineup.count('S') == S:
            return lineup
    else:
        return "IMPOSSIBLE"


for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, rather_perplexing_showdown())
