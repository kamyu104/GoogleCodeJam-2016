# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 3 - Problem B. Forest University
# https://code.google.com/codejam/contest/3224486/dashboard#s=p1
#
# Time:  O(T * N^2), T is the times of samplings.
# Space: O(N)
#

from random import randint
from math import ceil

def sample(children, descendants_cnt, name):
    sequence = []

    candidates, left_cnt = [0], len(children)
    while candidates:
        k = randint(1, left_cnt)

        # Uniformly choose the candidate course by its weight.
        # The weight of a candidate course is proportional to its descendants_cnt.
        # In other words, randomly find a remaining course and
        # choose its prerequisite course in candidates.
        cnt = 0
        for i in xrange(len(candidates)):
            cnt += descendants_cnt[candidates[i]]
            if cnt >= k: break
        chosen = candidates[i]

        # Add the chosen course to the sequence.
        sequence.append(name[chosen])

        # Expand the chosen course to the children courses.
        del candidates[i]
        candidates.extend(children[chosen])
        left_cnt -= 1

    return "".join(sequence)

def forest_university():
    N = input()
    parent = [-1] + map(int, raw_input().strip().split())
    name = "^" + raw_input().strip()
    M = input()
    cool = raw_input().strip().split()
    cnts = [0] * M

    children = [set() for _ in xrange(N+1)]
    children_tmp = [set() for _ in xrange(N+1)]
    for i in xrange(1, N+1):
        children[parent[i]].add(i)
        children_tmp[parent[i]].add(i)

    descendants_cnt = [1] * (N+1)
    left_cnt = N
    while left_cnt:
        for i in xrange(1, N+1):
            if children_tmp[i] == set():
                descendants_cnt[parent[i]] += descendants_cnt[i]
                children_tmp[parent[i]].remove(i)
                children_tmp[i] = None
                left_cnt -= 1

    # 1. sigma = sqrt(p * (1-p) / times) <= 0.5 / sqrt(times)
    #    (https://en.wikipedia.org/wiki/Binomial_distribution#Normal_approximation)
    # 2. precision / sigma >= 6 means error rate < 2e-7
    #    (https://en.wikipedia.org/wiki/Standard_deviation)
    #
    # 1 & 2 => 3e-2 / sigma >= 6
    #       => 3e-2 / 0.5 * sqrt(times) >= 6
    #       => sqrt(times) >= 6 * 0.5 / 3e-2
    #       => times >= (6 * 0.5 / 3e-2) ** 2
    times = int(ceil((6 * 0.5 / 3e-2) ** 2))

    for _ in xrange(times):
        sequence = sample(children, descendants_cnt, name)
        for i in xrange(M):
            if cool[i] in sequence: cnts[i] += 1

    return " ".join(map(str, [1.0 * cnt / times for cnt in cnts]))


for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, forest_university())
