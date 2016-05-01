# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 1B - Problem B. Close Match
# https://code.google.com/codejam/contest/11254486/dashboard#s=p1
#
# Time:  O(N^2)
# Space: O(N)
#

def awins(A, B, target=-1):
    wins, X, Y = False, list(A), list(B)
    for i in xrange(len(X)):
        if wins:
            if X[i] == '?':
                X[i] = '0'         
            if Y[i] == '?':
                Y[i] = '9' 
        else:
            if X[i] != '?' and Y[i] != '?':
                if X[i] < Y[i]:
                    return (float("inf"), 0, 0)
                if X[i] > Y[i]:
                    wins = True
            else:
                if i == target:
                    if X[i] == '?' and Y[i] == '?':
                        X[i], Y[i] = '1', '0'
                    elif X[i] == '?' and Y[i] != '9':
                        X[i] = str(int(Y[i])+1)
                    elif Y[i] == '?' and X[i] != '0':
                        Y[i] = str(int(X[i])-1)

                    if X[i] != '?' and Y[i] != '?':
                        wins = True

                if X[i] == '?' and Y[i] == '?':
                    X[i], Y[i] = '0', '0'
                elif X[i] == '?':
                    X[i] = Y[i]
                elif Y[i] == '?':
                    Y[i] = X[i]

    X = "".join(X)
    Y = "".join(Y)
    return (int(X)-int(Y), X, Y)


def bwins(A, B, hint=-1):
    X = awins(B, A, hint)
    return (X[0], X[2], X[1])


def close_match():
    A, B = raw_input().strip().split()
    res = min(awins(A, B), bwins(A, B))
    for i in xrange(len(A)):
        res = min(res, min(awins(A, B, i), bwins(A, B, i)))
        
    return res

for case in xrange(input()):
    print 'Case #{0}: {2} {3}'.format(case+1, *close_match())
