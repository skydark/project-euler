#!/usr/bin/python
# -*- coding: utf-8 -*-

#The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form ΔOPQ.

#There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is,
#0 ≤ x1, y1, x2, y2 ≤ 2.

#Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?

#Answer:
	#14234

from time import time; t=time()

M = 50

s = M*M
ss = M*M
for x1 in range(1, M+1):
    for y1 in range(1, M+1):
        a = x1*x1+y1*y1
        for x2 in range(x1+1, M+1):
            x212a = (x2-x1)**2+a
            x22 = x2*x2
            for y2 in range(0, y1):
                b = (y2-y1)**2+x212a#(x2-x1)**2+a
                c = y2*y2+x22#x2*x2
                if b < c: break
                if b == c:
                    ss += 1
                    break

print(s+ss*2)#, time()-t
