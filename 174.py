#!/usr/bin/python
# -*- coding: utf-8 -*-

#We shall define a square lamina to be a square outline with a square "hole" so that the shape possesses vertical and horizontal symmetry.

#Given eight tiles it is possible to form a lamina in only one way: 3x3 square with a 1x1 hole in the middle. However, using thirty-two tiles it is possible to form two distinct laminae.

#If t represents the number of tiles used, we shall say that t = 8 is type L(1) and t = 32 is type L(2).

#Let N(n) be the number of t ≤ 1000000 such that t is type L(n); for example, N(15) = 832.

#What is ∑ N(n) for 1 ≤ n ≤ 10?

#Answer:
	#209566

from time import time; t=time()
from mathplus import isqrt

M = 1000000
N = range(1, 11)#(15,)#

M //= 4
facts = [1]*(M+1)
facts[0] = 0
for i in range(1, isqrt(M+1)):
    facts[i*i] -= 1
for i in range(1, M+1):
    for j in range(i, M+1, i):
        facts[j] += 1
    facts[i] //= 2

s = [0]*len(N)
for i, n in enumerate(N):
    s[i] = facts.count(n)

print(sum(s))#, time()-t
