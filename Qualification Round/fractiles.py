# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Qualification Round - Problem D. Fractiles
# https://code.google.com/codejam/contest/6254486/dashboard#s=p1
#
# Time:  O(K)
# Space: O(1)
#

def fractiles():
    K, C, S = map(int, raw_input().strip().split())

    # We can only check C positions in the original artwork by 1 student.
    if C * S < K:
        return "IMPOSSIBLE"

    indexes = []
    for i in xrange(1, K + 1, C):
        # Let p(j) be a position in the artwork of complexity (j+1) s.t
        # p(j) = (p(j - 1) - 1) * K + d(j) (1 <= d(j) <= K)
        # We observe that the value of p(j) is L iff p(j-1) is L, and iff,
        # ..., and iff p(0) is L, and iff the values of p(0) in the
        # position d(0) ~ d(C-1) are Ls
        #
        # So we want to check if the values of p(0)
        # in the position i ~ i + C-1 are all Ls,
        # We may choose d(j) to be min(i + j, K),
        # thus we only need to check if the value of p(C) is L
        # to get the answer.
        p = 1
        for j in xrange(C):
            p = (p - 1) * K + min(i + j, K)
        indexes.append(str(p))
    return " ".join(indexes)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, fractiles())
