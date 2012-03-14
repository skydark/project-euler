#!/usr/bin/python
# -*- coding: utf-8 -*-

#The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

#28 = 22 + 23 + 24
#33 = 32 + 23 + 24
#49 = 52 + 23 + 24
#47 = 22 + 33 + 24

#How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?

#Answer:
	#1097343

from time import time; t=time()
from mathplus import get_primes_by_sieve, isqrt, pow

M = 50000000

sqrtM = isqrt(M)
primes, _ = get_primes_by_sieve(sqrtM)
p2 = [p*p for p in primes]
p3 = [p**3 for p in primes[:int(pow(M, 1.0/3))]]
p4 = [p**4 for p in primes[:isqrt(sqrtM)+1]]
pool = set(p+q for p in p3 for q in p4 if p+q < M)
pool = set(p+q for p in pool for q in p2 if p+q < M)
print(len(pool))#, time()-t
