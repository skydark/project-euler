#!/usr/bin/python
# -*- coding: utf-8 -*-

#The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 62 + 72 + 82 + 92 + 102 + 112 + 122.

#There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164. Note that 1 = 02 + 12 has not been included as this problem is concerned with the squares of positive integers.

#Find the sum of all the numbers less than 108 that are both palindromic and can be written as the sum of consecutive squares.

#Answer:
	#2906969179

from time import time; t=time()
from mathplus import isqrt, palindrome

M = 10**8
s = isqrt(M/2)
pool = [0]*(s+1)
for i in range(s):
    pool[i+1] = pool[i] + i*i

ss = set()
for u in range(s-1):
    for v in range(u+2, s+1):
        x = pool[v] - pool[u]
        if x >= M: break
        if palindrome(x): ss.add(x)

print(sum(ss)-1)#, time()-t
