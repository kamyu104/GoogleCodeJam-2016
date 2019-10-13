# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2016 World Finals - Problem D. Map Reduce
# https://code.google.com/codejam/contest/7234486/dashboard#s=p3
#
# Time:  O((R * C) * log(R * C)), pass in PyPy2 but Python2
# Space: O(R * C)
#

from itertools import islice, imap
from collections import deque

def manhattan_distance(S, F):
    return abs(S[0]-F[0]) + abs(S[1]-F[1])

def shortest_distance(M, S, F):
    q = deque([(0, S)])
    lookup = set([S])
    while q:
        d, (r, c) = q.popleft()
        if (r, c) == F:
            return d
        for dr, dc in islice(DIRECTIONS, 4):
            nr, nc = r+dr, c+dc
            if not (0 <= nr < len(M) and 0 <= nc < len(M[0]) and
                    M[nr][nc] != '#' and (nr, nc) not in lookup):
                continue
            lookup.add((nr, nc))
            q.append((d+1, (nr, nc)))
    assert(False)

def can_remove(M, p):
    r, c = p
    if not (0 < r < len(M)-1 and 0 < c < len(M[0])-1):
        return False
    if M[r][c] != '#':
        return False
    if M[r-1][c-1] != '#' and M[r-1][c] == '#' and M[r][c-1] == '#':
        return False
    if M[r-1][c+1] != '#' and M[r-1][c] == '#' and M[r][c+1] == '#':
        return False
    if M[r+1][c-1] != '#' and M[r+1][c] == '#' and M[r][c-1] == '#':
        return False
    if M[r+1][c+1] != '#' and M[r+1][c] == '#' and M[r][c+1] == '#':
        return False     
    cnt, pair = 0, 0
    for i, (dr, dc) in enumerate(islice(DIRECTIONS, 4)):
        nr, nc = r+dr, c+dc
        if M[nr][nc] == '#':
            cnt += 1
            pair ^= i
    return cnt == 0 or cnt == 1 or \
           (cnt == 2 and (pair & 1))  # cnt == 2 and (pair&1) means only (left, up), (up, right),
                                      # (right, down), (down, left) exist walls

def find_remove_list_in_order(M, S, F):
    remove_list = []
    q = deque()
    lookup = set()
    for r in xrange(len(M)):
        for c in xrange(len(M[0])):
            if not can_remove(M, (r, c)):
                continue
            lookup.add((r, c))
            q.append((r, c))
    while q:
        (r, c) = q.popleft()
        if not can_remove(M, (r, c)):
            lookup.remove((r, c))  # make it able to remove in the future
            continue
        remove_list.append((r, c))
        M[r][c] = '.'
        for dr, dc in DIRECTIONS:
            nr, nc = r+dr, c+dc
            if not (0 <= nr < len(M) and 0 <= nc < len(M[0]) and
                    can_remove(M, (nr, nc)) and (nr, nc) not in lookup):
                continue
            lookup.add((nr, nc))
            q.append((nr, nc))
    return remove_list

def apply_remove_list(M, remove_list, l):
    for i, (r, c) in enumerate(remove_list):
        M[r][c] = '.' if i < l else '#'

def binary_search_for_remove_list_length(M, S, F, D, remove_list):
    left, right = 0, len(remove_list)
    while left <= right:
        mid = left + (right-left)//2
        apply_remove_list(M, remove_list, mid)
        if not (shortest_distance(M, S, F) >= D):
            right = mid-1
        else:
            left = mid+1
    return right

def is_invalid(M, p):
    r, c = p
    if not (0 <= r < len(M)-1 and 0 <= c < len(M[0])-1):
        return False
    if M[r][c] == '#' and M[r+1][c+1] == '#' and \
       M[r][c+1] != '#' and M[r+1][c] != '#':
        return True
    if M[r][c+1] == '#' and M[r+1][c] == '#' and \
       M[r][c] != '#' and M[r+1][c+1] != '#':
        return True
    return False

def check(M, S, F, D):
    return not any(is_invalid(M, (r, c)) for r in xrange(len(M)) for c in xrange(len(M[0]))) and \
           shortest_distance(M, S, F) == D

def map_reduce():
    R, C, D = map(int, raw_input().strip().split())
    M = []
    S, F = None, None
    for r in xrange(R):
        M.append(list(raw_input().strip()))
        for c in xrange(C):
            if M[r][c] == 'S':
                S = (r, c)
                M[r][c] = '.'
            elif M[r][c] == 'F':
                F = (r, c)
                M[r][c] = '.'
    min_d, curr_d = manhattan_distance(S, F), shortest_distance(M, S, F)
    if not (min_d <= D <= curr_d and curr_d%2 == D%2):
        return "IMPOSSIBLE"
    remove_list = find_remove_list_in_order(M, S, F)
    l = binary_search_for_remove_list_length(M, S, F, D, remove_list)
    apply_remove_list(M, remove_list, l)
    if not check(M, S, F, D):
        assert(False)
    M[S[0]][S[1]], M[F[0]][F[1]] = 'S', 'F'
    result = ["POSSIBLE"]
    result.extend(imap(lambda x: "".join(x), M))
    return "\n".join(result)

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1),
              (-1, 1), (1, 1), (1, -1), (-1, -1)] 
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, map_reduce())
