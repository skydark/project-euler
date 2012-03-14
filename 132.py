#!/usr/bin/python
# -*- coding: utf-8 -*-

#A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k.

#For example, R(10) = 1111111111 = 11×41×271×9091, and the sum of these prime factors is 9414.

#Find the sum of the first forty prime factors of R(109).

#Answer:
	#843296

from time import time; t=time()
from mathplus import pow_mod, get_primes_by_sieve

M = 10**9
C = 40

L = 200000

primes, sieves = get_primes_by_sieve(L)

def f(n, m, p):
    # assert p in primes
    return pow_mod(n, m % (p-1), p)

s = 0
c = C
for p in primes[3:]:
    if f(10, M, p) == 1:
        s += p
        c -= 1
        if c == 0: break
else:
    raise Exception('L is too low')

print(s)#, time()-t
