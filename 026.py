#!/usr/bin/python
# -*- coding: utf-8 -*-

#A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    #1/2	= 	0.5
    #1/3	= 	0.(3)
    #1/4	= 	0.25
    #1/5	= 	0.2
    #1/6	= 	0.1(6)
    #1/7	= 	0.(142857)
    #1/8	= 	0.125
    #1/9	= 	0.(1)
    #1/10	= 	0.1

#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

#Answer:
	#983

# cheat...

from time import time; t = time()

def cycle(i):
    u, v = 1, 1
    while v % i != 0:
        u += 1
        v = (10*v+1)%i
    return u

for i in range(997, 0, -2):
    if i % 3 == 0 or i % 5 == 0: continue
    if cycle(i) == i - 1:
        print(i)#, time() - t
        break
