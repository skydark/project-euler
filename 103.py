#!/usr/bin/python
# -*- coding: utf-8 -*-

#Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:

#    S(B) ≠ S(C); that is, sums of subsets cannot be equal.
#    If B contains more elements than C then S(B) > S(C).

#If S(A) is minimised for a given n, we shall call it an optimum special sum set. The first five optimum special sum sets are given below.

#n = 1: {1}
#n = 2: {1, 2}
#n = 3: {2, 3, 4}
#n = 4: {3, 5, 6, 7}
#n = 5: {6, 9, 11, 12, 13}

#It seems that for a given optimum set, A = {a1, a2, ... , an}, the next optimum set is of the form B = {b, a1+b, a2+b, ... ,an+b}, where b is the "middle" element on the previous row.

#By applying this "rule" we would expect the optimum set for n = 6 to be A = {11, 17, 20, 22, 23, 24}, with S(A) = 117. However, this is not the optimum set, as we have merely applied an algorithm to provide a near optimum set. The optimum set for n = 6 is A = {11, 18, 19, 20, 22, 25}, with S(A) = 115 and corresponding set string: 111819202225.

#Given that A is an optimum special sum set for n = 7, find its set string.

#NOTE: This problem is related to problems 105 and 106.

#Answer:
	#20313839404245

from time import time; t=time()
from mathplus import Cnr, combinations

NN = N = 7

l, h = 17, 50
#l, h = 11, 26

min_s = h * N
min_k = []
cache = {}
for i in range(l, h):
    cache[(i,)] = True
for N in range(2, NN+1):
    for k in combinations(range(l, h - NN + N), N):
        kk = sorted(k)
        if tuple(kk) in cache: continue
        if tuple(kk[:N-1]) not in cache: continue
        if N == NN:
            s = sum(kk)
            if s >= min_s: continue
        for i in range(1, (N+1)//2):
            if sum(kk[-i:]) >= sum(kk[:i+1]): break
        else:
            for r in range(2, N-1):
                ss = set()
                for j in combinations(kk, r):
                    ss.add(sum(j))
                if len(ss) != Cnr(N, r): break
            else:
                if N == NN:
                    min_s = s
                    min_k = kk
                else:
                    for i in range(0, h - NN + N - kk[-1]):
                        cache[tuple(k + i for k in kk)] = True

print(''.join(str(i) for i in min_k))#, time()-t
