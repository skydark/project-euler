#!/usr/bin/python
# -*- coding: utf-8 -*-

#Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    #1634 = 14 + 64 + 34 + 44
    #8208 = 84 + 24 + 04 + 84
    #9474 = 94 + 44 + 74 + 44

#As 1 = 14 is not a sum it is not included.

#The sum of these numbers is 1634 + 8208 + 9474 = 19316.

#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

#Answer:
	#443839

from time import time; t = time()

max_search = 6
power = 5
d = [i**power for i in range(10)]
def split_num(n, size):
    if size == 1 or n == 0:
        yield 0
        return
    j = 0
    for i in range(n+1):
        for v in split_num(n-i, size-1):
            yield j+v
        j += d[size-1]

s = -1
for n in split_num(max_search, 10):
    m = str(n)
    if n == sum(m.count(str(i))*d[i] for i in range(1, 10)):
        #print n
        s += n

print(s)#, time() - t
