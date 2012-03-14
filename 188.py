#!/usr/bin/python
# -*- coding: utf-8 -*-

#The hyperexponentiation or tetration of a number a by a positive integer b, denoted by a↑↑b or ba, is recursively defined by:

#a↑↑1 = a,
#a↑↑(k+1) = a(a↑↑k).

#Thus we have e.g. 3↑↑2 = 33 = 27, hence 3↑↑3 = 327 = 7625597484987 and 3↑↑4 is roughly 103.6383346400240996*10^12.

#Find the last 8 digits of 1777↑↑1855.

#Answer:
	#95962097

from time import time; t=time()
from mathplus import pow_mod, factorization, phi

A, B = 1777, 1855
M = 10**8

def f(a, b, p):
    if b == 1 or p == 2: return a % p
    x = f(a, b-1, phi(p))
    return pow_mod(a, x, p)

print(f(A, B, M))#, time()-t
