# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2016 World Finals - Problem A. Integeregex
# https://code.google.com/codejam/contest/7234486/dashboard#s=p0
#
# Time:  O(R^2 + RlogB) on average, worst: O(R^2 + (2^R)logB)
# Space: O(R) on average, worst: O(2^R)
#
# another implementation of NFA 
#

from collections import defaultdict

def make_epsilon_reached_NFA(R, start, lookup, idx_set):  # Time: O(R), Space: O(R)
    # find the nearest epsilon reachable digit indices from current position of regex,
    # which are expressed as a state
    if start in lookup:
       return
    lookup.add(start)
    if start == len(R) or R[start].isdigit():
        idx_set.add(start)  # ...[0-9]...
        return
    if R[start] == ')':
        make_epsilon_reached_NFA(R, start+1, lookup, idx_set)  # ...)expr...
        return
    if R[start] == '|':
        count, new_start = 0,  0
        for i in xrange(start+1, len(R)):
            if R[i] == '(':
                count += 1
            elif R[i] == ')':
                count -= 1
            if count == -1:
                new_start = i
                break
        make_epsilon_reached_NFA(R, new_start+1, lookup, idx_set)  # ...|...)expr...
        return
    if R[start]=='*':
        count, new_start = 0,  0
        for i in reversed(xrange(start-1)):
            if R[i] == '(':
                count += 1
            elif R[i] == ')':
                count -= 1
            if count == 1:
                new_start = i
                break
        make_epsilon_reached_NFA(R, start+1, lookup, idx_set)  # ...(expr)*...
        make_epsilon_reached_NFA(R, new_start+1, lookup, idx_set)  # ...)*expr...
        return
    assert(R[start] == '(')
    make_epsilon_reached_NFA(R, start+1, lookup, idx_set)  # ...(expr|...
    count, new_start = 0,  0
    for i in xrange(start, len(R)):
        if R[i] == '(':
            count += 1
        elif R[i] == ')':
            count -= 1
        if count == 0:
            new_start = i
            break
        if count == 1 and R[i] == '|':
            make_epsilon_reached_NFA(R, i+1, lookup, idx_set)  # ...(...|expr...
    if new_start+1 != len(R) and R[new_start+1] == '*':
        make_epsilon_reached_NFA(R, new_start+2, lookup, idx_set)  # ...(...)*expr...

def match_NFA(R, transitions, X):  # Time: O(RlogB) ~ O((2^R)logB), Space: O(R) ~ O(2^R), ps. NFA for exact string matching rather than range count is only Time: O(RlogB), Space: O(R)
    x_digits = map(int, list(str(X)))
    count_state = {(True, True, frozenset(transitions[0])):1}
    for index in xrange(len(x_digits)):  # O(logB) times
        new_count_state = defaultdict(int)
        new_count_state[True, False, frozenset(transitions[0])] = 1
        assert(len(count_state) <= len(transitions))  # for extreme case, it would be more than 10*R, worst to O(2^R)
        for (is_empty, is_prefix_of_x, states), count in count_state.iteritems():  # O(R) times on normal case
            for new_digit in xrange(10):
                if is_empty and new_digit == 0:
                    continue  # numbers can't start with 0
                if is_prefix_of_x and new_digit > x_digits[index]:
                    continue  # numbers can't be greater than X
                new_possible_states = set()
                for start_state in states:  # find all possible states if new_digit was next in the string
                    for epsilon_state in transitions[start_state]:
                        if epsilon_state != len(R) and R[epsilon_state] == str(new_digit):
                            new_possible_states |= transitions[epsilon_state+1]
                if not new_possible_states:
                    continue
                new_count_state[False, is_prefix_of_x and new_digit == x_digits[index], frozenset(new_possible_states)] += count
        count_state = new_count_state
    count_match = 0
    for (_, _, states), count in count_state.iteritems():
        if states & transitions[len(R)]:
            count_match += count  # NFA matching may include empty string, which would be excluded after substraction
    return count_match

def integeregex():
    A, B = map(int, raw_input().strip().split())
    R = raw_input().strip()
    transitions = defaultdict(set)
    for i in xrange(len(R)+1):
        make_epsilon_reached_NFA(R, i, set(), transitions[i])
    return match_NFA(R, transitions, B) - \
           match_NFA(R, transitions, A-1)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, integeregex())
