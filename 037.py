#!/usr/bin/python
# -*- coding: utf-8 -*-

#The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

#NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

#Answer:
	#748317

from time import time; t=time()
from mathplus import is_prime

M = 6
pl = [[3, 7]]
pr = [[2, 3, 5, 7]]

for n in range(1, M):
    newpl = []
    newpr = []
    for p in pl[-1]:
        b = 10**n
        newpl += list(filter(is_prime, [(b*i+p) for i in (1, 2, 3, 5, 7, 9)]))
    for p in pr[-1]:
        newpr += list(filter(is_prime, [(10*p+i) for i in (1, 2, 3, 5, 7, 9)]))
    pl.append(newpl)
    pr.append(newpr)
ret = filter(lambda i: i >= 10, set(sum(pl, [])).intersection(set(sum(pr, []))))
#assert len(ret) == 11, ret
#ret = [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
print(sum(ret))#, time()-t
