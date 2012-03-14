#!/usr/bin/python
# -*- coding: utf-8 -*-

#The radical of n, rad(n), is the product of distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

#If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and sorting on n if the radical values are equal, we get:
#Unsorted

#Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and E(6) = 9.

#If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).

#Answer:
	#21417

from time import time; t=time()
from mathplus import factorization

M = 100000
L = 10000

M += 1
fsieves = [0] * M
fsieves[0] = 0
fsieves[1] = 1

l = 2
s = 1
ss = 1
for n in range(2, M):
    if fsieves[n] > 0: continue
    fsieves[n] = l
    ret = [n]
    for f, k in factorization(n):
        for m in ret[:]:
            while True:
                m *= f
                if m > M: break
                ret.append(m)
                fsieves[m] = l
    ss = s + len(ret)
    if ss >= L: break
    s = ss
    l += 1

ss = L - s
for i in range(M):
    if fsieves[i] == l: ss -= 1
    if ss == 0: break

print(i)#, time()-t
