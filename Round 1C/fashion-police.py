# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 1C - Problem C. Fashion Police
# https://code.google.com/codejam/contest/4314486/dashboard#s=p2
#
# Time:  O(J * P * min(S, K))
# Space: O(1)
#

def fashion_police():
    J, P, S, K = map(int, raw_input().strip().split())

    if S <= K:
        return [(j, p, s) for j in xrange(J) \
                          for p in xrange(P) \
                          for s in xrange(S)]

    # S > K
    return [(j, p, (j + p + d) % S) for j in xrange(J) \
                                    for p in xrange(P) \
                                    for d in xrange(K)]


for case in xrange(input()):
    res = fashion_police()
    print "Case #{}: {}\n{}".format(case+1, \
                                    len(res), \
                                    "\n".join(" ".join(str(val+1) for val in outfit) \
                                                                  for outfit in res))
