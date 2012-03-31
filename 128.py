#!/usr/bin/python
# -*- coding: utf-8 -*-

#A hexagonal tile with number 1 is surrounded by a ring of six hexagonal tiles, starting at "12 o'clock" and numbering the tiles 2 to 7 in an anti-clockwise direction.

#New rings are added in the same fashion, with the next rings being numbered 8 to 19, 20 to 37, 38 to 61, and so on. The diagram below shows the first three rings.

#By finding the difference between tile n and each its six neighbours we shall define PD(n) to be the number of those differences which are prime.

#For example, working clockwise around tile 8 the differences are 12, 29, 11, 6, 1, and 13. So PD(8) = 3.

#In the same way, the differences around tile 17 are 1, 17, 16, 1, 11, and 10, hence PD(17) = 2.

#It can be shown that the maximum value of PD(n) is 3.

#If all of the tiles for which PD(n) = 3 are listed in ascending order to form a sequence, the 10th tile would be 271.

#Find the 2000th tile in this sequence.

#Answer:
	#14516824220

from time import time; t=time()
from mathplus import get_primes_by_sieve

# 3n(n-1)+2, where 6n-1, 6n+1, 12n+5 in primes

N = 2000
M = 1000000

_, sieves = get_primes_by_sieve(M)

s, r = 1, 0
for n in range(2, (M-5)//12):
    if sieves[6*n-7] and sieves[6*n-1] and sieves[12*n-19]:
        s += 1
        if s == N:
            r = 3*n*(n-1)+1
            break
    if sieves[6*n-1] and sieves[6*n+1] and sieves[12*n+5]:
        s += 1
        if s == N:
            r = 3*n*(n-1)+2
            break

print(r)#, time()-t)
