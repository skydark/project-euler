#!/usr/bin/python
# -*- coding: utf-8 -*-

#A row of five black square tiles is to have a number of its tiles replaced with coloured oblong tiles chosen from red (length two), green (length three), or blue (length four).

#If red tiles are chosen there are exactly seven ways this can be done.

#If green tiles are chosen there are three ways.

#And if blue tiles are chosen there are two ways.

#Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of replacing the black tiles in a row measuring five units in length.

#How many different ways can the black tiles in a row measuring fifty units in length be replaced if colours cannot be mixed and at least one coloured tile must be used?

#NOTE: This is related to problem 117.

#Answer:
	#20492570929

from time import time; t=time()
from mathplus import memorize

N = 50
M = (2, 3, 4)

@memorize
def tiles(n, m):
    return 1 + sum(tiles(k, m) for k in range(n-m+1))

print(sum(tiles(N, k)-1 for k in M))#, time()-t
