#!/usr/bin/python
# -*- coding: utf-8 -*-

#The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

#Let us list the factors of the first seven triangle numbers:

     #1: 1
     #3: 1,3
     #6: 1,2,3,6
    #10: 1,2,5,10
    #15: 1,3,5,15
    #21: 1,3,7,21
    #28: 1,2,4,7,14,28

#We can see that 28 is the first triangle number to have over five divisors.

#What is the value of the first triangle number to have over five hundred divisors?

#Answer:
	#76576500

from time import time; t=time()
from mathplus import get_primes_by_sieve, isqrt
#from mathplus import factorization, reduce, op

LEAST = 500

SIZE = 100
primes, sieves = get_primes_by_sieve(SIZE)
PRIME_CNT = len(primes)

def func(n):
    global primes, sieves, SIZE, PRIME_CNT
    factors = 1
    while n % 2 == 0:
        factors += 1
        n /= 2
    if factors >= 2: factors -= 1
    isqrtn = isqrt(n)
    while isqrtn >= PRIME_CNT:
        SIZE = 10*SIZE
        primes, sieves = get_primes_by_sieve(SIZE)
        PRIME_CNT = len(primes)
    for i in range(1,isqrtn):
        cnt = 1
        p = primes[i]
        while n % p == 0:
            cnt += 1
            n /= p
        factors *= cnt
        if n == 1: break
    return factors

#func=lambda x: reduce(op.mul, (j+1 if i != 2 else j for i, j in factorization(x)))

triangle = 7
f1, f2 = func(triangle), func(triangle+1)
while True:
    f1, f2 = f2, func(triangle+1)
    if f1 * f2 > LEAST:
        print(triangle*(triangle+1)//2)#, time()-t
        break
    triangle += 1
