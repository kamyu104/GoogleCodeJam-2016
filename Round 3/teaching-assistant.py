# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 3 - Problem A. Teaching Assistant
# https://code.google.com/codejam/contest/3224486/dashboard#s=p0
#
# Time:  O(S)
# Space: O(S)
#

def teaching_assistant():
    S = raw_input().strip()
    mood = []
    for c in S:
        if mood and mood[-1] == c:  # Pair [CC|JJ].
            mood.pop()
        else:  # Remaining (CJ)+/(JC)+
            mood.append(c)
    # maximum points - (count of [CJ|JC]) * 5
    return len(S) / 2 * 10 - len(mood) / 2 * 5


for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, teaching_assistant())
