# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2016 World Finals - Problem E. Radioactive Islands
# https://code.google.com/codejam/contest/7234486/dashboard#s=p4
#
# Time:  O(X/H), X is the const range of x for integral
#              , H is the dx parameter for integral
# Space: O(1)
#
# Calculus of Variations: the fastest one
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

# Euler-Lagrange equation for finding minima of F(a, b) = sum(f(x, y, y') * dx)
def fp(C, x, y, yp):  # y'' = f'(x, y, y')
    t, s, syp, sx = 1.0+yp**2, 1.0, 0.0, 0.0
    for c in C:
        d_square = x**2 + (y-c)**2
        s += 1.0/d_square
        syp += (y-c)/d_square**2
        sx += (x + (y-c)*yp)/d_square**2  
    # according to Euler-Lagrange equation, i.e. df/dy = d(df/dy')/dx
    # let f = s * t^(1/2)
    #   1. df/dy = -2 * syp * t^(1/2)
    #   2. df/dy' = s * y' * t^(-1/2)
    #      d(df/dy')/dx = (-2 * sx) * y' * t^(-1/2) + s * (y'' *  t^(-1/2) - y' * y' * y'' * t^(-3/2))
    #                   = (-2 * sx * y') * t^(-1/2) + s * (t^(-1/2) - y'^2 * t^(-3/2)) * y''
    # df/dy = d(df/dy')/dx
    # => -2 * syp * t^(1/2) = (-2 * sx * y') * t^(-1/2) + s * (t^(-1/2) - y'^2 * t^(-3/2)) * y''
    # => y'' = 2 * ((sx * y') * t^(-1/2) - syp * t^(1/2)) / (s * (t^(-1/2) - y'^2 * t^(-3/2)))
    #        = 2 * (sx * y' * t - syp * t^2) / s * (t - y'^2))
    #        = 2 * (sx * y' * t - syp * t^2) / s * ((1 + y'^2) - y'^2))
    #        = 2 * (sx * y' * t - syp * t^2) / s
    #        = 2 * t * (sx * y' - syp * t) / s
    return 2.0 * t * (sx * yp - syp * t) / s

# Runge-Kutta methods:
# - https://en.wikipedia.org/wiki/List_of_Runge%E2%80%93Kutta_methods
# RK2 for 2nd-order ODE:
# - https://math.stackexchange.com/questions/1134540/second-order-runge-kutta-method-for-solving-second-order-ode
# RK4 for 2nd-order ODE:
# - https://math.stackexchange.com/questions/2615672/solve-fourth-order-ode-using-fourth-order-runge-kutta-method
# - http://homepages.cae.wisc.edu/~blanchar/eps/ivp/ivp.htm
# - https://stackoverflow.com/questions/52334558/runge-kutta-4th-order-method-to-solve-second-order-odes
# - https://publications.waset.org/1175/pdf
def F(C, x, y, yp):
    dose = 0.0
    for _ in xrange(int((X_END-X_START)/H)):  # more accurate than [while x < X_END]
        if not (MIN_Y_BOUND <= y <= MAX_Y_BOUND):
            return float("inf"), y
        # dose = sum(f(x, y, y') * dx = (1 + sum(1 / (x^2 + (y-ci)^2))) * sqrt(1 + y'^2) * dx)), where dx = H
        dose += H * (1.0+D(C, x, y)) * sqrt(1.0 + yp**2)
        # applying RK1 (forward Euler) for 2nd-order ODE is enough,
        # besides, RK2 (explicit midpoint) is also fine,
        # but RK4 is unstable (fine with H = 0.01 but other may not) for some cases due to large y'
        k1 = H * yp
        l1 = H * fp(C, x, y, yp)
        '''
        k2 = H * (yp + l1/2.0)
        l2 = H * fp(C, x+H/2.0, y+k1/2.0, yp+l1/2.0)
        k3 = H * (yp + l2/2.0)
        l3 = H * fp(C, x+H/2.0, y+k2/2.0, yp+l2/2.0)
        k4 = H * (yp + l3)
        l4 = H * fp(C, x+H, y+k3, yp+l3)
        '''
        x += H
        y += k1  # RK2: y += k2, RK4: y += (k1 + 2.0*k2 + 2.0*k3 + k4)/6.0
        yp += l1  # RK2: yp += l2, RK4: yp += (l1 + 2.0*l2 + 2.0*l3 + l4)/6.0
    return dose, y

def binary_search(A, B, C, left, right):
    dose = float("inf")
    while abs(right-left)/2.0 > float_info.epsilon:
        mid = (left+right)/2.0
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
        result = min(result, binary_search(A, B, C, slopes[i], slopes[i+1]))
    return result

H = 0.01  # tuned by experiment, works for RK1, RK2, RK4, besides, H = 0.5 only works for RK1

MIN_Y_BOUND, MAX_Y_BOUND = -13.0, 13.0  # verified by experiment
X_START, X_END = -10.0, 10.0
MIN_A, MAX_A = -10.0, 10.0
MIN_C, MAX_C = -10.0, 10.0
X_C = 0.0
MIN_SLOPE, MAX_SLOPE = (MIN_C-MAX_A)/(X_C-X_START), (MAX_C-MIN_A)/(X_C-X_START)
for case in xrange(input()):
    print "Case #%d: %s" % (case+1, radioactive_islands())
