#!/usr/bin/python
# -*- coding: utf-8 -*-

#The first two consecutive numbers to have two distinct prime factors are:

#14 = 2 × 7
#15 = 3 × 5

#The first three consecutive numbers to have three distinct prime factors are:

#644 = 2² × 7 × 23
#645 = 3 × 5 × 43
#646 = 2 × 17 × 19.

#Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?

#Answer:
	#134043

from time import time; t=time()

T=S=4

M = 150000

faccnt = [0]*M
nrange = list(range(M))

for i in range(2, M):
    if nrange[i] != 1:
        for j in range(i, M, i):
            nrange[j] = nrange[j//i]
            faccnt[j] += 1

cnt = 0
for i in range(0, M-3):
    if faccnt[i] == S:
        cnt += 1
        if cnt == T:
            print(i-T+1)#, time()-t
            break
    else:
        cnt = 0
