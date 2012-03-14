#!/usr/bin/python
# -*- coding: utf-8 -*-

#The binomial coefficient 10C3 = 120.
#120 = 23 × 3 × 5 = 2 × 2 × 2 × 3 × 5, and 2 + 2 + 2 + 3 + 5 = 14.
#So the sum of the terms in the prime factorisation of 10C3 is 14.

#Find the sum of the terms in the prime factorisation of 20000000C15000000.
#Answer:
	#7526965179680

from time import time; t=time()
#from mathplus import get_primes_by_sieve
from gen_primes import get_primes

N, M = 20000000, 15000000
M = min(M, N-M)

#primes, sieves = get_primes_by_sieve(N)
primes = get_primes(50000000)
#print time()-t

def factfact(n):
    #ret = {}
    ret = 0
    for p in primes:
        if p > n: break
        k, m = 0, n
        while m >= p:
            m //= p
            k += m
        #ret[p] = k
        ret += p*k
    return ret

def factcnm(n, m):
    ret = factfact(n)
    ret -= factfact(m)+factfact(n-m)
    #for k, v in factfact(m).iteritems():
    #    ret[k] -= v
    #for k, v in factfact(n-m).iteritems():
    #    ret[k] -= v
    return ret

print(factcnm(N, M))#, time()-t
#print sum(k*v for k, v in factcnm(N, M).iteritems())#, time()-t

'''
NN = N+1
facts = [{} for i in xrange(NN)]
print time()-t
for i in xrange(2, NN):
    if not facts[i]:
        ii = i
        k = 1
        while ii < NN:
            for j in xrange(ii, NN, ii):
                facts[j][i] = k
            ii *= i
            k += 1
print time()-t'''

'''
K = 4473#sqrt(20000000)
primes, sieves = get_primes_by_sieve(K)
def facts(n):
    ret = []
    isqrtn = isqrt(n)
    for p in primes:
        if p > isqrtn or n == 1: break
        k = 0
        while n % p == 0:
            n /= p
            k += 1
        if k > 0:
            ret.append((p, k))
            isqrtn = isqrt(n)
    if n > 1: ret.append((n, 1))
    return ret

n = N
c = dict(facts(n))
for m in xrange(2, M+1):
    for k, v in facts(n-m+1):
        c.setdefault(k, 0)
        c[k] += v
    for k, v in facts(m):
        c.setdefault(k, 0)
        c[k] -= v
    #if m % 100000 == 0: print m/50000
'''
