#!/usr/bin/python
# -*- coding: utf-8 -*-

#Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

#1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

#It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

#Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference is pentagonal and D = |Pk − Pj| is minimised; what is the value of D?

#Answer:
	#5482660

from time import time; t = time()
#import psyco; psyco.full()
from mathplus import isqrt

ps = []
pool = {}
d = 10000000000
def pentagonal():
    i = 1
    x = 0
    while True:
        #x = i*(3*i-1)/2
        x += 3*i-2
        ps.append(x)
        yield x
        i += 1

def is_pentagonal(n):
    n2 = n*24+1
    n = isqrt(n2)
    return n*n == n2 and (n+1) % 6 == 0

p_iter = pentagonal()
l = 0
for p in p_iter:
    l += 1
    if 1.5*l*l-6.5*l+2 > d: break
    for i in range(l-1, -1, -1):
        if ps[i]*2 <= p: break
        a, b = ps[i]*2-p, p-ps[i]
        if is_pentagonal(a) and is_pentagonal(b):
            #print a, b, ps[i], p
            d = a

print(d)#, time()-t
