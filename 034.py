#!/usr/bin/python
# -*- coding: utf-8 -*-

#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

#Find the sum of all numbers which are equal to the sum of the factorial of their digits.

#Note: as 1! = 1 and 2! = 2 are not sums they are not included.

#Answer:
	#40730

from time import time; t = time()
from mathplus import factorial

d = [factorial(i) for i in range(10)]
M = d[9]*6
s = -3
def split_num(n, size):
    if size == 1:
        yield [n], n
        return
    if n == 0:
        yield [0]*size, 0
        return
    j = 0
    for i in range(n+1):
        for k, v in split_num(n-i, size-1):
            yield k+[i], j+v
        j += d[size-1]

for c in range(1, 7):
    for k, v in split_num(c, 10):
        m = str(v)
        if all((m.count(str(i)) == k[i]) for i in range(10)):
            #print k, v
            s += v
print(s)#, time()-t
