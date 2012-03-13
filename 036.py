#!/usr/bin/python
# -*- coding: utf-8 -*-

#The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

#(Please note that the palindromic number, in either base, may not include leading zeros.)

#Answer:
	#872187

from time import time; t = time()
from mathplus import palindrome

M = 1000000
s = 0
for i in range(1, M, 2):
    if not palindrome(i): continue
    m = bin(i)[2:]
    if int(m[::-1], 2) == i:
        #print i
        s += i

print(s)#, time()-t
