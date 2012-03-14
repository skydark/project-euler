#!/usr/bin/python
# -*- coding: utf-8 -*-

#It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

#We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

#Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).

#Answer:
	#518408346

from time import time; t=time()
# Tip: Pell Equation

M = 1000000000

def pell3():
    x, y, k = 2, 1, 1
    while True:
        x, y, k = 2*x+3*y, x+2*y, -k
        yield x, y, k

s = 0
for x, y, k in pell3():
    ss = 2*x-2*k
    if ss > M: break
    s += ss

print(s)#, time()-t
