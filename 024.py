#!/usr/bin/python
# -*- coding: utf-8 -*-

#A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

#012   021   102   120   201   210

#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

#Answer:
	#2783915460

from time import time; t = time()
from mathplus import permutations, factorial

I = 1000000
size = 10

def direct_no_thinking(n, size):
    return list(permutations(range(size)))[n]

def a_bit_thinking(n, size, choices=None):
    if choices is None: choices = range(size)
    if size == 1: return choices
    s = factorial(size-1)
    m, n = choices[n//s], n%s
    return [m]+a_bit_thinking(n, size-1, [i for i in choices if i != m])

method = a_bit_thinking
print(''.join(str(i) for i in method(I-1, size)))#, time()-t
