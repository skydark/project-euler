#!/usr/bin/python
# -*- coding: utf-8 -*-

#Using a combination of black square tiles and oblong tiles chosen from: red tiles measuring two units, green tiles measuring three units, and blue tiles measuring four units, it is possible to tile a row measuring five units in length in exactly fifteen different ways.

#How many ways can a row measuring fifty units in length be tiled?

#NOTE: This is related to problem 116.

#Answer:
	#100808458960497

from time import time; t=time()
from mathplus import memorize

N = 50
M = (2, 3, 4)

@memorize
def tiles(n):
    return 1 + sum(tiles(k) for m in M for k in range(n-m+1))

print(tiles(N))#, time()-t
