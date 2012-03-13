#!/usr/bin/python
# -*- coding: utf-8 -*-

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

#Answer:
	#104743

from time import time; t=time()
from mathplus import get_primes_by_sieve, prime

CNT = 10001
i = 0
for p in prime():
    i += 1
    if i == CNT: break
    
print(p)#, time()-t
