# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 2 - Problem D. initial_edgesform Factory
# https://code.google.com/codejam/contest/10224486/dashboard#s=p3
#
# Time:  O(2^N)
# Space: O(2^N)
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
    groups.sort(key=lambda g: max(g[0], g[1]))
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

    groups = []
    for i in xrange(N):
        groups.append(set(['w_' + str(i)]))
        groups.append(set(['m_' + str(i)]))

    # Group connected components.
    initial_edges = 0
    for w in xrange(N):
        accessible_machines = map(int, list(raw_input().strip()))
        new_group = set(['w_' + str(w)])
        for m in xrange(N):
            if accessible_machines[m-1]:
                initial_edges += 1
                new_group.add('m_' + str(m))
        groups_to_merge = []
        for group in groups:
            group_acquired = False
            for elem in new_group:
                if group_acquired:
                    continue
                if elem in group:
                    groups_to_merge.append(group)
                    group_acquired = True
        for group in groups_to_merge:
            groups.remove(group)
            new_group = new_group.union(group)
        groups.append(new_group)

    new_groups = []
    for group in groups:
        g = [0,0]
        for elem in group:
            if elem[0] == 'w':
                g[0] += 1
            else:
                g[1] += 1
        new_groups.append((g[0], g[1]))

    # Every maximal matching is perfect if and only if
    # each connected component of the bipartite graph is a complete bipartite graph
    # with same number of vertices in each part.
    min_edges = dfs(tuple(new_groups))

    # The number of added edges is the total number of edges in the resulting graph
    # minus the number edges we have initially.
    return min_edges - initial_edges


for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, freeform_factory())
