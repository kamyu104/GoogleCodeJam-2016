# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 2 - Problem C. The Gardener of Seville
# https://code.google.com/codejam/contest/10224486/dashboard#s=p2
#
# Time:  O((R + C)log(R + C) + R * C)
# Space: O(R * C)
#

DOWN, LEFT, UP, RIGHT = 0, 1, 2, 3
directions = {DOWN:(1, 0), LEFT:(0, -1), UP:(-1, 0), RIGHT:(0, 1)}
mirrors = {"/":{DOWN:LEFT, LEFT:DOWN, UP:RIGHT, RIGHT:UP}, \
           "\\":{DOWN:RIGHT, LEFT:UP, UP:LEFT, RIGHT:DOWN},}

def position(v, R, C):
    if v <= C: return DOWN, (-1, v-1)  # Upper side.
    v -= C
    if v <= R: return LEFT, (v-1, C)  # Right side.
    v -= R
    if v <= C: return UP, (R, C-v)  # Lower side.
    v -= C
    return RIGHT, (R-v, -1)  # Left side.

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
        x, y = x + directions[direction][0], y + directions[direction][1]
        while 0<=x<R and 0<=y<C:
            if board[x][y] is None:
                # Install a hedge on a vacant cell to turn right.
                board[x][y] = "/" if direction in (DOWN, UP) else "\\"
            direction = mirrors[board[x][y]][direction]
            x, y = x + directions[direction][0], y + directions[direction][1]
        if (x, y) != position(B, R, C)[1]:
            return "IMPOSSIBLE"
    return "\n".join("".join(c or "/" for c in row) for row in board)


for case in xrange(input()):
    print 'Case #%d:\n%s' % (case+1, the_gardener_of_seville())
