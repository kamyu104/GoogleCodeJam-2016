# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 3 - Problem C. Rebel Against The Empire
# https://code.google.com/codejam/contest/3224486/dashboard#s=p2
#
# Time:  O(logN * (N^2 + H * N)), H is the length of possible planets in the timeline. (Height of BFS)
# Space: O(N^2)
#
# TLE (Although it fails in Python, it could pass in C++ within 20 seconds)
#

from collections import deque
from math import sqrt, log

INF = 1e10
MAX_N = 1000
PRECISION = 1e-4
START, END = 0, 1

P = [[0 for _ in xrange(3)] for _ in xrange(MAX_N)]
V = [[0 for _ in xrange(3)] for _ in xrange(MAX_N)]

jump_begin = [[0 for _ in xrange(MAX_N)] for _ in xrange(MAX_N)]
jump_end = [[0 for _ in xrange(MAX_N)] for _ in xrange(MAX_N)]
stay_begin = [INF] * MAX_N
stay_end = [-INF] * MAX_N

def compare(N, S, P, V, D):
    for i in xrange(N):
        stay_begin[i], stay_end[i] = INF, -INF
        for j in xrange(N):
            if i != j:
                # (vi - vj)t + pi - pj <= d
                # At^2 + Bt + (C-D) <= 0
                # (-B - sqrt(B^2 - 4(C-D))) / 2A <= t <= (-B + sqrt(B^2 - 4(C-T))) / 2A
                dP = (P[i][0] - P[j][0], P[i][1] - P[j][1], P[i][2] - P[j][2])
                dV = (V[i][0] - V[j][0], V[i][1] - V[j][1], V[i][2] - V[j][2])
                A = dV[0]**2 + dV[1]**2 + dV[2]**2
                B = 2 * (dV[0]*dP[0] + dV[1]*dP[1] + dV[2]*dP[2])
                C = dP[0]**2 + dP[1]**2 + dP[2]**2
                jump_begin[i][j] = INF
                jump_end[i][j] = -INF
                if A == 0:
                    if C-D <= 0:
                        jump_begin[i][j] = 0.0
                        jump_end[i][j] = INF
                else:
                    if B**2- 4*A*(C-D) >= 0:
                        jump_begin[i][j] = (-B - sqrt(B**2 - 4*A*(C-D))) / 2 / A
                        jump_end[i][j] = (-B + sqrt(B**2 - 4*A*(C-D))) / 2 / A

    for i in xrange(N):
        stay_begin[i] = INF
        stay_end[i] = -INF
    stay_begin[0] = 0
    stay_end[0] = S

    # BFS
    q = deque()
    q.append(START)
    while q:
        i = q.popleft()
        # Jump to possible planet.
        for j in xrange(N):
            if j != i and jump_begin[i][j] < jump_end[i][j]:
                L = max(stay_begin[i], jump_begin[i][j])
                R = min(stay_end[i], jump_end[i][j])
                if L <= R:
                    if j == END:
                        return True
                    R = jump_end[i][j]
                    if L < stay_begin[j] or R + S > stay_end[j]:
                        # Add unvisited / updated planet to queue.
                        stay_begin[j] = min(stay_begin[j], L)
                        stay_end[j] = max(stay_end[j], R + S)
                        q.append(j)

    return False

def rebel_against_the_empire():
    N, S = map(int, raw_input().strip().split())
    for i in xrange(N):
        P[i][0], P[i][1], P[i][2], V[i][0], V[i][1], V[i][2] = map(int, raw_input().strip().split())

    left, right = 0.0, 3 * 1000**2
    times = log((right - left) / (PRECISION * PRECISION), 2) + 1
    for _ in xrange(int(times)):
        mid = left + (right - left) / 2
        if compare(N, S, P, V, mid):
            right = mid
        else:
            left = mid
    return sqrt(mid)


for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, rebel_against_the_empire())
