# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 1B - Problem C. Technobabble
# https://code.google.com/codejam/contest/11254486/dashboard#s=p2
#
# Time:  O(N * sqrt(W))
# Space: O(W)
#

from collections import defaultdict

# Source code from http://code.activestate.com/recipes/123641-hopcroft-karp-bipartite-matching/
# Hopcroft-Karp bipartite max-cardinality matching and max independent set
# David Eppstein, UC Irvine, 27 Apr 2002
def bipartiteMatch(graph):
    '''Find maximum cardinality matching of a bipartite graph (U,V,E).
    The input format is a dictionary mapping members of U to a list
    of their neighbors in V.  The output is a triple (M,A,B) where M is a
    dictionary mapping members of V to their matches in U, A is the part
    of the maximum independent set in U, and B is the part of the MIS in V.
    The same object may occur in both U and V, and is treated as two
    distinct vertices if this happens.'''
    
    # initialize greedy matching (redundant, but faster than full search)
    matching = {}
    for u in graph:
        for v in graph[u]:
            if v not in matching:
                matching[v] = u
                break
    
    while 1:
        # structure residual graph into layers
        # pred[u] gives the neighbor in the previous layer for u in U
        # preds[v] gives a list of neighbors in the previous layer for v in V
        # unmatched gives a list of unmatched vertices in final layer of V,
        # and is also used as a flag value for pred[u] when u is in the first layer
        preds = {}
        unmatched = []
        pred = dict([(u,unmatched) for u in graph])
        for v in matching:
            del pred[matching[v]]
        layer = list(pred)
        
        # repeatedly extend layering structure by another pair of layers
        while layer and not unmatched:
            newLayer = {}
            for u in layer:
                for v in graph[u]:
                    if v not in preds:
                        newLayer.setdefault(v,[]).append(u)
            layer = []
            for v in newLayer:
                preds[v] = newLayer[v]
                if v in matching:
                    layer.append(matching[v])
                    pred[matching[v]] = v
                else:
                    unmatched.append(v)
        
        # did we finish layering without finding any alternating paths?
        if not unmatched:
            unlayered = {}
            for u in graph:
                for v in graph[u]:
                    if v not in preds:
                        unlayered[v] = None
            return (matching,list(pred),list(unlayered))

        # recursively search backward through layers to find alternating paths
        # recursion returns true if found path, false otherwise
        def recurse(v):
            if v in preds:
                L = preds[v]
                del preds[v]
                for u in L:
                    if u in pred:
                        pu = pred[u]
                        del pred[u]
                        if pu is unmatched or recurse(pu):
                            matching[v] = u
                            return 1
            return 0

        for v in unmatched: recurse(v)


def technobabble():
    N = input()
    U, V, E = set(), set(), defaultdict(list)
    for _ in xrange(N):
        s1, s2 = raw_input().strip().split()
        U.add(s1)
        V.add(s2)
        E[s1].append(s2)

    # Hopcroft-Karp algorithm
    # Time:  O(E * sqrt(V))
    # Space: O(V)
    M, _, _ = bipartiteMatch(E)

    # The answer is total number of edges (topics) minus the size of a minimum edge cover.
    # - total number of edges = N
    # - (1) the size of minimum edge cover = (the number of edges in a maximum matching) + 
    #                                        (the number of vertices not included in a maximum matching)
    #   (2) 2 * (the number of edges in a maximum matching) + 
    #       (the number of vertices not included in a maximum matching) = |U| + |V|
    #
    #   (1) + (2) <=> the size of minimum edge cover = |U| + |V| - (the number of edges in a maximum matching)
    return N - (len(U) + len(V) - len(M))


for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, technobabble())

