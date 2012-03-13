#!/usr/bin/python
# -*- coding: utf-8 -*-

#It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

#9 = 7 + 2×12
#15 = 7 + 2×22
#21 = 3 + 2×32
#25 = 7 + 2×32
#27 = 19 + 2×22
#33 = 31 + 2×12

#It turns out that the conjecture was false.

#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

#Answer:
	#5777

from time import time; t=time()
from mathplus import sieve, isqrt

M = 10000
p = sieve(M)

for n in range(35, M, 2):
    if p[n]: continue
    for i in range(1, isqrt((n-3)/2)+1):
        if p[n-2*i*i]: break
    else:
        print(n)#, time()-t
        break
