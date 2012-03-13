#!/usr/bin/python
# -*- coding: utf-8 -*-

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Answer:
	#232792560

from time import time; t=time()
from mathplus import prime, log

NUM = 20

n = NUM
logn = log(NUM)
ret = 1
for p in prime():
    if p > n: break
    ret *= p**int(logn/log(p))
print(ret)#, time()-t
