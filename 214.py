#!/usr/bin/python
# -*- coding: utf-8 -*-

#Let φ be Euler's totient function, i.e. for a natural number n, φ(n) is the number of k, 1 ≤ k ≤ n, for which gcd(k,n) = 1.

#By iterating φ, each positive integer generates a decreasing chain of numbers ending in 1.
#E.g. if we start with 5 the sequence 5,4,2,1 is generated.
#Here is a listing of all chains with length 4:
#5,4,2,1
#7,6,2,1
#8,4,2,1
#9,6,2,1
#10,4,2,1
#12,4,2,1
#14,6,2,1
#18,6,2,1

#Only two of these chains start with a prime, their sum is 12.

#What is the sum of all primes less than 40000000 which generate a chain of length 25?

#Answer:
	#1677366278943

from time import time; t=time()
#from psyco import full;full()

M = 40000000
L = 25

phis = list(range(M))
#lens = [1]*M
s = 0

for p in range(2, M):
    if phis[p] == p:
        #phis[p] = p-1
        for m in range(p*2, M, p):
            phis[m] -= phis[m]//p
        #lens[p] = lens[p-1]+1
        phis[p] = phis[p-1]+1
        #if lens[p] == L: s += p
        if phis[p] == L: s += p
    else:
        #lens[p] = lens[phis[p]]+1
        phis[p] = phis[phis[p]]+1

#print sum(p for p, k in enumerate(lens) if k == L and phis[p] == p-1), time()-t
print(s)#, time()-t
