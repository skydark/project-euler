#!/usr/bin/python
# -*- coding: utf-8 -*-

#It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

#Answer:
	#142857


#print 142857

from time import time; t=time()

M = 1000000
for i in range(1, M):
    x = ''.join(sorted(str(i)))
    for j in range(1, 7):
        if ''.join(sorted(str(i*j))) != x: break
    else:
        print(i)#, time()-t
        break
