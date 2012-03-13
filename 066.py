#!/usr/bin/python
# -*- coding: utf-8 -*-

#Consider quadratic Diophantine equations of the form:

#x2 – Dy2 = 1

#For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

#It can be assumed that there are no solutions in positive integers when D is square.

#By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

#32 – 2×22 = 1
#22 – 3×12 = 1
#92 – 5×42 = 1
#52 – 6×22 = 1
#82 – 7×32 = 1

#Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

#Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

#Answer:
	#661

from time import time; t=time()
# http://zh.wikipedia.org/zh-cn/%E4%BD%A9%E5%B0%94%E6%96%B9%E7%A8%8B

M = 1000

maxx = 0
ss = 0
for i in range(1, 31):
    nn = i*i
    for j in range(1, 2*i+1):
        n = nn + j
        if n > M: break
        p, q = i, j
        expan = [i]
        while True:
            r, s = 1, 0
            for k in expan:
                r, s = k*r+s, r
            if r*r - n*s*s == 1:
                if r > maxx:
                    ss = n
                    maxx = r
                break
            s = i + p
            k, p = s//q, s%q-i
            expan.insert(0, k)
            m = n - p*p
            assert m % q == 0
            p, q = -p, m//q
print(ss)#, time()-t
