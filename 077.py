#!/usr/bin/python
# -*- coding: utf-8 -*-

#It is possible to write ten as the sum of primes in exactly five different ways:

#7 + 3
#5 + 5
#5 + 3 + 2
#3 + 3 + 2 + 2
#2 + 2 + 2 + 2 + 2

#What is the first value which can be written as the sum of primes in over five thousand different ways?

#Answer:
	#71

from time import time; t=time()
from mathplus import memorize, get_primes_by_sieve, takewhile

M = 100
L = 5000

primes, sieves = get_primes_by_sieve(M)
flag = 0
for i in range(M):
    if sieves[i]: flag = i
    sieves[i] = flag

@memorize
def sp(n, m):
    if n == 0: return 1
    if n <= 1 or m <= 1: return 0
    if n == 2: return 1
    s = 0
    for i in takewhile(lambda x: x <= m, primes):
        ni = n - i
        if i <= ni:
            s += sp(ni, i)
        else:
            s += sp(ni, sieves[ni])
    return s

test = 0
while True:
    v = sp(test, sieves[test])
    if v > L: break
    test += 1
print(test)#, time()-t
