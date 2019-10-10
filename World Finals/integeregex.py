# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2016 World Finals - Problem A. Integeregex
# https://code.google.com/codejam/contest/7234486/dashboard#s=p0
#
# Time:  O(R)
# Space: O(R)
#

from collections import defaultdict

def make_state(state_count):
    state = "s{}".format(state_count[0])
    state_count[0] += 1
    return state

def make_E_NFA(R, start, state_count, transitions):
    initial_state, final_state = make_state(state_count), make_state(state_count)
    i = start[0]
    if R[start[0]].isdigit():
        transitions[initial_state][int(R[start[0]])] = set([final_state])
        start[0] += 1
    else:
        assert(R[start[0]] == '(')
        start[0] += 1
        transitions[initial_state][''] = set()
        while True:
            prev_start = start[0]
            new_initial_state, new_final_state = make_NFA(R, start, state_count, transitions)
            if not new_initial_state or not new_final_state:
                break
            if start[0]+1 != len(R) and R[start[0]:start[0]+2] == ")*":
                # repetition
                start[0] += 2
                transitions[new_final_state][''] = set([new_initial_state, final_state])
                transitions[initial_state][''] |= set([new_initial_state, final_state])
                break
            assert(R[start[0]] in ")|")
            start[0] += 1
            transitions[initial_state][''].add(new_initial_state)
            transitions[new_final_state][''] = set([final_state])
            if R[start[0]-1] == ')':
                break
    # print "make_E_NFA:", R[i:start[0]]
    return initial_state, final_state

# Thompson's construction
def make_NFA(R, start, state_count, transitions):
    initial_state, final_state = None, None
    i = start[0]
    while start[0] != len(R) and (R[start[0]] == '(' or R[start[0]].isdigit()):
        # concatenation
        new_initial_state, new_final_state = make_E_NFA(R, start, state_count, transitions)
        if initial_state is None:
            initial_state = new_initial_state
        if final_state is not None:
            transitions[final_state][''] = set([new_initial_state])
        final_state = new_final_state
    # print "make_NFA:  ", R[i:] if start[0] == len(R) else R[i:start[0]]
    return initial_state, final_state

def expand_epsilon_transitions(transitions, final_state):
    def dfs(start_state, transitions, lookup=set()):
        epsilon_set = set()
        for state in transitions[start_state]['']:
            if state not in lookup:
                lookup.add(state)
                dfs(state, transitions, lookup)
            epsilon_set |= transitions[state]['']
        epsilon_set.add(start_state)
        transitions[start_state][''] = epsilon_set

    for state in transitions.keys():
        dfs(state, transitions)
    transitions[final_state][''] = set([final_state])

def match_NFA(X, transitions, initial_state, final_state):
    x_digits = map(int, list(str(X)))
    count_state = {(True, True, frozenset([initial_state])):1}
    for index in xrange(len(x_digits)):
        new_count_state = defaultdict(int)
        new_count_state[True, False, frozenset([initial_state])] = 1
        for (is_empty, is_prefix_of_x, states), count in count_state.iteritems():
            for new_digit in xrange(10):
                if is_empty and new_digit == 0:
                    continue  # numbers can't start with 0.
                if is_prefix_of_x and new_digit > x_digits[index]:
                    continue  # numbers can't be greater than X.
                # find all possible states if new_digit was next in the string
                new_possible_states = set()
                for start_state in states:
                    for epsilon_state in transitions[start_state]['']:
                        new_possible_states |= transitions[epsilon_state][new_digit]
                if not new_possible_states:
                    continue
                new_count_state[False, is_prefix_of_x and new_digit == x_digits[index], frozenset(new_possible_states)] += count
        count_state = new_count_state
    count_match = 0
    for (_, _, states), count in count_state.iteritems():
        for end_state in states:
            if final_state in transitions[end_state]['']:
                count_match += count
    #print count_state, initial_state, final_state
    return count_match

def integeregex():
    A, B = map(int, raw_input().strip().split())
    R = raw_input().strip()
    #print R
    transitions = defaultdict(lambda: defaultdict(set))
    initial_state, final_state = make_NFA(R, [0], [0], transitions)
    expand_epsilon_transitions(transitions, final_state)
    #print R, transitions, initial_state, final_state
    return match_NFA(B, transitions, initial_state, final_state) - \
           match_NFA(A-1, transitions, initial_state, final_state)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, integeregex())