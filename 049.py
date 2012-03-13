#!/usr/bin/python
# -*- coding: utf-8 -*-

#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

#What 12-digit number do you form by concatenating the three terms in this sequence?

#Answer:
	#296962999629

from time import time; t=time()
from mathplus import sieve, permutations

ret = {}
primes = sieve(10000)
p = [i for i, f in enumerate(primes) if f and i >= 1000]
for n in p:
    c = []
    for i in permutations((n//1000, (n % 1000)//100, (n % 100)//10, n%10)):
        if 0 in i: break
        m = i[0]*1000+i[1]*100+i[2]*10+i[3]
        if primes[m] and m not in c: c.append(m)
    if len(c) >= 3:
        c = sorted(c)
        if c[0] in ret: continue
        for i in range(1, len(c)-1):
            for j in range(i):
                if c[i]*2-c[j] in c:
                    ret[c[0]] = (c[j], c[i], 2*c[i]-c[j])
assert len(ret) == 2
del ret[1487]
print(['%s%s%s' %(v[0],v[1],v[2]) for k, v in ret.items()][0])#, time()-t
