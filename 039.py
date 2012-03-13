#!/usr/bin/python
# -*- coding: utf-8 -*-

#If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

#{20,48,52}, {24,45,51}, {30,40,50}

#For which value of p ≤ 1000, is the number of solutions maximised?

#Answer:
	#840

from time import time; t=time()
from mathplus import isqrt, gcd

M = 1000

p = [0] * (M//2+1)
q = [0] * (M//2+1)
for n in range(1, M//2+1):
    for k in range(1, n):
        if n % k != 0: continue
        m = n//k
        if q[m] == 0:
            for i in range(isqrt(m//2)+1, isqrt(m)+1):
                if m % i != 0: continue
                u, v = i, m//i - i
                if (u+v) % 2 != 0 and gcd(u, v) == 1:
                    q[m] += 1
                    #if n == 60: 
                        #print k, u, v, k*(u*u-v*v), 2*k*u*v, k*(u*u+v*v)
        p[n] += q[m]

print(max((x, i) for i, x in enumerate(p))[1]*2)#, time()-t
'''
from time import time; t=time()
from mathplus import isqrt, gcd

M = 1000

ss = 0
MM = M/2+1
p = [0] * MM
q = [0] * MM
isqrtm = [isqrt(m) for m in xrange(MM)]
for m in range(1, MM):
    for i in range(isqrtm[m/2]+1, isqrtm[m]+1):
        if m % i != 0: continue
        mi = m/i 
        if mi % 2 == 0: continue
        u, v = i, mi - i
        if gcd(u, v) == 1:
            q[m] += 1
            #if n == 60: print k, u, v, k*(u*u-v*v), 2*k*u*v, k*(u*u+v*v)
    for n in xrange(m, MM, m):
        p[n] += q[m]

print max((x, i) for i, x in enumerate(p))[1]*2, time()-t
'''
