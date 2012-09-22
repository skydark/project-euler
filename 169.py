#!/usr/bin/python
# -*- coding: utf-8 -*-

# Define f(0)=1 and f(n) to be the number of different ways n can be expressed as a sum of integer powers of 2 using each power no more than twice.
# 
# For example, f(10)=5 since there are five different ways to express 10:
# 
# 1 + 1 + 8
# 1 + 1 + 4 + 4
# 1 + 1 + 2 + 2 + 4
# 2 + 4 + 4
# 2 + 8
# 
# What is f(1025)?

#Answer:
	#178653872807

from time import time; t=time()
from mathplus import memorize, log

N = 10**25

@memorize
def pe169(n, k=None):
    if n < 0:
        return 0
    if n <= 1:
        return 1
    k2 = int(log(n, 2))
    if k is None:
        k = k2
    elif k < k2 - 1:
        return 0
    else:
        k = min(k, k2)
    if k == 0:
        return 1 if n < 3 else 0
    kmax = 2 ** k
    return pe169(n, k-1)+pe169(n-kmax, k-1)+pe169(n-kmax*2, k-1)

print(pe169(N))#, time()-t)
