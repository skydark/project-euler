#!/usr/bin/python
# -*- coding: utf-8 -*-

#The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 83 = 512. Another example of a number with this property is 614656 = 284.

#We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.

#You are given that a2 = 512 and a10 = 614656.

#Find a30.

#Answer:
	#248155780267521

from time import time; t=time()

# How can we make sure the magic limit number 100 & 20?

L = 30

ret = set()
for a in range(100):
    x = a
    for b in range(20):
        x *= a
        if x < 10: continue
        if sum(int(i) for i in str(x)) == a: ret.add(x)

print(sorted(ret)[L-1])#, len(ret), time()-t
