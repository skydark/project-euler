#!/usr/bin/python
# -*- coding: utf-8 -*-

#The prime 41, can be written as the sum of six consecutive primes:
#41 = 2 + 3 + 5 + 7 + 11 + 13

#This is the longest sum of consecutive primes that adds to a prime below one-hundred.

#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

#Which prime, below one-million, can be written as the sum of the most consecutive primes?

#Answer:
	#997651

from time import time; t=time()
from mathplus import get_primes_by_sieve

M = 1000000
primes, sieves = get_primes_by_sieve(M)

m, mi = 5, 2
s = 5
for i in range(2, len(primes)-1, 2):
    s += primes[i]+primes[i+1]
    if s >= M: break
    if sieves[s]: m, mi = s, i+2

if mi < 21: m, mi = 953, 21
primes.pop(0)
ss = sum(primes[:21])
for i in range(23, len(primes)-1, 2):
    ss += primes[i-1]+primes[i-2]
    if ss >= M: break
    if sieves[ss]:
        m, mi = ss, i
        continue
    s = ss
    for j in range(i, len(primes)):
        s += primes[j]-primes[j-i]
        if s >= M: break
        if sieves[s]: 
            m, mi = s, i
            break

print(m)#, time()-t
