#!/usr/bin/python
# -*- coding: utf-8 -*-

# A 4x4 grid is filled with digits d, 0 \leq d\leq 9.

# It can be seen that in the grid

# 6 3 3 0
# 5 0 4 3
# 0 7 1 4
# 1 2 4 5

# the sum of each row and each column has the value 12. Moreover the sum of each diagonal is also 12.

# In how many ways can you fill a 4x4 grid with the digits d, 0 \leq d \leq 9 so that each row, each column, and both diagonals have the same sum?

#Answer:
	#7130034

from time import time; t=time()

def pe166():
    pool = [[] for i in range(37)]
    for i1 in range(10):
        for i2 in range(10):
            for i3 in range(10):
                for i4 in range(10):
                    l = (i1, i2, i3, i4)
                    pool[sum(l)].append(l)
    count = 0
    for s, ls in enumerate(pool):
        #print(s)
        dd = {}
        lls = len(ls)
        for l1 in ls:
            for l2 in ls:
                key = (l1[0]+l2[0], l1[1]+l2[1], l1[2]+l2[2], l1[3]+l2[3], l1[0]+l2[1], l1[3]+l2[2])
                dd.setdefault(key, 0)
                dd[key] += 1
        for (s1, s2, s3, s4, s5, s6), c in dd.items():
            key = (s-s1, s-s2, s-s3, s-s4, s-s6, s-s5)
            count += c * dd.get(key, 0)
    return count

print(pe166(), time()-t)
