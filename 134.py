#!/usr/bin/python
# -*- coding: utf-8 -*-

#Consider the consecutive primes p1 = 19 and p2 = 23. It can be verified that 1219 is the smallest number such that the last digits are formed by p1 whilst also being divisible by p2.

#In fact, with the exception of p1 = 3 and p2 = 5, for every pair of consecutive primes, p2 > p1, there exist values of n for which the last digits are formed by p1 and n is divisible by p2. Let S be the smallest of these values of n.

#Find ∑ S for every pair of consecutive primes with 5 ≤ p1 ≤ 1000000.

#Answer:
	#18613426663617118

from time import time; t=time()
from mathplus import log10, get_primes_by_sieve

M = 10**6+5

primes, sieves = get_primes_by_sieve(M)

def f(n, m):
    #assert n > m
    if (n, m) == (1, 0): return 1, 0
    q, r = n//m, n%m
    a, b = f(m, r)
    return b, a-b*q

s = 0
for i in range(2, len(primes)-1):
    p, q = primes[i:i+2]
    n = 10**(int(log10(p))+1)
    a, b = f(q, n%q)
    s += (b*(q-p) % q)*n+p

print(s)#, time()-t

