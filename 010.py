#!/usr/bin/python
# -*- coding: utf-8 -*-

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

#Answer:
	#142913828922

MAX = 2000000

from time import time; t=time()
from mathplus import isqrt

marked = [0] * MAX
value = 3
s = 2
limit = isqrt(MAX)+1
while value < limit:
    if marked[value] == 0:
        s += value
        for i in range(value*3, MAX, value*2):
            marked[i] = 1
    value += 2
for i in range(limit//2*2, MAX, 2):
    marked[i] = 1
s += sum(p+limit for p, f in enumerate(marked[limit:]) if f == 0)
print(s)#, time()-t
