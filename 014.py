#!/usr/bin/python
# -*- coding: utf-8 -*-

#The following iterative sequence is defined for the set of positive integers:

#n → n/2 (n is even)
#n → 3n + 1 (n is odd)

#Using the rule above and starting with 13, we generate the following sequence:
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

#Which starting number, under one million, produces the longest chain?

#NOTE: Once the chain starts the terms are allowed to go above one million.

#Answer:
	#837799

from time import time; t=time()
#import psyco; psyco.full()

LIMIT = 1000000
SIZE = LIMIT
#SIZE = int(LIMIT*1.2)

pool = [-1]*SIZE
pool[1] = 0
m = 0
m_i = 0
def mark(i):
    if i < SIZE and pool[i] >= 0:
        return pool[i]
    j = i//2 if i % 2 == 0 else i*3+1
    c = mark(j) + 1
    if i < SIZE:
        pool[i] = c
    return c

for i in range(LIMIT//2, LIMIT):
    if pool[i] >= 0: continue
    j = mark(i)
    if j > m:
        m, m_i = j, i
print(m_i)#, time()-t)
#print max((j, i) for i, j in enumerate(pool[LIMIT/2:LIMIT]))[1]
