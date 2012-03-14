#!/usr/bin/python
# -*- coding: utf-8 -*-

#A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.

#Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that there always exists a value, k, for which R(k) is divisible by n, and let A(n) be the least such value of k; for example, A(7) = 6 and A(41) = 5.

#You are given that for all primes, p > 5, that p − 1 is divisible by A(p). For example, when p = 41, A(41) = 5, and 40 is divisible by 5.

#However, there are rare composite values for which this is also true; the first five examples being 91, 259, 451, 481, and 703.

#Find the sum of the first twenty-five composite values of n for which
#GCD(n, 10) = 1 and n − 1 is divisible by A(n).

#Answer:
	#149253

from time import time; t=time()
from mathplus import pow_mod, get_primes_by_sieve

M = 10**6
C = 25
L = []

primes, sieves = get_primes_by_sieve(M)

n, c = 7, C
while True:
    n += 2
    if n % 3 == 0 or n % 5 == 0 or sieves[n]: continue
    if pow_mod(10, n-1, n) == 1:
        c -= 1
        L.append(n)
        if c == 0: break

print(sum(L))#, time()-t

