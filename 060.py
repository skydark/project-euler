#!/usr/bin/python
# -*- coding: utf-8 -*-

#The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

#Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

#Answer:
	#26033

from time import time; t=time()
from mathplus import isqrt, log10, get_primes_by_sieve, dropwhile

L = 10000

primes, sieves = get_primes_by_sieve(L, odd_only=True)
max_prime = primes[-1]

def is_prime(n):
    if n <= L: return sieves[n]
    for i in primes:
        if n % i == 0: return False
    for i in range(max_prime+2, isqrt(n), 2):
        if n % i == 0: return False
    return True

def concat(i, j):
    return 10**(int(log10(j))+1)*i+j

s = L * 5
checks = {}
for i in primes:
    checks[i] = {}
    for j in primes:
        if j < i:
            checks[i][j] = checks[j][i]
        elif j == i:
            checks[i][j] = False
        else:
            checks[i][j] = is_prime(concat(i, j)) and is_prime(concat(j, i))
def get_fit_num(i):
    return [k for k, v in checks[i].items() if v]

#print time()-t
p = [0]*5
for p[0] in checks:
    s0 = get_fit_num(p[0])
    for p[1] in dropwhile(lambda x: x>p[0], s0):
        s1 = sorted(list(set(get_fit_num(p[1])).intersection(s0)))
        for p[2] in dropwhile(lambda x: x>p[1], s1):
            for p[3] in dropwhile(lambda x: x>p[2], s1):
                if sum(p[:4]) > s: break
                if not checks[p[2]][p[3]]: break
                for p[4] in dropwhile(lambda x: x>p[3], s1):
                    if checks[p[2]][p[4]] and checks[p[3]][p[4]]:
                        ss = sum(p)
                        if ss >= s: break
                        s = ss
                        print(s)#, p, time()-t
