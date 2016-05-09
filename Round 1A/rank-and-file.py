# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 1A - Problem B. Rank and File
# https://code.google.com/codejam/contest/4304486/dashboard#s=p1
#
# Time:  O(N^2)
# Space: O(N^2), at most N^2 numbers in the Counter
#

from collections import Counter

def rank_and_file():
    N = input()
    cnt = Counter()
    for _ in xrange(2 * N - 1):
        cnt += Counter(list(raw_input().strip().split()))
    
    file = []
    for k, v in cnt.iteritems():
        # The count of the missing number must be odd.
        if v % 2 == 1:
            file.append(k)
    # The order of the missing numbers must be sorted.
    file.sort(key=int)

    return " ".join(file)


for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, rank_and_file())
