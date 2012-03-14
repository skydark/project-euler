#!/usr/bin/python
# -*- coding: utf-8 -*-

#In the following equation x, y, and n are positive integers.
#1/x + 1/y = 1/n
#For n = 4 there are exactly three distinct solutions:
#1/5 + 1/20 = 1/4
#1/6 + 1/12 = 1/4
#1/8 + 1/8 = 1/4

#What is the least value of n for which the number of distinct solutions exceeds one-thousand?

#NOTE: This problem is an easier version of problem 110; it is strongly advised that you solve this one first.

#Answer:
	#180180

from time import time; t=time()
from mathplus import get_primes_by_sieve, isqrt

L = 1000
M = 1000

primes, _ = get_primes_by_sieve(M)

def solve2(n):
    u = 1
    m = isqrt(n)
    for f in primes:
        if f > m:
            u *= 3
            break
        k = 0
        while n % f == 0:
            n //= f
            k += 1
        u *= (2*k+1)
        if n == 1: break
    return u

n = 4
l = L*2-1
while solve2(n) < l: n += 1

print(n)#, time()-t
