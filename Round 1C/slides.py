# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 1C - Problem A. Senate Evacuation
# https://code.google.com/codejam/contest/4314486/dashboard#s=p1
#
# Time:  O(B^2)
# Space: O(1)
#

def slides():
    B, M = map(int, raw_input().strip().split())
    # The number of ways without loop is at most 2^(B-2).
    # We can create the graph in this form:
    # 01111
    # 00111
    # 00011
    # 00001
    # 00000
    if M > (2 ** (B - 2)):
        return []

    # Init row 1 ~ B
    # 00000
    # 00111
    # 00011
    # 00001
    # 00000
    res = [[0 for _ in xrange(B)] for _ in xrange(B)]
    for i in xrange(1, B):
        for j in xrange(i + 1, B):
            res[i][j] = 1

    # We can create the graph in exact M ways in this form:
    # 0????
    # 00111
    # 00011
    # 00001
    # 00000
    if M == 2 ** (B - 2):
        # row 1 is 01111
        for j in xrange(1, B):
            res[0][j] = 1
    else:
        # row 1 is 0???0, ??? is M in binary format.
        j = -2
        while M:
            res[0][j] = M % 2
            M /= 2
            j -= 1

    return res


for case in xrange(input()):
    res = slides()
    if not res:
        print 'Case #%d: %s' % (case+1, "IMPOSSIBLE")
    else:
        print 'Case #%d: %s' % (case+1, "POSSIBLE")
        for row in res:
           print "".join(map(str, row))
