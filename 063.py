#!/usr/bin/python
# -*- coding: utf-8 -*-

#The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

#How many n-digit positive integers exist which are also an nth power?

#Answer:
	#49

#from time import time; t=time()
from math import log10

print(sum(int(1/(1-log10(i))) for i in range(1, 10)))#, time()-t
