#!/usr/bin/python
# -*- coding: utf-8 -*-

#Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

#37 36 35 34 33 32 31
#38 17 16 15 14 13 30
#39 18  5  4  3 12 29
#40 19  6  1  2 11 28
#41 20  7  8  9 10 27
#42 21 22 23 24 25 26
#43 44 45 46 47 48 49

#It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13  62%.

#If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

#Answer:
	#26241

#from time import time; t=time()
from mathplus import isqrt, sieve, get_primes_by_sieve

M = 23000
primes, sieves = get_primes_by_sieve(M, odd_only=True)
max_prime = primes[-1]

def is_prime(n):
    if n <= M: return sieves[n]
    for i in primes:
        if n % i == 0: return False
    for i in range(max_prime+2, isqrt(n), 2):
        if n % i == 0: return False
    return True

a, b = 0, 1
n2 = 1
double_n = 2
#print time() - t
while True:
    for i in range(1, 4):
        a += is_prime(n2+double_n*i)
    b += 4
    if 10*a < b: break
    n2 += double_n*4
    double_n += 2
print(double_n+1)#, time()-t
