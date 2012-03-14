#!/usr/bin/python
# -*- coding: utf-8 -*-

#The Fibonacci sequence is defined by the recurrence relation:

#Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
#It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

#Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.

#Answer:
	#329468

from time import time; t=time()
from math import log10, sqrt

M = 1000000000
sqrt5 = sqrt(5)
phi = log10((sqrt5+1)/2)
logsqrt5 = log10(sqrt5)

def test(n):
    if n < 100000000: return False
    flags = [0]*10
    flags[0] = 1
    while n > 0:
        n, m = n//10, n%10
        if flags[m]: return False
        flags[m] = 1
    return True

def first(n, s):
    return n//(10**(int(log10(n))-8))

a, b, k = 1, 1, 2
while True:
    a, b, k = b, a+b, k+1
    a, b, k = b % M, (a+b)%M, k+1
    if test(b):
        phik = phi*k-logsqrt5
        n = int(10**(phik-int(phi*k)+9))//10
        if test(n): break

print(k)#, time()-t
