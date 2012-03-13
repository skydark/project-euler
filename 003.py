#!/usr/bin/python
# -*- coding: utf-8 -*-

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

#Answer:
	#6857

from time import time; t=time()
from mathplus import prime

NUM = 600851475143

n = NUM
last = 1
for p in prime():
    while n % p == 0:
        n /= p
        last = p
    if n == 1:
        break

print(last)#, time()-t
