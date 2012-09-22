#!/usr/bin/python
# -*- coding: utf-8 -*-

# Consider the number 45656.
# It can be seen that each pair of consecutive digits of 45656 has a difference of one.
# A number for which every pair of consecutive digits has a difference of one is called a step number.
# A pandigital number contains every decimal digit from 0 to 9 at least once.
# How many pandigital step numbers less than 1040 are there? 

#Answer:
	#126461847755

from time import time; t=time()
from mathplus import memorize

N = 40

@memorize
def pe178(n, k, s1):
    if n < len(s1) or k < 0 or k > 9:
        return 0
    if not s1 and n == 0:
        return 1
    s1 = set(s1)
    s2 = s1.copy()
    s1.discard(k-1)
    s2.discard(k+1)
    s1 = tuple(sorted(s1))
    s2 = tuple(sorted(s2))
    return pe178(n-1, k-1, s1)+pe178(n-1, k+1, s2)

s = 1  #9876543210
for k in range(1, 10):
    sset = set(range(10))
    sset.remove(k)
    sset = tuple(sorted(sset))
    for j in range(10, N):
        s += pe178(j, k, sset)

print(s)#, time()-t)
