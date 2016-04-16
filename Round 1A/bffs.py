# Copyright (c) 2016 kamyu. All rights reserved.
#
# Google Code Jam 2016 Round 1A - Problem C. BFFs
# https://code.google.com/codejam/contest/4304486/dashboard#s=p2
#
# Time:  O(N)
# Space: O(N)
#

# Time:  O(N)
# Space: O(N)
def compute(N, F, used, longest_len_from_kid, first_kid_in_a_circle_from_kid):
    for i in xrange(N):
        if i not in used:
            cur, length = i, 0
            while cur not in used:
                length += 1
                used.add(cur)
                cur = F[cur]
            if longest_len_from_kid[cur]:  # Compute from the visited kid.
                used_kid = cur
                cur = i
                while cur != used_kid:
                    first_kid_in_a_circle_from_kid[cur] = \
                                        first_kid_in_a_circle_from_kid[used_kid]
                    longest_len_from_kid[cur] = \
                                        length + longest_len_from_kid[used_kid]
                    length -= 1
                    cur = F[cur]
            else:
                first_kid_in_a_circle = cur
                cur, is_through_first_kid_in_a_circle = i, False
                while not is_through_first_kid_in_a_circle or \
                      cur != first_kid_in_a_circle:
                    if cur == first_kid_in_a_circle:
                        is_through_first_kid_in_a_circle = True
                    # Update the kid in the chain.
                    if not is_through_first_kid_in_a_circle:
                        first_kid_in_a_circle_from_kid[cur] = \
                                        first_kid_in_a_circle
                        longest_len_from_kid[cur] = length
                        length -= 1
                    else:  # Update the kid in the circle.
                        first_kid_in_a_circle_from_kid[cur] = cur
                        longest_len_from_kid[cur] = length
                    cur = F[cur]


# Time:  O(N^2)
# Space: O(N)
def compute2(N, F, used, longest_len_from_kid, first_kid_in_a_circle_from_kid):
    for i in xrange(N):
        used = set()
        cur, length = i, 0
        while cur not in used:
            length += 1
            used.add(cur)
            cur = F[cur]
        longest_len_from_kid[i], first_kid_in_a_circle_from_kid[i] = length, cur


def BFFs():
    N = input()
    F = [int(c) - 1 for c in raw_input().strip().split()]

    # longest_len_from_kid[i] denotes the longest length from the kid i.
    longest_len_from_kid =[0] * N

    # first_kid_in_a_circle_from_kid[i] denotes the index of the first kid in
    # the circle from the kid i.
    first_kid_in_a_circle_from_kid = [0] * N

    # Compute longest_len_from_kid and first_kid_in_a_circle_from_kid by used.
    used = set()
    compute(N, F, used, longest_len_from_kid, first_kid_in_a_circle_from_kid)

    # longest_len_to_kid[i] denotes the longest length to the kid i.
    longest_len_to_kid = [0] * N

    for i in xrange(N):
        cur = first_kid_in_a_circle_from_kid[i]
        longest_len_to_kid[cur] = max(longest_len_to_kid[cur], \
                                      longest_len_from_kid[i] - \
                                      longest_len_from_kid[cur] + 1)

    chains, circle = 0, 0
    used = set()
    for i in xrange(N):
        # Only check an unused kid in a circle.
        if i not in used and first_kid_in_a_circle_from_kid[i] == i:
            # Count the length of the circle and mark the kids in it as used.
            lens, cur = [], i
            while cur not in used:
                used.add(cur)
                lens.append(longest_len_to_kid[cur])
                cur = F[cur]

            # Type 1: update the max length of the 2 chains
            #         connected with a circle of which length is 2.
            #         Type 1 looks like:
            #
            #         ->->->->->O<-<-<-<-<- ... ->->->->->O<-<-<-<-<-
            #                  ^^^                  ^^^
            #                   the circle length is 2
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
    print 'Case #%d: %s' % (case+1, BFFs())
