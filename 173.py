#!/usr/bin/python
# -*- coding: utf-8 -*-

#We shall define a square lamina to be a square outline with a square "hole" so that the shape possesses vertical and horizontal symmetry. For example, using exactly thirty-two square tiles we can form two different square laminae:

#With one-hundred tiles, and not necessarily using all of the tiles at one time, it is possible to form forty-one different square laminae.

#Using up to one million tiles how many different square laminae can be formed?

#Answer:
	#1572729

from time import time; t=time()
from mathplus import isqrt

M = 1000000

M += 1
sieves = [0]*M
for n in range(2, isqrt(M)):
    for m in range(n*(n+2), M, n*2): sieves[m] += 1

s = sum(sieves[n] for n in range(4, M, 4))

print(s)#, time()-t
