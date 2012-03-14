#!/usr/bin/python
# -*- coding: utf-8 -*-

#By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

#Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.

#Answer:
	#2772

from time import time; t=time()
from mathplus import isqrt

M = 2000000

def tria(n):
    return n*(n+1)
def is_tria(n):
    n4 = n*8+1
    return isqrt(n4)**2 == n4
#n*(n+1)*m*(m+1) = M*4

cnt = 0
while True:
    cnt += 1
    for k in (M-cnt, M+cnt):
        sn = 0
        n = 1
        while True:
            sn += n
            n += 1
            if sn > k: break
            if k % sn != 0 or not is_tria(k//sn): continue
            m = (isqrt(k/sn*8+1)-1)//2
            print((n-1)*m)#, time()-t, n-1, m
            import sys; sys.exit()
