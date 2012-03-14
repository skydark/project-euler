#!/usr/bin/python
# -*- coding: utf-8 -*-

#A Hamming number is a positive number which has no prime factor larger than 5.
#So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
#There are 1105 Hamming numbers not exceeding 108.

#We will call a positive number a generalised Hamming number of type n, if it has no prime factor larger than n.
#Hence the Hamming numbers are the generalised Hamming numbers of type 5.

#How many generalised Hamming numbers of type 100 are there which don't exceed 109?

#Answer:
	#2944730

from time import time; t=time()
from mathplus import log10

M = 9

P = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
pl = [log10(p) for p in P]

def f(pos, limit):
    if pos == 0: return int(limit/pl[0])+1
    v = pl[pos]
    pos -= 1
    s = 0
    while limit > 0:
        s += f(pos, limit)
        limit -= v
    return s

print(f(len(pl)-1, M))#, time()-t
