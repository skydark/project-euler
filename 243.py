#!/usr/bin/python
# -*- coding: utf-8 -*-

#A positive fraction whose numerator is less than its denominator is called a proper fraction.
#For any denominator, d, there will be d−1 proper fractions; for example, with d = 12:
#1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12 .

#We shall call a fraction that cannot be cancelled down a resilient fraction.
#Furthermore we shall define the resilience of a denominator, R(d), to be the ratio of its proper fractions that are resilient; for example, R(12) = 4/11 .
#In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10 .

#Find the smallest denominator d, having a resilience R(d) < 15499/94744 .

#Answer:
	#892371480

from time import time; t=time()
from mathplus import get_primes_by_sieve, takewhile

A = 15499
B = 94744
M = 100

primes, sievs = get_primes_by_sieve(M)

def no_primes_larger_than(n, p):
    for pp in takewhile(lambda x: x<=p, primes):
        while n % pp == 0:
            n //= pp
    return n == 1

a = 1
b = 1
pool = []
for p in primes:
    a *= (p-1)
    b *= p
    x = b*A-a*B
    if x > 0:
        k = A//x+1
        while True:
            if no_primes_larger_than(k, p):
                pool.append([b*k, b, x, k, p])
                break
            k += 1
        if k <= 1:
            print(min(pool)[0])#, time()-t
            break
