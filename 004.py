#!/usr/bin/python
# -*- coding: utf-8 -*-

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

#Answer:
	#906609

from time import time; t=time()
from mathplus import palindrome

ret = 0
for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        x = i * j
        if x <= ret: break
        if palindrome(x):
            ret = x

print(ret)#, time()-t
