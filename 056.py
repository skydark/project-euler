#!/usr/bin/python
# -*- coding: utf-8 -*-

#A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

#Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

#Answer:
	#972

#from time import time; t=time()

print(max(sum(int(i) for i in str(a**b)) for a in range(100) for b in range(100)))#, time()-t
