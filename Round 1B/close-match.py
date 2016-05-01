# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 1B - Problem B. Close Match
# https://code.google.com/codejam/contest/11254486/dashboard#s=p1
#
# Time:  O(N^2)
# Space: O(N)
#

def a_wins(A, B, i=-1):
    is_won, X, Y = False, list(A), list(B)
    if i >= 0:
        if X[i] == '?' and Y[i] == '?':
            X[i], Y[i] = '1', '0'  # Try '1', '0' to win.
        elif X[i] == '?' and Y[i] != '9':
            X[i] = str(int(Y[i])+1)  # Change to 1 more than that digit to win.
        elif Y[i] == '?' and X[i] != '0':
            Y[i] = str(int(X[i])-1)  # Change to 1 less than that digit to win.
        else:
            # Change nothing (dupilcated work), just return a default val.
            return (float("inf"), 0, 0)

    for i in xrange(len(X)):
        if is_won:  # Already won, just minimize the difference.
            if X[i] == '?':
                X[i] = '0'         
            if Y[i] == '?':
                Y[i] = '9' 
        else:
            if X[i] != '?' and Y[i] != '?':
                if X[i] < Y[i]:
                    return (float("inf"), 0, 0)  # Impossible to win, just return a default val.
                if X[i] > Y[i]:
                    is_won = True
            elif X[i] == '?' and Y[i] == '?':
                X[i], Y[i] = '0', '0'  # Try '0', '0' to win.
            elif X[i] == '?':
                X[i] = Y[i]  # Change to that digit to win.
            elif Y[i] == '?':
                Y[i] = X[i]  # Change to that digit to win.

    X, Y = "".join(X), "".join(Y)
    return (int(X)-int(Y), X, Y)


def b_wins(A, B, i=-1):
    X = a_wins(B, A, i)
    return (X[0], X[2], X[1])


def close_match():
    A, B = raw_input().strip().split()

    # Change nothing to win.
    res = min(a_wins(A, B), b_wins(A, B))
    # Try to change at each position with any '?' to minimize the difference. 
    for i in xrange(len(A)):
        res = min(res, min(a_wins(A, B, i), b_wins(A, B, i)))
    return res


for case in xrange(input()):
    print 'Case #{0}: {2} {3}'.format(case+1, *close_match())
