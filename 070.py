#!/usr/bin/python
# -*- coding: utf-8 -*-

#Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
#The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

#Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

#Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.

#Answer:
	#8319823

from time import time; t=time()
#import psyco; psyco.full()

#from gen_primes import get_primes
from mathplus import get_primes_by_sieve

M = 10000000
primes, _ = get_primes_by_sieve(M, odd_only=True)
#primes = get_primes(M, odd_only=True)
#print time()-t
phis = list(range(M))
for i in range(2, M, 2):
    phis[i] = 0
for p in primes:
    if p >= M: break
    for i in range(p, M, p):
        phis[i] -= phis[i]//p

#print time()-t
def is_permutation(x, y):
    sx, sy = str(x), str(y)
    return len(sx) == len(sy) and ''.join(sorted(sx)) == ''.join(sorted(sy))

min_phi = M
min_n = 0
enum = list(enumerate(phis))[2:]
for n, phi_n in enum:
    if n < min_phi*phi_n and is_permutation(n, phi_n):
        min_n = n
        min_phi = 1.0*n/phi_n
print(min_n)#, time()-t
