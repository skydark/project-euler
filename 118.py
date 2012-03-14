#!/usr/bin/python
# -*- coding: utf-8 -*-

#Using all of the digits 1 through 9 and concatenating them freely to form decimal integers, different sets can be formed. Interestingly with the set {2,5,47,89,631}, all of the elements belonging to it are prime.

#How many distinct sets containing each of the digits one through nine exactly once contain only prime elements?

#Answer:
	#44680

from time import time; t=time()
from mathplus import permutations, isqrt, get_primes_by_sieve

M = 1000000

primes, sieves = get_primes_by_sieve(M)
def is_prime_plus(n):
    if n % 2 == 0: return n == 2
    if n % 3 == 0: return n == 3
    if n < M: return sieves[n]
    isqrtn = isqrt(n)
    for p in primes:
        if p > isqrtn: return True
        if n % p == 0: return False

ret = set()

def tryn(n, l, start_i, tr, maxn):
    for i in range(start_i, 9):
        n = n*10+l[i]
        if n < maxn: continue
        if is_prime_plus(n):
            tr.append(n)
            tryn(0, l, i+1, tr, n)
            tr.pop()
    if start_i == 9:
        ret.add(tuple(sorted(tr)))

for l in permutations(range(1, 10)):
    if l[-1] % 2 == 0 or l[-1] == 5: continue
    tr = []
    tryn(0, l, 0, tr, 0)

print(len(ret))#, time()-t
