#!/usr/bin/python
# -*- coding: utf-8 -*-

#We can easily verify that none of the entries in the first seven rows of Pascal's triangle are divisible by 7:
  	  	  	  	  	  	 #1
  	  	  	  	  	 #1 	  	 1
  	  	  	  	 #1 	  	 2 	  	 1
  	  	  	 #1 	  	 3 	  	 3 	  	 1
  	  	 #1 	  	 4 	  	 6 	  	 4 	  	 1
  	 #1 	  	 5 	  	10 	  	10 	  	 5 	  	 1
#1 	  	 6 	  	15 	  	20 	  	15 	  	 6 	  	 1

#However, if we check the first one hundred rows, we will find that only 2361 of the 5050 entries are not divisible by 7.

#Find the number of entries which are not divisible by 7 in the first one billion (109) rows of Pascal's triangle.

#Answer:
	#2129970655314432

from time import time; t=time()

M = 10**9

def int2(n, base):
    ret = []
    while n != 0:
        n, k = n//base, n%base
        ret.insert(0, k)
    return ret

def f(l, base):
    if not l: return 0
    r = l[0]
    if r == 0: return f(l[1:], base)
    if r < base: r*(r+1)//2
    s = base*(base+1)//2
    return r*(r+1)//2*s**(len(l)-1)+(r+1)*f(l[1:], base)

print(f(int2(M, 7), 7))#, time()-t
