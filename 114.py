#!/usr/bin/python
# -*- coding: utf-8 -*-

#A row measuring seven units in length has red blocks with a minimum length of three units placed on it, such that any two red blocks (which are allowed to be different lengths) are separated by at least one black square. There are exactly seventeen ways of doing this.

#How many ways can a row measuring fifty units in length be filled?

#NOTE: Although the example above does not lend itself to the possibility, in general it is permitted to mix block sizes. For example, on a row measuring eight units in length you could use red (3), black (1), and red (4).

#Answer:
	#16475640049

from time import time; t=time()
from mathplus import memorize

N = 50
L = 3

@memorize
def tiles(n):
    return 1 + sum((k-L+1)*tiles(n-k-1) for k in range(L, n+1))

print(tiles(N))#, time()-t
