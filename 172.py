#!/usr/bin/python
# -*- coding: utf-8 -*-

# How many 18-digit numbers n (without leading zeros) are there such that no digit occurs more than three times in n?

#Answer:
	#227485267000992000

from time import time; t=time()
from mathplus import Cnr, memorize, factorial, product

Cnr = memorize(Cnr)

N = 18
M = 3

def pe172(n, m):
    m += 1
    @memorize
    def test(digit, sum, c):
        if digit * m < sum:
            return 0
        if digit == 0:
            return c
        if sum == 0:
            return 1
        s = 0
        for i in range(min(m, sum+1)):
            s += test(digit-1, sum-i, Cnr(sum, i))
        return s * c

    s = 0
    for k in range(m):
        s += test(9, n-k, 1) * Cnr(n-1, k)
    return s

print(pe172(N, M))#, time()-t)
