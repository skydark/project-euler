#!/usr/bin/python
# -*- coding: utf-8 -*-

#Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,

#where each "_" is a single digit.

#Answer:
	#1389019170

from time import time; t=time()

min_ = 101010103//10
max_ = 138902657//10

for n in range(max_, min_-1, -1):#(min_, max_+1):
    n10 = n*10
    for n in (n10+3, n10+7):
        n2 = n*n
        diff = n2 - 10203040506070809
        while diff > 0:
            last = diff % 10
            if last != 0: break
            diff //= 100
        else:
            print(n*10)#, time()-t
            import sys; sys.exit()
