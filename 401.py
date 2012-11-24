#!/usr/bin/python
# -*- coding: utf-8 -*-

# The divisors of 6 are 1,2,3 and 6.
# The sum of the squares of these numbers is 1+4+9+36=50.

# Let sigma2(n) represent the sum of the squares of the divisors of n. Thus sigma2(6)=50.
# Let SIGMA2 represent the summatory function of sigma2, that is SIGMA2(n)=∑sigma2(i) for i=1 to n.
# The first 6 values of SIGMA2 are: 1,6,16,37,63 and 113.

# Find SIGMA2(1015) modulo 109.

#Answer:
    #281632621

from mathplus import timer, isqrt

N = 10 ** 15
M = 10 ** 9


@timer
def pe(n, m):
    s, t = 0, isqrt(n)
    cache = [(n // i % m) for i in range(1, n // t + 1)]
    for i in range(t - 1):
        k = cache[i]
        s += k * (k + 1) * (2 * k + 1) // 6
    k = cache[t - 1]
    s -= (t - 1) * k * (k + 1) * (2 * k + 1) // 6
    s %= m
    for i in range(n // t):
        s += (i + 1) ** 2 * cache[i]
    return s % m

print(pe(N, M))
