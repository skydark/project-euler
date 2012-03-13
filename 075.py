#!/usr/bin/python
# -*- coding: utf-8 -*-

#It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

#12 cm: (3,4,5)
#24 cm: (6,8,10)
#30 cm: (5,12,13)
#36 cm: (9,12,15)
#40 cm: (8,15,17)
#48 cm: (12,16,20)

#In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

#120 cm: (30,40,50), (20,48,52), (24,45,51)

#Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?

#Note: This problem has been changed recently, please check that you are using the right parameters.

#Answer:
	#161667

from time import time; t=time()
from mathplus import gcd, isqrt

M = 1500000
q = [0]*(M+1)
for m in range(2, isqrt(M/2)+1):
    for n in range(m % 2 + 1, min(m, M//(2*m)-m+1), 2):
        #length = 2*m*(m+n)
        #if length > M: break
        #x = m*m-n*n
        #y = 2*m*n
        #if gcd(x,y)==1:
        if gcd(m, n)==1:
            length = 2*m*(m+n)
            q[length] += 1

p = [0]*(M+1)
for m, c in enumerate(q):
    if c:
        for n in range(m, M+1, m):
            p[n] += c

print(sum(1 for i in p if i == 1))#, time()-t
