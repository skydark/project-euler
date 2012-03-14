#!/usr/bin/python
# -*- coding: utf-8 -*-

#There are some prime values, p, for which there exists a positive integer, n, such that the expression n3 + n2p is a perfect cube.

#For example, when p = 19, 83 + 82×19 = 123.

#What is perhaps most surprising is that for each prime with this property the value of n is unique, and there are only four such primes below one-hundred.

#How many primes below one million have this remarkable property?

#Answer:
	#173

from time import time; t=time()
from mathplus import isqrt, get_primes_by_sieve

M = 10**6

primes, sieves = get_primes_by_sieve(M)
m = isqrt(M/3.)
ps = set(3*x*x+3*x+1 for x in range(m))

print(len(ps.intersection(primes)))#, time()-t

