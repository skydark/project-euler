#!/usr/bin/python
# -*- coding: utf-8 -*-

# !!!WARNING!!! USE PYPY!

# For a positive integer n, let σ2(n) be the sum of the squares of its divisors. For example,
# σ2(10) = 1 + 4 + 25 + 100 = 130.

# Find the sum of all n, 0 < n < 64,000,000 such that σ2(n) is a perfect square.

#Answer:
    #1922364685

from mathplus import timer, is_quad

N = 64000000


@timer
def pe(n):
    pool = [k * k + 1 for k in range(n)]
    pool[1] = 1

    for k in range(2, (n + 1) // 2):
        k2 = k * k
        for m in range(k * 2, n, k):
            pool[m] += k2

    s = 0
    for i, m in enumerate(pool):
        if is_quad(m):
            s += i
    return s

print(pe(N))
