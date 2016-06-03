# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 2 - Problem D. initial_edgesform Factory
# https://code.google.com/codejam/contest/10224486/dashboard#s=p3
#
# Time:  O(N + C * C!), C is the number of connected components.
# Space: O(N + C * C!)
#

import collections
import functools

class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
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
        return functools.partial(self.__call__, obj)


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
def dfs(groups):
    # Count the sum of squares of rs.
    edges = 0
    groups = list(groups)
    for group in list(groups):
        if group[0] == group[1]:
            edges += group[0] ** 2
            groups.remove(group)
    if not groups:
        return edges

    # Choose the largest one to merge.
    group_to_merge = groups.pop()

    # DFS
    min_edges = float("inf")
    for group in set(groups):
        new_groups = list(groups)
        merged_group = (group_to_merge[0] + group[0], group_to_merge[1] + group[1])
        new_groups.remove(group)
        new_groups.append(merged_group)
        min_edges = min(min_edges, edges + dfs(tuple(new_groups)))
    return min_edges


# We are given a bipartite graph with N vertices in each part,
# and need to add the smallest amount of edges to this graph to
# guarantee that every maximal matching is a perfect matching.
def freeform_factory():
    N = input()

    # Group connected components.
    union_find = UnionFind(2 * N)
    initial_edges = 0
    for i in xrange(N):
        for j, accessible in enumerate(map(int, list(raw_input().strip()))):
            if accessible:
                initial_edges += 1
                union_find.union_set(i, N + j)

    groups = collections.defaultdict(lambda:[0, 0])
    for i in xrange(2 * N):
        groups[union_find.find_set(i)][i >= N] += 1
    new_groups = map(tuple, groups.values())

    # Every maximal matching is perfect if and only if
    # each connected component of the bipartite graph is a complete bipartite graph
    # with same number of vertices in each part.
    # => We try to construct this kind of graph with less number of edges as possible.
    new_groups.sort(key=lambda g: max(g[0], g[1]))
    min_edges = dfs(tuple(new_groups))

    # The number of added edges is the total number of edges in the resulting graph
    # minus the number edges we have initially.
    return min_edges - initial_edges


for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, freeform_factory())
