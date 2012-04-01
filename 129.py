#!/usr/bin/python
# -*- coding: utf-8 -*-

#A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.

#Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that there always exists a value, k, for which R(k) is divisible by n, and let A(n) be the least such value of k; for example, A(7) = 6 and A(41) = 5.

#The least value of n for which A(n) first exceeds ten is 17.

#Find the least value of n for which A(n) first exceeds one-million.

#Answer:
	#1000023

from time import time; t=time()
from mathplus import pow_mod, factorization, phi

M = 1000000
S = M//2*2 + 1
T = 1001000

def report(p):
    print(p)#, time()-t)
    import sys
    sys.exit()

for p in range(S, T, 2):
    if p % 5 == 0: continue
    phip = phi(p)
    m = p
    if p % 3 == 0:
        phip *= 9
        m *= 9
    if phip <= M: continue
    factors = factorization(phip)
    while phip > M:
        for f, c in factors:
            phif = phip//f
            if pow_mod(10, phif, m) == 1:
                phip = phif
                if c > 1:
                    factors = [(k, v) if k != f else (k, v-1)
                        for k, v in factors]
                else:
                    factors = [(k, v) for k, v in factors if k != f]
                break
        else:
            report(p)

print('Failed!', time()-t)
