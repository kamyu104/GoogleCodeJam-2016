# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2016 World Finals - Problem E. Radioactive Islands
# https://code.google.com/codejam/contest/7234486/dashboard#s=p4
#
# Time:  O(IT * W * X/H), X is the const range of x for integral
#                       , IT is the count of iterations for hill-climbing method
#                       , W is the interval window size
#                       , H is the dx parameter for integral
# Space: O(X/H)
#
# Hill-Climbing method: faster than dp, but slower than Calculus of Variations
#

from sys import float_info
from math import sqrt

def D(C, x, y):
    dose = 0.0
    for c in C:
        d_square = x**2 + (y-c)**2
        if d_square < float_info.epsilon:
            return float("inf")
        dose += 1.0/d_square
    return dose

def f(C, x, y, dx, dy):
    return (1.0+D(C, x, y)) * sqrt(dx**2 + dy**2)

def F(C, path):
    dose = 0.0
    for i in xrange(len(path)-1):
        dose += f(C, path[i][0], path[i][1], H, path[i+1][1]-path[i][1])
    return dose

def dy(path, m, i, j):
    if j in (0, len(path)-1):
        return 0.0  # no change on begin and end
    return m * (W-abs(j-i))

def fi(C, path, i, m):
    new_path = [[path[j][0], path[j][1]+dy(path, m, i, j)] for j in xrange(max(0, i-W), min(i+W+1, len(path)))]
    return F(C, new_path)

def move(path, i, m):
    for j in xrange(max(0, i-W), min(i+W+1, len(path))):
        path[j][1] += dy(path, m, i, j)

def hill_climbing(C, path):
    for it in xrange(IT):
        is_changed = False
        for i in xrange(len(path)):
            up, down = fi(C, path, i, M), fi(C, path, i, -M)
            if up < down:
                move(path, i, M)
                is_changed = True
            elif down < up:
                move(path, i, -M)
                is_changed = True
        if not is_changed:
            break
    return F(C, path)

def radioactive_islands():
    N, A, B = map(float, raw_input().strip().split())
    C = map(float, raw_input().strip().split())
    regions = [MIN_Y_BOUND, MAX_Y_BOUND]
    regions.extend(C)
    regions.sort()
    result = float("inf")
    for i in xrange(len(regions)-1):
        assert(PATH_LEN%2 == 1)
        mid, mid_y = (PATH_LEN-1)//2, (regions[i]+regions[i+1])/2.0
        path = []
        path.extend([X_START+j*H, A + 1.0*j/mid * (mid_y-A)]
                    for j in xrange(mid))
        path.extend([X_START+j*H, mid_y + 1.0*(j-mid)/(PATH_LEN-1-mid)*(B-mid_y)]
                    for j in xrange(mid, PATH_LEN))
        result = min(result, hill_climbing(C, path))
    return result

IT = 1600  # tuned by experiment
W = 2  # interval window size is 2W+1 for move of hill-climbing, ex. move (0, 1, 2, 3, 4, 3, 2, 1, 0), tuned by experiment
H = 0.5  # tuned by experiment

MIN_Y_BOUND, MAX_Y_BOUND = -13.0, 13.0  # verified by experiment
X_START, X_END = -10.0, 10.0
PATH_LEN = int((X_END-X_START)/H)+1
M = (MAX_Y_BOUND-MIN_Y_BOUND)/(W**2*IT)  # every iteration each point can move [0, W^2] up or down in a triangular shape
for case in xrange(input()):
    print ("Case #%d: %s" % (case+1, radioactive_islands()))
