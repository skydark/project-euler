#!/usr/bin/python
# -*- coding: utf-8 -*-

#In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    #1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

#It is possible to make £2 in the following way:

    #1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

#How many different ways can £2 be made using any number of coins?

#Answer:
	#73682  

from time import time; t = time()

M = 200
d = [1, 2, 5, 10, 20, 50, 100, 200]
d.reverse()

def diff_ways(n, d):
    if len(d) == 1: return n % d[0] == 0
    new_d = d[1:]
    return sum(diff_ways(i, new_d) for i in range(n, -1, -d[0]))

print(diff_ways(M, d))#, time()-t
