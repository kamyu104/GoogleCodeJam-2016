# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 1A - Problem A. The Last Word
# https://code.google.com/codejam/contest/4304486/dashboard#s=p0
#
# Time:  O(N), N is the length of S
# Space: O(N)
#

from collections import deque

def the_last_word():
    res = deque()
    S = raw_input().strip()
    for c in S:
        if res and c >= res[0]:
            res.appendleft(c)
        else:
            res.append(c)
    return "".join(res)


for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, the_last_word())
