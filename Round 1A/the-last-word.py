# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 1A - Problem A. The Last Word
# https://code.google.com/codejam/contest/4304486/dashboard#s=p0
#
# Time:  O(L), L is the length of S
# Space: O(L)
#

from collections import deque

def the_last_word():
    S = raw_input().strip()
    word = deque()
    for c in S:
        # Use greedy strategy to put the smaller char in the back,
        # and put the larger or equal char in the front.
        if word and c >= word[0]:
            word.appendleft(c)
        else:
            word.append(c)
    return "".join(word)


for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, the_last_word())
