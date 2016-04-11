# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Qualification Round - Problem B. Revenge of the Pancakes
# https://code.google.com/codejam/contest/6254486/dashboard#s=p1
#
# Time:  O(N)
# Space: O(1)
#

def revenge_of_the_pancakes():
    stack = raw_input().strip()
    # The best strategy is to flip between
    # two pancakes facing opposite directions.
    return stack.count('-+') + stack.count('+-') + int(stack.endswith('-'))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, revenge_of_the_pancakes())
