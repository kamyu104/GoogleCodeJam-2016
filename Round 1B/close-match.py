# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 1B - Problem B. Close Match
# https://code.google.com/codejam/contest/11254486/dashboard#s=p1
#
# Time:  O(N * 3^N)
# Space: O(N)
#

def smallest(S):
    return S.replace('?', '0')


def largest(S):
    return S.replace('?', '9')


def close_match(S, J):
    n = len(S)
    if n == 0:
        return (0, '', '')

    if S[0] == J[0]:
        if S[0] == '?':
            return min(close_match('0' + S[1:], '0' + J[1:]),
                       close_match('0' + S[1:], '1' + J[1:]),
                       close_match('1' + S[1:], '0' + J[1:]))
        else:
            R = close_match(S[1:], J[1:])
            return (R[0], S[0] + R[1], J[0] + R[2])
    elif S[0] == '?':
        x = int(J[0])
        return min(close_match(str(x + d) + S[1:], J) \
                   for d in [-1, 0, 1] if 0 <= x + d <= 9)
    elif J[0] == '?':
        x = int(S[0])
        return min(close_match(S, str(x + d) + J[1:]) \
                   for d in [-1, 0, 1] if 0 <= x + d <= 9)
    elif S[0] < J[0]:
        s = largest(S)
        j = smallest(J)
        return (int(j) - int(s), s, j)
    else:
        s = smallest(S)
        j = largest(J)
        return (int(s) - int(j), s, j)


for case in xrange(input()):
    S, J = raw_input().strip().split()
    print 'Case #{0}: {2} {3}'.format(case+1, *close_match(S, J))
