#!/usr/bin/python
# -*- coding: utf-8 -*-

#The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

#Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

#Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

#12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

#Since this chain returns to its starting point, it is called an amicable chain.

#Find the smallest member of the longest amicable chain with no element exceeding one million.

#Answer:
	#14316

from time import time; t=time()
from mathplus import get_primes_by_sieve

M = 1000000

pool = list(range(M))
value = [1]*M
primes, _ = get_primes_by_sieve(M)
for p in primes:
    for m in range(p*2, M, p):
        k = 0
        while pool[m] % p == 0: 
            k += 1
            pool[m] //= p
        value[m] *= (p**(k+1)-1)//(p-1)
#print time()-t

flag = [0]*M
max_k = 0
max_f = None
for n in range(2, M):
    if flag[n]: continue
    f, x, k = [], n, 0
    while x not in f:
        f.append(x)
        k += 1
        x = value[x]-x
        if x >= M or flag[x] != 0:
            k = -1
            break
    if k > 0:
        w = f.index(x)
        f = f[w:]
        k = len(f)
        if k > max_k:
            max_k = k
            max_f = f[:]
    for x in f:
        flag[x] = k

print(sorted(max_f)[0])#, max_k, time()-t
