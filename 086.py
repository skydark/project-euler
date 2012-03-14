#!/usr/bin/python
# -*- coding: utf-8 -*-

#A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.

#However, there are up to three "shortest" path candidates for any given cuboid and the shortest route is not always integer.

#By considering all cuboid rooms with integer dimensions, up to a maximum size of M by M by M, there are exactly 2060 cuboids for which the shortest distance is integer when M=100, and this is the least value of M for which the number of solutions first exceeds two thousand; the number of solutions is 1975 when M=99.

#Find the least value of M such that the number of solutions first exceeds one million.

#Answer:
	#1818

from time import time; t=time()
from mathplus import isqrt

L = 1000000

def test(u, v):
    w = u*u+v*v
    return w == isqrt(w)**2

m = 0
ss = 0
while ss < L:
    m += 1
    for bc in range(2, m+1):
        # 2 <= b+c <= m
        if test(m, bc): ss += bc//2
    m2 = 2*m+2
    for bc in range(m+1, 2*m):
        if test(m, bc): ss += (m2-bc)//2
print(m)#, time()-t
