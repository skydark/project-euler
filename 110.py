#!/usr/bin/python
# -*- coding: utf-8 -*-

#In the following equation x, y, and n are positive integers.
#1/x + 1/y = 1/n

#It can be verified that when n = 1260 there are 113 distinct solutions and this is the least value of n for which the total number of distinct solutions exceeds one hundred.

#What is the least value of n for which the number of distinct solutions exceeds four million?

#NOTE: This problem is a much more difficult version of problem 108 and as it is well beyond the limitations of a brute force approach it requires a clever implementation.

#Answer:
	#9350130049860600

from time import time; t=time()
from mathplus import reduce, op

M = 4000000
L = M*2-1
S = 15#assert S == int(log(L)/log(3))+1 == len(primes)
primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

min_n = reduce(op.mul, primes, 1)

def get_next(pos, n, k, limit):
    global min_n
    if k >= L:
        if n < min_n: min_n = n
        return True
    #if pos == S: return False
    for p in range(1, limit+1):
        n *= primes[pos]
        if n > min_n: break
        if get_next(pos+1, n, k*(2*p+1), p): break
    return False

get_next(0, 1, 1, M)

print(min_n)#, time()-t
