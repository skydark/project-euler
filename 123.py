#!/usr/bin/python
# -*- coding: utf-8 -*-

#Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when (pn−1)n + (pn+1)n is divided by pn2.

#For example, when n = 3, p3 = 5, and 43 + 63 = 280 ≡ 5 mod 25.

#The least value of n for which the remainder first exceeds 109 is 7037.

#Find the least value of n for which the remainder first exceeds 1010.

#Answer:
	#21035

from time import time; t=time()
from mathplus import get_primes_by_sieve, takewhile

M = 10**10
L = 1000000

p, sieves = get_primes_by_sieve(L)

for n in takewhile(lambda x: 2*x*p[x-1] <= M, range(7037, L, 2)): pass

print(n+2)#, time()-t
