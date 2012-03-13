#!/usr/bin/python
# -*- coding: utf-8 -*-

#It is possible to write five as a sum in exactly six different ways:

#4 + 1
#3 + 2
#3 + 1 + 1
#2 + 2 + 1
#2 + 1 + 1 + 1
#1 + 1 + 1 + 1 + 1

#How many different ways can one hundred be written as a sum of at least two positive integers?

#Answer:
	#190569291

from time import time; t=time()
from mathplus import memorize

M = 100

@memorize
def sp(n, m):
    #assert n >= m
    if n <= 1 or m == 1: return 1
    s = 0
    for i in range(m, 0, -1):
        s += sp(n-i, min(i, n-i))
    return s

print(sp(M, M)-1)#, time()-t
