#!/usr/bin/python
# -*- coding: utf-8 -*-

#A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

#For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

#For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

#k=2: 4 = 2 × 2 = 2 + 2
#k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
#k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
#k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
#k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

#Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once in the sum.

#In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

#What is the sum of all the minimal product-sum numbers for 2≤k≤12000?

#Answer:
	#7587457

from time import time; t=time()
from mathplus import isqrt, reduce, op

M=12000

n = M
D=[2*i for i in range(n+1)]

def mul(l):
    return reduce(op.mul, l, 1)

p=[[i] for i in range(2, isqrt(2*n)+1)]
while p:
    q = []
    for l in p:
        m, s = mul(l), sum(l)-len(l)
        r = l[-1]
        mr = m*r
        while mr <= 2*n:
            nn = mr-s-r+1
            if nn > n: break
            q.append(l+[r])
            D[nn] = min(D[nn], mr)
            r += 1
            mr += m
    p = q

print(sum(set(D[2:])))#, time()-t
