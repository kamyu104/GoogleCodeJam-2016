# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 1B - Problem A. Getting the Digits
# https://code.google.com/codejam/contest/11254486/dashboard#s=p0
#
# Time:  O(N)
# Space: O(1)
#

from collections import Counter

# The count of each char in each number string.
cnts = [Counter(s) for s in ["ZERO", "ONE", "TWO", "THREE", \
                             "FOUR", "FIVE", "SIX", "SEVEN", \
                             "EIGHT", "NINE"]]

# The order for greedy method.
order = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]

# The unique char in the order.
unique = ['Z', 'O', 'W', 'T', 'U', \
          'F', 'X', 'S', 'G', 'N']

def getting_the_digits():
    S = raw_input().strip()
    cnt = Counter(list(S))
    ans = []
    for i in order:
        while cnt[unique[i]] > 0:
            cnt -= cnts[i]
            ans.append(i)
    ans.sort()
    return "".join(map(str, ans))


for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, getting_the_digits())
