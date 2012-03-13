#!/usr/bin/python
# -*- coding: utf-8 -*-

#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

#How many circular primes are there below one million?

#Answer:
	#55  

from time import time; t = time()
from mathplus import sieve

M = 1000000

S = sieve(M)
count = 2
for k in range(3, M, 2):
    if not S[k]: continue
    s = str(k)
    if any((i in s) for i in '024568'): continue
    for i in range(len(s)):
        if not S[int(s)]: break
        s = s[1:]+s[0]
    else:
        count += 1

print(count)#, time()-t
