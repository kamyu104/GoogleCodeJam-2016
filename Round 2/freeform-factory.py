# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 2 - Problem D. Freeform Factory
# https://code.google.com/codejam/contest/10224486/dashboard#s=p3
#
# Time:  O(N + C * C!), C is the number of connected components.
# Space: O(N + C * C!)
#

from collections import Hashable, defaultdict
from functools import partial

class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if not isinstance(args, Hashable):
            # uncacheable. a list, for instance.
            # better to not cache than blow up.
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return partial(self.__call__, obj)


class UnionFind(object):
    def __init__(self, n):
        self.set = range(n)
        self.count = n

    def find_set(self, x):
       if self.set[x] != x:
           self.set[x] = self.find_set(self.set[x])  # path compression.
       return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root != y_root:
            self.set[min(x_root, y_root)] = max(x_root, y_root)
            self.count -= 1


@memoized
def dfs(group_pairs):
    # Count the sum of squares of rs.
    edges_count = 0
    cur_group_pairs = list(group_pairs)
    for group_pair in list(group_pairs):
        if group_pair[0] == group_pair[1]:
            edges_count += group_pair[0] ** 2
            cur_group_pairs.remove(group_pair)
    if not cur_group_pairs:
        return edges_count

    # Choose the largest one to merge.
    group_pair_to_merge = cur_group_pairs.pop()

    # DFS
    min_edges_count = float("inf")
    for group_pair in set(cur_group_pairs):
        next_group_pairs = list(cur_group_pairs)
        merged_group_pair = (group_pair_to_merge[0] + group_pair[0], \
                             group_pair_to_merge[1] + group_pair[1])
        next_group_pairs.remove(group_pair)
        next_group_pairs.append(merged_group_pair)
        min_edges_count = min(min_edges_count, \
                              edges_count + dfs(tuple(next_group_pairs)))
    return min_edges_count


# We are given a bipartite graph with N vertices in each part,
# and need to add the smallest amount of edges to this graph to
# guarantee that every maximal matching is a perfect matching.
def freeform_factory():
    N = input()

    # Group connected components.
    union_find = UnionFind(2 * N)
    initial_edges_count = 0
    for i in xrange(N):
        for j, accessible in enumerate(map(int, list(raw_input().strip()))):
            if accessible:
                initial_edges_count += 1
                union_find.union_set(i, N + j)

    groups_dict = defaultdict(lambda:[0, 0])
    for i in xrange(2 * N):
        groups_dict[union_find.find_set(i)][i >= N] += 1
    group_pairs = map(tuple, groups_dict.values())

    # Every maximal matching is perfect if and only if
    # each connected component of the bipartite graph is a complete bipartite graph
    # with same number of vertices in each part.
    # => We try to construct this kind of graph with less number of edges as possible.
    group_pairs.sort(key=lambda g: max(g[0], g[1]))
    min_edges_count = dfs(tuple(group_pairs))

    # The number of added edges is the total number of edges in the resulting graph
    # minus the number edges we have initially.
    return min_edges_count - initial_edges_count


for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, freeform_factory())
