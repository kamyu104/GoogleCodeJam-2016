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
    
    K = min(K, S)
    # If S >= K:
    #   Let outfits be (j, p, s), and s = (j + p + d) % S, 0 <= j < J, 0 <= p < P, 0 <= d < K:
    #  - For pair (j, p), s = (j + p + d) % S is at most K choices due to d is at most K choices
    #  - For pair (j, s), p = (s - j - d) % S is at most K choices due to d is at most K choices
    #  - For pair (p, s), j = (s - p - d) % S is at most K choices due to d is at most K choices
    #
    #  => the combinations won't exceed the maximum.
    return [(j, p, (j + p + d) % S) for j in xrange(J) \
                                    for p in xrange(P) \
                                    for d in xrange(K)]


for case in xrange(input()):
    res = fashion_police()
    print "Case #{}: {}\n{}".format(case+1, \
                                    len(res), \
                                    "\n".join(" ".join(str(val+1) for val in outfit) \
                                                                  for outfit in res))
