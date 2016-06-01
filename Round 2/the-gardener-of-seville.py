# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 2 - Problem C. The Gardener of Seville
# https://code.google.com/codejam/contest/10224486/dashboard#s=p2
#
# Time:  O((R + C)log(R + C) + R * C)
# Space: O(R * C)
#

DOWN, LEFT, UP, RIGHT = 0, 1, 2, 3
directions = {DOWN:(0, 1), LEFT:(-1, 0), UP:(0, -1), RIGHT:(1, 0)}
mirror = {"/":{DOWN:LEFT, LEFT:DOWN, UP:RIGHT, RIGHT:UP}, \
          "\\":{DOWN:RIGHT, LEFT:UP, UP:LEFT, RIGHT:DOWN},}

def position(v, R, C):
    if v <= C: return DOWN, (v-1, -1)  # Upper side.
    v -= C
    if v <= R: return LEFT, (C, v-1)  # Right side.
    v -= R
    if v <= C: return UP, (C-v, R)  # Lower side.
    v -= C
    return RIGHT, (-1, R-v)  # Left side.


def move(x, y, d):
    return x + directions[d][0], y + directions[d][1]


def the_gardener_of_seville():
    R, C = map(int, raw_input().strip().split())
    permutation = map(int, raw_input().strip().split())
    board = [[None] * C for _ in xrange(R)]
    size = 2*(R+C)
    permutation = zip(permutation[::2], permutation[1::2])
    permutation.sort(key=lambda(a,b): min((b-a)%size, (a-b)%size))  # O((R + C)log(R + C))
    for A, B in permutation:  # O(R * C)
        # Let the two outer cells be A and B,
        # such that A->B clockwise around the edge is shorter
        # than counterclockwise
        if (A-B) % size > R+C:
            A, B = B, A
        direction, (x, y) = position(A, R, C)
        x, y = move(x, y, direction)
        while 0<=x<C and 0<=y<R:
            if board[y][x] is None:
                # Install a hedge on a vacant cell to turn right.
                board[y][x] = "/" if direction in (DOWN, UP) else "\\"
            direction = mirror[board[y][x]][direction]
            x, y = move(x, y, direction)
        if (x, y) != position(B, R, C)[1]:
            return "IMPOSSIBLE"
    return "\n".join("".join(c or "/" for c in row) for row in board)


for case in xrange(input()):
    print 'Case #%d:\n%s' % (case+1, the_gardener_of_seville())