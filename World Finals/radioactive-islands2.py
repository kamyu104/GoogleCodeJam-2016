# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2016 World Finals - Problem E. Radioactive Islands
# https://code.google.com/codejam/contest/7234486/dashboard#s=p4
#
# Time:  O((20/H)^2), pass in PyPy2 but Python2
# Space: O(1)
#

from sys import float_info
from math import sqrt

def D(C, x, y):
    dose = 0.0
    for c in C:
        d_square = x**2 + (y-c)**2
        if d_square < float_info.epsilon:
            return float("inf")
        dose += 1.0/d_square
    return dose

# Euler-Lagrange Equation for finding minima of F
def f(C, x, y, y_prime):  # y'' = f(x, y, y')
    d = [x**2 + (y-c)**2 for c in C]
    p0, p1, p2, p3 = 1.0+y_prime**2, 0.0, 0.0, 1.0
    for i in xrange(len(C)):
        p1 += (y-C[i])/d[i]/d[i]
        p2 += (x + (y-C[i])*y_prime)/d[i]/d[i]
        p3 += 1.0/d[i]
    return -2.0*(p0**2*p1 - y_prime*p0*p2)/p3  # solved by Euler-Lagrange Equation

# Runge-Kutta Method (RK4) for 2nd-order ODE:
# 1. https://math.stackexchange.com/questions/2615672/solve-fourth-order-ode-using-fourth-order-runge-kutta-method
# 2. http://homepages.cae.wisc.edu/~blanchar/eps/ivp/ivp.htm
# 3. https://stackoverflow.com/questions/52334558/runge-kutta-4th-order-method-to-solve-second-order-odes
# 4. https://publications.waset.org/1175/pdf
def F(C, x, y, y_prime):
    dose = 0.0
    while x < X_END:
        if y < MIN_Y_BOUND:
            return float("inf"), MIN_Y_BOUND
        if y > MAX_Y_BOUND:
            return float("inf"), MAX_Y_BOUND
        # dose = sum(F(x, y, y_prime)= (1 + sum(1 / (x^2 + (y-ci)^2))) * sqrt(1 + y_prime^2) * dx), where dx = H
        dose += H * (1.0+D(C, x, y)) * sqrt(1.0 + y_prime**2)
        k1 = H * y_prime
        l1 = H * f(C, x, y, y_prime)
        k2 = H * (y_prime + l1/2)
        l2 = H * f(C, x+H/2, y+k1/2, y_prime+l1/2)
        k3 = H * (y_prime + l2/2)
        l3 = H * f(C, x+H/2, y+k2/2, y_prime+l2/2)
        k4 = H * (y_prime + l3/2)
        l4 = H * f(C, x+H/2, y+k3, y_prime+l3)
        x += H
        y += (k1 + 2*k2 + 2*k3 + k4)/6
        y_prime += (l1 + 2*l2 + 2*l3 + l4)/6
    return dose, y

def binary_search(A, B, C, left, right):
    dose = float("inf")
    while abs(right-left) > EPISOLON:
        mid = (left+right)/2
        dose, y = F(C, X_START, A, mid)
        if y >= B:
            right = mid
        else:
            left = mid
    return dose

def radioactive_islands():
    N, A, B = map(float, raw_input().strip().split())
    C = map(float, raw_input().strip().split())
    slopes = [MIN_SLOPE, MAX_SLOPE]
    slopes.extend((c-A)/(X_C-X_START) for c in C)
    slopes.sort()
    result = float("inf")
    for i in xrange(len(slopes)-1):
        result = min(result,
                     binary_search(A, B, C, slopes[i], slopes[i+1]),
                     binary_search(A, B, C, slopes[i+1], slopes[i]))
    return result

H = 0.001  # tuned by experiment
MIN_Y_BOUND, MAX_Y_BOUND = -100.0, 100.0  # tuned by experiment
EPISOLON = 1e-4  # tuned by experiment

X_START, X_END = -10.0, 10.0
MIN_A, MAX_A = -10.0, 10.0
MIN_C, MAX_C = -10.0, 10.0
X_C = 0.0
MIN_SLOPE, MAX_SLOPE = (MIN_C-MAX_A)/(X_C-X_START), (MAX_C-MIN_A)/(X_C-X_START)
for case in xrange(input()):
    print "Case #%d: %s" % (case+1, radioactive_islands())
