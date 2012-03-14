#!/usr/bin/python
# -*- coding: utf-8 -*-

#Given is the arithmetic-geometric sequence u(k) = (900-3k)rk-1.
#Let s(n) = Σk=1...nu(k).

#Find the value of r for which s(5000) = -600,000,000,000.

#Give your answer rounded to 12 places behind the decimal point.

#Answer:
	#1.002322108633

from time import time; t=time()
from mathplus import isqrt
from decimal import Decimal

n = 5000
ans = -600000000000*-1
threshold = 1
jd = 10**13
start = 10020000000000
end = 10030000000000

def f(r):
    c=Decimal(int(r))/jd
    d=c**n
    e=(1-d)/(1-c)
    s=900*e-3*(e-n*d)/(1-c)
    return -s

def binary(f, start, end, reach):
    m = (start+end)//2
    if m in (start, end): return m
    a = f(m)
    #print start, end, a
    if a == reach: return m
    if a < reach: return binary(f, m, end, reach)
    return binary(f, start, m, reach)

print(Decimal((binary(f, start, end, ans)+5)//10)*10/jd)#, time()-t
