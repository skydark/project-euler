#!/usr/bin/python
# -*- coding: utf-8 -*-

#An irrational decimal fraction is created by concatenating the positive integers:

#0.123456789101112131415161718192021...

#It can be seen that the 12th digit of the fractional part is 1.

#If dn represents the nth digit of the fractional part, find the value of the following expression.

#d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

#Answer:
	#210

from time import time; t = time()
from mathplus import op, reduce

def idf(n):
    n -= 1
    i = 1
    c = (10**i-10**(i-1))*i
    while n > c:
        n -= c
        i += 1
        c = (10**i-10**(i-1))*i
    u, v = n / i, n % i
    return int(str(10**(i-1)+u)[v])

d = [1, 10, 100, 1000, 10000, 100000, 1000000]
d = map(idf, d)
#print d
print(reduce(op.mul, d, 1))#, time()-t
