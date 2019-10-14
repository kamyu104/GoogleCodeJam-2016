# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2016 World Finals - Problem E. Radioactive Islands
# https://code.google.com/codejam/contest/7234486/dashboard#s=p4
#
# Time:  O(P^2*G^2), P is the granularity parameter of y, G is the number of grids
# Space: O(P*G)
#
# referenced from https://code.google.com/codejam/contest/scoreboard/do?cmd=GetSourceCode&contest=7234486&problem=5760632301289472&io_set_id=1&username=Gennady.Korotkevich
#

from sys import float_info
from math import sqrt

def D(C, x):
    dose = 0.0
    for c in C:
        dist = x[0]**2 + (x[1]-c)**2
        if dist < float_info.epsilon:
            return float("inf")
        dose += 1.0/dist
    return dose

def calc(C, a, b):  # dose = (1 + sum(1 / (x^2 + (y-ci)^2))) * sqrt(dx^2 + dy^2)
    return (1.0+D(C, (X_START + a[0]*X_STEP, Y_START + a[1]*Y_STEP))) * \
           sqrt(((b[0]-a[0])*X_STEP)**2 + ((b[1]-a[1])*Y_STEP)**2)

def radioactive_islands():
    N, A, B = map(float, raw_input().strip().split())
    C = map(float, raw_input().strip().split())
    dp = [float("inf")]*(Y_GRID_NUM+1)
    dp[int((A-Y_START)/Y_STEP + 0.5)] = 0.0
    for i in xrange(1, X_GRID_NUM+1):
        new_dp = [float("inf")]*(Y_GRID_NUM+1)
        for j in xrange(Y_GRID_NUM+1):
            for k in xrange(max(0, j-NEIGHBORS_NUM), min(Y_GRID_NUM, j+NEIGHBORS_NUM)+1):
                new_dp[j] = min(new_dp[j], dp[k] + calc(C, (i-1, k), (i, j)))
        dp = new_dp
    return dp[int((B-Y_START)/Y_STEP + 0.5)]

GRANULARITY = 26  # tuned by experiment
GRID_NUM = 40  # tuned by experiment
MAX_ABS_SLOPE = 2  # verified by experiment
Y_START, Y_END = -13.0, 13.0  # verified by experiment

X_START, X_END = -10.0, 10.0
X_GRID_NUM, Y_GRID_NUM = GRID_NUM, GRANULARITY*GRID_NUM
NEIGHBORS_NUM = MAX_ABS_SLOPE*Y_GRID_NUM//X_GRID_NUM
X_STEP = (X_END-X_START)/X_GRID_NUM
Y_STEP = (Y_END-Y_START)/Y_GRID_NUM
for case in xrange(input()):
    print "Case #%d: %s" % (case+1, radioactive_islands())
