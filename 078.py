#!/usr/bin/python
# -*- coding: utf-8 -*-

#Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can separated into piles in exactly seven different ways, so p(5)=7.
#OOOOO
#OOOO   O
#OOO   OO
#OOO   O   O
#OO   OO   O
#OO   O   O   O
#O   O   O   O   O

#Find the least value of n for which p(n) is divisible by one million.

#Answer:
	#55374

# http://zh.wikipedia.org/zh-cn/%E6%95%B4%E6%95%B8%E5%88%86%E6%8B%86

from time import time; t=time()

M = 1000000
Q = 100
STEP = 50

q = sum([[i*(3*i-1)//2, i*(3*i+1)//2] for i in range(1, Q)], [0])
pool = [1, 1, 2]
n = 3
while True:
    s, j = 0, 1
    while q[j] <= n:
        if (j-1)%4 < 2:
            s += pool[n-q[j]]
        else:
            s -= pool[n-q[j]]
        j += 1
        if j == Q:
            q += sum([[i*(3*i-1)//2, i*(3*i+1)//2] for i in range(Q, Q+STEP)], [])
            Q += STEP
    #pool[n] = s % M
    pool.append(s%M)
    if pool[n] == 0: break
    n += 1

print(n)#, time()-t
