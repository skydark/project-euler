#!/usr/bin/python
# -*- coding: utf-8 -*-

#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

#What is the largest n-digit pandigital prime that exists?

#Answer:
	#7652413

from time import time; t = time()
from mathplus import first_factor, permutations, reduce

p = 0
for ps in permutations(range(7, 0, -1)):
    if ps[0] == 5: continue
    p = reduce(lambda x, y: 10*x+y, ps)
    if first_factor(p) == p:
        break

print(p)#, time()-t
