# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2016 World Finals - Problem A. Integeregex
# https://code.google.com/codejam/contest/7234486/dashboard#s=p0
#
# Time:  O(R^2 + RlogB)
# Space: O(R)
#

from collections import defaultdict

def make_state(state_count):
    state_count[0] += 1
    return "s{}".format(state_count[0])  # make state more readable

def make_E_NFA(R, start, state_count, transitions):
    initial_state, final_state = make_state(state_count), make_state(state_count)
    assert(state_count[0] <= 2*len(R))
    i = start[0]
    if R[start[0]].isdigit():
        start[0] += 1
        transitions[initial_state][int(R[start[0]-1])] = set([final_state])
    else:
        assert(R[start[0]] == '(')
        start[0] += 1
        while R[start[0]-1] in "(|":
            new_initial_state, new_final_state = make_NFA(R, start, state_count, transitions)
            if start[0]+1 != len(R) and R[start[0]:start[0]+2] == ")*":
                start[0] += 2  # repetition
                transitions[initial_state][''] |= set([new_initial_state, final_state])
                transitions[new_final_state][''] = set([new_initial_state, final_state])
                break
            assert(R[start[0]] in "|)")
            start[0] += 1  # disjunction
            transitions[initial_state][''] |= set([new_initial_state])
            transitions[new_final_state][''] = set([final_state])
    return initial_state, final_state

# Thompson's construction, reference: https://www.researchgate.net/profile/Shin-ichi_Minato/publication/221580042/figure/fig1/AS:341447451660288@1458418824089/The-construction-of-Thompson-automata-TNFAs.png
def make_NFA(R, start, state_count, transitions):  # Time: O(R), Space: O(R)
    initial_state, final_state = None, None
    i = start[0]
    while start[0] != len(R) and (R[start[0]] == '(' or R[start[0]].isdigit()):
        new_initial_state, new_final_state = make_E_NFA(R, start, state_count, transitions)  # concatenation
        if initial_state is None:
            initial_state = new_initial_state
        if final_state is not None:
            transitions[final_state][''] = set([new_initial_state])
        final_state = new_final_state
    return initial_state, final_state

def expand_epsilon_reached_states(transitions, final_state):  # Time: O(R^2), Space: O(R)
    def dfs(start_state, curr_state, transitions, lookup):
        for state in set(transitions[curr_state]['']):
            if state in lookup:
                continue
            lookup.add(state)
            dfs(start_state, state, transitions, lookup)
        transitions[start_state][''].add(curr_state)

    for state in transitions.keys():
        dfs(state, state, transitions, set())
    transitions[final_state][''] = set([final_state])

def match_NFA(X, transitions, initial_state, final_state):  # Time: O(RlogB), Space: O(R)
    x_digits = map(int, list(str(X)))
    count_state = {(True, True, frozenset([initial_state])):1}
    for index in xrange(len(x_digits)):  # O(logB) times
        new_count_state = defaultdict(int)
        new_count_state[True, False, frozenset([initial_state])] = 1
        assert(len(count_state) <= len(transitions))
        for (is_empty, is_prefix_of_x, states), count in count_state.iteritems():  # O(R) times
            for new_digit in xrange(10):
                if is_empty and new_digit == 0:
                    continue  # numbers can't start with 0
                if is_prefix_of_x and new_digit > x_digits[index]:
                    continue  # numbers can't be greater than X
                new_possible_states = set()
                for start_state in states:  # find all possible states if new_digit was next in the string
                    for epsilon_state in transitions[start_state]['']:
                        new_possible_states |= transitions[epsilon_state][new_digit]
                if not new_possible_states:
                    continue
                new_count_state[False, is_prefix_of_x and new_digit == x_digits[index], frozenset(new_possible_states)] += count
        count_state = new_count_state
    count_match = 0
    for (_, _, states), count in count_state.iteritems():
        if any(final_state in transitions[end_state][''] for end_state in states):
            count_match += count
    return count_match

def integeregex():
    A, B = map(int, raw_input().strip().split())
    R = raw_input().strip()
    transitions = defaultdict(lambda: defaultdict(set))
    initial_state, final_state = make_NFA(R, [0], [0], transitions)
    expand_epsilon_reached_states(transitions, final_state)
    return match_NFA(B, transitions, initial_state, final_state) - \
           match_NFA(A-1, transitions, initial_state, final_state)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, integeregex())
