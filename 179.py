#!/usr/bin/python
# -*- coding: utf-8 -*-

#Find the number of integers 1 < n < 107, for which n and n + 1 have the same number of positive divisors. For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.

#Answer:
	#986262

from time import time; t=time()
from mathplus import isqrt

M=10**7

sieves = [2]*M
sieves[0] = 0
sieves[1] = 1
for n in range(2, isqrt(M)):
    nn = n*n
    for m in range(nn, M, n): sieves[m] += 2
    sieves[nn] -= 1
s = sum(1 for n in range(3, M) if sieves[n] == sieves[n-1])

print(s)#, time()-t
