#!/usr/bin/python
# -*- coding: utf-8 -*-

#Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

#21 22 23 24 25
#20  7  8  9 10
#19  6  1  2 11
#18  5  4  3 12
#17 16 15 14 13

#It can be verified that the sum of the numbers on the diagonals is 101.

#What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

#Answer:
	#669171001

from time import time; t = time()

M = 1001
l = (M-1)/2

print(int(4*((M-1)*M*(2*M-1)/6 - 4*l*(l+1)*(2*l+1)/6) + 12 * l*(l+1)/2 + M*M))#, time()-t
