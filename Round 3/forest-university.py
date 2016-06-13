# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 3 - Problem B. Forest University
# https://code.google.com/codejam/contest/3224486/dashboard#s=p1
#
# Time:  O(T * N^2), T is the times of samplings.
# Space: O(N)
#

from random import randint

def sample(children, children_size, name):
    sequence = []

    stack, left_cnt = [0], len(children)
    while stack:
        k = randint(1, left_cnt)

        # Find the parent of the kth remaining courses.
        cnt = 0
        for i in xrange(len(stack)):
            cnt += children_size[stack[i]]
            if cnt >= k: break
        chosen = stack[i]

        # Add the chosen course to the sequence.
        sequence.append(name[chosen])

        # Expand the chosen course to the children courses.
        del stack[i]
        stack.extend(children[chosen])
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

    children_size = [1] * (N+1)
    done = 0
    while done < N:
        for i in xrange(N+1):
            if children_tmp[i] == set():
                children_size[parent[i]] += children_size[i]
                children_tmp[parent[i]].remove(i)
                children_tmp[i] = None
                done += 1

    times = 3000
    for _ in xrange(times):
        sequence = sample(children, children_size, name)
        for i in xrange(M):
            if cool[i] in sequence: cnts[i] += 1

    return " ".join(map(str, [1.0 * cnts[i] / times for i in xrange(M)]))


for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, forest_university())