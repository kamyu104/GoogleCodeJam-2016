# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2016 World Finals - Problem A. Integeregex
# https://code.google.com/codejam/contest/7234486/dashboard#s=p0
#
# Time:  O(R^2 + RlogB) on average, worst: O(R^2 + (2^R)logB)
# Space: O(R) on average, worst: O(2^R)
#

from collections import defaultdict

def make_state(state_count):
    state_count[0] += 1
    return "s{}".format(state_count[0])  # make state more readable

def make_Ei_NFA(R, start, state_count, transitions):
    initial_state, final_state = make_state(state_count), make_state(state_count)
    assert(state_count[0] <= 2*len(R))
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
    while start[0] != len(R) and (R[start[0]] == '(' or R[start[0]].isdigit()):
        new_initial_state, new_final_state = make_Ei_NFA(R, start, state_count, transitions)  # concatenation
        if initial_state is None:
            initial_state = new_initial_state
        if final_state is not None:
            transitions[final_state][''] = set([new_initial_state])
        final_state = new_final_state
    return initial_state, final_state

def make_epsilon_reached_NFA(transitions, final_state):  # Time: O(R^2), Space: O(R)
    def dfs(transitions, curr_state, lookup, epsilon_reached_states):
        for state in transitions[curr_state]['']:
            if state in lookup:
                continue
            lookup.add(state)
            dfs(transitions, state, lookup, epsilon_reached_states)
        epsilon_reached_states.add(curr_state)

    transitions[final_state][''] = set([final_state])  # create key first to avoid changing size of keys below
    for state in transitions.iterkeys():
        epsilon_reached_states = set()
        dfs(transitions, state, set(), epsilon_reached_states)
        transitions[state][''] = epsilon_reached_states

def match_NFA(transitions, initial_state, final_state, X):  # Time: O(RlogB) ~ O((2^R)logB), Space: O(R) ~ O(2^R), ps. NFA for exact string matching rather than range count is only Time: O(RlogB), Space: O(R)
    x_digits = map(int, list(str(X)))
    count_state = {(True, True, frozenset([initial_state])):1}
    for index in xrange(len(x_digits)):  # O(logB) times
        new_count_state = defaultdict(int)
        new_count_state[True, False, frozenset([initial_state])] = 1
        assert(len(count_state) <= len(transitions))  # for extreme case, it would be more than 10*R, worst to O(2^R)
        for (is_empty, is_prefix_of_x, states), count in count_state.iteritems():  # O(R) times on normal case
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
            count_match += count  # NFA matching may include empty string, which would be excluded after substraction
    return count_match

def integeregex():
    A, B = map(int, raw_input().strip().split())
    R = raw_input().strip()
    transitions = defaultdict(lambda: defaultdict(set))
    initial_state, final_state = make_NFA(R, [0], [0], transitions)
    make_epsilon_reached_NFA(transitions, final_state)
    return match_NFA(transitions, initial_state, final_state, B) - \
           match_NFA(transitions, initial_state, final_state, A-1)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, integeregex())
