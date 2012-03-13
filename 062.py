#!/usr/bin/python
# -*- coding: utf-8 -*-

#The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

#Find the smallest cube for which exactly five permutations of its digits are cube.

#Answer:
	#127035954683

#from time import time; t=time()
from itertools import permutations

c = [str(i) for i in range(10)]
pool = {}
n = 346
while True:
    n3 = n*n*n
    s = str(n3)
    k = tuple(s.count(c[i]) for i in range(10))
    pool.setdefault(k, [])
    pool[k].append(n3)
    if len(pool[k]) == 5:
        print(pool[k][0])#, time()-t
        break
    n += 1
