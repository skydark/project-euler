#!/usr/bin/python
# -*- coding: utf-8 -*-

#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

#The product 7254 is unusual, as the identity, 39  186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

#Answer:
    #45228  

from time import time; t=time()
from mathplus import permutations, reduce

def to_int(l):
    return reduce(lambda x, y: x*10+y, l)

ret = set()
for i in permutations(range(1, 10), 9):
    if i[0] >= 8: break
    if i[0]*i[2] < 10 and i[1]*i[4] % 10 == i[8]:
        r = to_int(i[5:])
        if to_int(i[:2]) * to_int(i[2:5]) == r:
            ret.add(r)
    if i[0]*i[1] < 10 and i[0]*i[4] % 10 == i[8]:
        r = to_int(i[5:])
        if to_int(i[:1]) * to_int(i[1:5]) == r:
            ret.add(r)
print(sum(ret))#, time()-t
