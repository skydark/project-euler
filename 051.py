#!/usr/bin/python
# -*- coding: utf-8 -*-

#By replacing the 1st digit of *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

#By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

#Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

#Answer:
	#121313

from time import time; t=time()
from mathplus import get_primes_by_sieve, product

M = 1000000
L = 8

primes, sieves = get_primes_by_sieve(M)
strn = [str(i) for i in range(10)]

def f(l):
    for n in range(10000, M):
        if not sieves[n]: continue
        s = str(n)
        for i in range(10):
            si = strn[i]
            sc = s.count(si)
            if sc <= 1: continue
            replace_pos = [0]*sc
            for i in range(sc):
                replace_pos[i] = s.find(si, replace_pos[i-1]+1 if i > 0 else 0)
            start_j = 1 if replace_pos[0] == 0 else 0
            for it in product(*[(0,1)]*sc):
                if sum(it) < 2: continue
                c = 0
                r = list(s)
                for j in range(start_j, 10):
                    u = strn[j]
                    for k in range(sc):
                        if it[k] == 1: r[replace_pos[k]] = u
                    ret = int(''.join(r))
                    if sieves[ret]: c += 1
                if c >= l: return n

n = f(L)
print(n)#, time() - t
