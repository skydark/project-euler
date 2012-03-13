#!/usr/bin/python
# -*- coding: utf-8 -*-

#The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

#1! + 4! + 5! = 1 + 24 + 120 = 145

#Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

#169 → 363601 → 1454 → 169
#871 → 45361 → 871
#872 → 45362 → 872

#It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

#69 → 363600 → 1454 → 169 → 363601 (→ 1454)
#78 → 45360 → 871 → 45361 (→ 871)
#540 → 145 (→ 145)

#Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

#How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

#Answer:
	#402

from time import time; t=time()
from mathplus import factorial

M = 1000000
MM = 2177282
L = 60

fact = [factorial(n) for n in range(10)]
facts = [0]*MM
facts[:10] = fact[:]
for n in range(10, MM):
    facts[n] = facts[n//10]+fact[n%10]
#print time()-t

ss = 0
for n in range(M):
    m = n
    way = {}
    while m not in way:
        way[m] = 1
        m = facts[m]
    if len(way) == 60:
        ss += 1
print(ss)#, time()-t
