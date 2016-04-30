# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 1A - Problem C. BFFs
# https://code.google.com/codejam/contest/4304486/dashboard#s=p2
#
# Time:  O(N)
# Space: O(N)
#

from collections import defaultdict

# Time:  O(N)
# Space: O(N)
# Optimized computation for longest_len_from_kid and first_kid_in_a_circle_from_kid.
def compute(N, F, visited, longest_len_from_kid, first_kid_in_a_circle_from_kid):
    for i in xrange(N):
        if i not in visited:
            cur, length = i, 0
            while cur not in visited:
                length += 1
                visited.add(cur)
                cur = F[cur]

            visited_kid = cur
            is_visited_kid_uninitiated = (longest_len_from_kid[visited_kid] == 0)
            if is_visited_kid_uninitiated:  # if visited_kid not initiated.
                first_kid_in_a_circle_from_kid[visited_kid] = visited_kid

            cur, is_before_the_circle = i, True
            while (is_visited_kid_uninitiated and is_before_the_circle) or \
                  cur != visited_kid:
                # Go through into the circle only if
                # the visited kid hasn't been initiated.
                if cur == visited_kid:
                    is_before_the_circle = False
                # Update the kids in the chain.
                if is_before_the_circle:
                    first_kid_in_a_circle_from_kid[cur] = \
                                    first_kid_in_a_circle_from_kid[visited_kid]
                    longest_len_from_kid[cur] = \
                                    length + longest_len_from_kid[visited_kid]
                    length -= 1
                else:  # Update the kids in the circle.
                    first_kid_in_a_circle_from_kid[cur] = cur
                    longest_len_from_kid[cur] = length
                cur = F[cur]


# Time:  O(N^2)
# Space: O(N)
# Easier implementation but slower computation for
# longest_len_from_kid and first_kid_in_a_circle_from_kid.
# It can pass the judge of the code jam.
def compute2(N, F, visited, longest_len_from_kid, first_kid_in_a_circle_from_kid):
    for i in xrange(N):
        visited = set()
        cur, length = i, 0
        while cur not in visited:
            length += 1
            visited.add(cur)
            cur = F[cur]
        longest_len_from_kid[i], first_kid_in_a_circle_from_kid[i] = length, cur


def bffs():
    N = input()
    F = map(lambda c: int(c) - 1, raw_input().strip().split())

    # longest_len_from_kid[i] denotes the longest length from the kid i.
    longest_len_from_kid = [0] * N

    # first_kid_in_a_circle_from_kid[i] denotes the index of the first kid in
    # the circle from the kid i.
    first_kid_in_a_circle_from_kid = [0] * N

    # Compute longest_len_from_kid and first_kid_in_a_circle_from_kid by visited.
    visited = set()
    compute(N, F, visited, longest_len_from_kid, first_kid_in_a_circle_from_kid)

    # longest_len_to_kid[i] denotes the longest length to the kid i
    # which resides in a cricle.
    longest_len_to_first_kid_in_a_circle = defaultdict(int)
    for i in xrange(N):
        cur = first_kid_in_a_circle_from_kid[i]
        longest_len_to_first_kid_in_a_circle[cur] = \
            max(longest_len_to_first_kid_in_a_circle[cur], \
                longest_len_from_kid[i] - longest_len_from_kid[cur] + 1)

    chains, circle = 0, 0
    visited = set()
    for i in xrange(N):
        # Only check an unvisited kid in a circle.
        if i not in visited and first_kid_in_a_circle_from_kid[i] == i:
            # Count the length of the circle and mark the kids in it as visited.
            lens, cur = [], i
            while cur not in visited:
                visited.add(cur)
                lens.append(longest_len_to_first_kid_in_a_circle[cur])
                cur = F[cur]

            # Type 1: update the sum of the lengths of the 2 chains
            #         connected with a circle of which length is 2.
            #         Type 1 looks like:
            #
            #         ->->->->->O<-<-<-<-<- ... ->->->->->O<-<-<-<-<-
            #                  ^^^                       ^^^
            #         the circle length is 2    the circle length is 2
            if len(lens) == 2:
                chains += lens[0] + lens[1]

            # Type 2: update the max length of the circle.
            #         Type 2 looks like:
            #
            #                   O
            #                  ^^^
            #              only a circle
            circle = max(circle, len(lens))

    return max(chains, circle)


for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, bffs())
