#!/usr/bin/python
# -*- coding: utf-8 -*-

#A composite is a number containing at least two prime factors. For example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.

#There are ten composites below thirty containing precisely two, not necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

#How many composite integers, n < 108, have precisely two, not necessarily distinct, prime factors?

#Answer:
	#17427258

from time import time; t=time()
from mathplus import isqrt, get_primes_by_sieve
from gen_primes import get_primes

#M = 30
M = 10**8

sqrtM = isqrt(M)
primes = get_primes(M//2, odd_only=False)
#print time()-t
sieves = [0]*(sqrtM+1)
pnext = 2
pnext_index = 0
p = 0
for i in range(sqrtM+1):
    if i == pnext:
        pnext_index += 1
        pnext = primes[pnext_index]
        p += 1
    sieves[i] = p
#print time()-t
ss = sieves[sqrtM]
s = ss*(ss+1)//2
s += sum(sieves[M//p] for p in primes[ss:])
print(s)#, time()-t
