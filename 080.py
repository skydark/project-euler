#!/usr/bin/python
# -*- coding: utf-8 -*-

#It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

#The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

#For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.

#Answer:
	#40886

from time import time; t=time()
from mathplus import isqrt

M = 100

def get_root(n, m):
    #assert 0 < n < 100
    root = [0]*m
    root[0] = isqrt(n)
    n -= root[0]**2
    if n == 0: return [root[0]]
    a2 = root[0]*20
    for i in range(1, m):
        n *= 100
        for b in range(n//a2, -1, -1):
            k = (a2+b)*b
            if k < n:
                n -= k
                break
        root[i] = b
        a2 = 10*(a2+2*b)
    return root

print(sum(sum(get_root(n, 100)) for n in range(M) if n != isqrt(n)**2))#, time()-t
