#!/usr/bin/python
# -*- coding: utf-8 -*-

#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

#Evaluate the sum of all the amicable numbers under 10000.

#Answer:
	#31626

from time import time; t = time()

M=10000

d = [0] * M
for i in range(1, M//2):
    for j in range(i*2, M, i):
        d[j] += i

s = sum(i+d[i] for i in range(M) if d[i] < i and i == d[d[i]])
print(s)#, time()-t
