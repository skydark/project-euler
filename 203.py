#!/usr/bin/python
# -*- coding: utf-8 -*-

#The binomial coefficients nCk can be arranged in triangular form, Pascal's triangle, like this:
	#1	
	#1		1	
	#1		2		1	
	#1		3		3		1	
	#1		4		6		4		1	
	#1		5		10		10		5		1	
	#1		6		15		20		15		6		1	
#1		7		21		35		35		21		7		1
#.........

#It can be seen that the first eight rows of Pascal's triangle contain twelve distinct numbers: 1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 21 and 35.

#A positive integer n is called squarefree if no square of a prime divides n. Of the twelve distinct numbers in the first eight rows of Pascal's triangle, all except 4 and 20 are squarefree. The sum of the distinct squarefree numbers in the first eight rows is 105.

#Find the sum of the distinct squarefree numbers in the first 51 rows of Pascal's triangle.

#Answer:
	#34029210557338

from time import time; t=time()
from mathplus import get_primes_by_sieve#, cached

M = 51

def factp(n, p):
    if n in (0, 1): return 0
    i = 0
    while n % p == 0:
        n //= p
        i += 1
    return i

primes, sieves = get_primes_by_sieve(M)
pcnt = len(primes)
pool = dict((n, [factp(n, p) for p in primes]) for n in range(M))

for n in range(2, M):
    v = n
    for m in range(2, n//2+1):
        u = v * (n+1-m)//m
        if u not in pool:
            pool[u] = [pool[v][i]+pool[n+1-m][i]-pool[m][i] for i in range(pcnt)]
        v = u

s = sum(k for k, v in pool.items() if all(u <= 1 for u in v))

print(s)#, time()-t
