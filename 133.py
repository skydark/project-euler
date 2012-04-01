#!/usr/bin/python
# -*- coding: utf-8 -*-

#A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.

#Let us consider repunits of the form R(10n).

#Although R(10), R(100), or R(1000) are not divisible by 17, R(10000) is divisible by 17. Yet there is no value of n for which R(10n) will divide by 19. In fact, it is remarkable that 11, 17, 41, and 73 are the only four primes below one-hundred that can be a factor of R(10n).

#Find the sum of all the primes below one-hundred thousand that will never be a factor of R(10n).

#Answer:
	#453647705

from time import time; t=time()
from mathplus import get_phis_by_sieve, pow_mod

M = 100000

phis = get_phis_by_sieve(M)

s = 3
for p, phip in enumerate(phis):
    if phip != p - 1 or p == 1: continue
    k = 1
    while phip % 2 == 0:
        phip //= 2
        k *= 2
    while phip % 5 == 0:
        phip //= 5
        k *= 5
    if pow_mod(10, k, p) != 1:
        s += p

print(s)#, time()-t)
