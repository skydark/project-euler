#!/usr/bin/python
# -*- coding: utf-8 -*-

#The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

#Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    #* d2d3d4=406 is divisible by 2
    #* d3d4d5=063 is divisible by 3
    #* d4d5d6=635 is divisible by 5
    #* d5d6d7=357 is divisible by 7
    #* d6d7d8=572 is divisible by 11
    #* d7d8d9=728 is divisible by 13
    #* d8d9d10=289 is divisible by 17

#Find the sum of all 0 to 9 pandigital numbers with this property.

#Answer:
	#16695334890

from time import time; t=time()
from mathplus import permutations, reduce

def three(d, i):
    return d[i]*100+d[i+1]*10+d[i+2]

ret = []
for d in permutations(range(10)):
    if d[5] != 0 and d[5] != 5: continue
    if d[3] % 2 != 0: continue
    #if three(d, 1) % 2 != 0: continue
    if (d[2]+d[3]+d[4]) % 3 != 0: continue
    #if three(d, 2) % 3 != 0: continue
    #if three(d, 3) % 5 != 0: continue
    if (d[4]*2+d[5]*3+d[6]) % 7 != 0: continue
    #if three(d, 4) % 7 != 0: continue
    if (d[5]-d[6]+d[7]) % 11 != 0: continue
    #if three(d, 5) % 11 != 0: continue
    if (d[6]*9-d[7]*3+d[8]) % 13 != 0: continue
    #if three(d, 6) % 13 != 0: continue
    if (-2*d[7]-7*d[8]+d[9]) % 17 != 0: continue
    #if three(d, 7) % 17 != 0: continue
    ret.append(reduce(lambda x, y:10*x+y, d))
print(sum(ret))#, time()-t
