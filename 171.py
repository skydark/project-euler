#!/usr/bin/python
# -*- coding: utf-8 -*-

# For a positive integer n, let f(n) be the sum of the squares of the digits (in base 10) of n, e.g.

#   f(3) = 3^2 = 9,

#   f(25) = 2^2 + 5^2 = 4 + 25 = 29,

#   f(442) = 4^2 + 4^2 + 2^2 = 16 + 16 + 4 = 36

# Find the last nine digits of the sum of all n, 0 < n < 10^20, such that f(n) is a perfect square.

#Answer:
	#142989277

from time import time; t=time()
from mathplus import isqrt

M = 9
N = 20

def pe171(n, m):
    up = isqrt(n * 81)
    uplimit = up ** 2 + 1
    d = [[[0, 0] for j in range(uplimit)] for i in range(n)]
    for k in range(10):
        d[0][k*k] = [1, k]
    for i in range(1, n):
        ii = 10 ** i if i < m else 0
        for j in range(uplimit):
            for k in range(10):
                kk = k * k
                if j < kk:
                    break
                p, q = d[i-1][j-kk]
                d[i][j][0] += p
                d[i][j][1] += q + ii * k * p
    # print [(k, d[n-1][k*k]) for k in range(up+1)]
    return str(sum(d[n-1][k*k][1] for k in range(1, up+1)))[-m:]

print(pe171(N, M), time()-t)
