# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 1A - Problem C. BFFs
# https://code.google.com/codejam/contest/4304486/dashboard#s=p2
#
# Time:  O(N^2)
# Space: O(N)
#

def BFFs():
    N = input()
    F = [int(c) - 1 for c in raw_input().strip().split()]

    # longest_len_begins_with_kid[i] denotes the longest length from the kid i.
    longest_len_begins_with_kid =[0] * N

    # first_kid_in_a_circle_from_kid[i] denotes the index of the first kid in
    # the circle from the kid i.
    first_kid_in_a_circle_from_kid = [0] * N

    for i in xrange(N):
        used = set()
        cur, length = i, 0
        while cur not in used:
            length += 1
            used.add(cur)
            cur = F[cur]
        longest_len_begins_with_kid[i], first_kid_in_a_circle_from_kid[i] = length, cur

    # longest_len_to_kid[i] denotes the longest length ends with the kid i.
    longest_len_to_kid = [0] * N

    for i in xrange(N):
        cur = first_kid_in_a_circle_from_kid[i]
        longest_len_to_kid[cur] = max(longest_len_to_kid[cur], \
                                      longest_len_begins_with_kid[i] - longest_len_begins_with_kid[cur] + 1)

    chains, circle = 0, 0
    used = set()
    for i in xrange(N):
        # Only check an unused kid in a circle.
        if i not in used and first_kid_in_a_circle_from_kid[i] == i:
            # Count the length of the circle and mark the kids in it as used.
            vals, cur = [], i
            while cur not in used:
                used.add(cur)
                vals.append(longest_len_to_kid[cur])
                cur = F[cur]

            # Type 1: update the max length of the 2 chains
            #         connected with a circle of which length is 2.
            #         Type 1 looks like:
            #
            #         ->->->->->O<-<-<-<-<-
            #                  ^^^
            #           the circle length is 2
            if len(vals) == 2:
                chains += vals[0] + vals[1]

            # Type 2: update the max length of the circle.
            #         Type 2 looks like:
            #
            #                   O
            #                  ^^^
            #               only a circle
            circle = max(circle, len(vals))

    return max(chains, circle)


for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, BFFs())
