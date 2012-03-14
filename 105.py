#!/usr/bin/python
# -*- coding: utf-8 -*-

#Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:

   #1. S(B) ≠ S(C); that is, sums of subsets cannot be equal.
   #2. If B contains more elements than C then S(B) > S(C).

#For example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special sum set because 65 + 87 + 88 = 75 + 81 + 84, whereas {157, 150, 164, 119, 79, 159, 161, 139, 158} satisfies both rules for all possible subset pair combinations and S(A) = 1286.

#Using sets.txt (right click and "Save Link/Target As..."), a 4K text file with one-hundred sets containing seven to twelve elements (the two examples given above are the first two sets in the file), identify all the special sum sets, A1, A2, ..., Ak, and find the value of S(A1) + S(A2) + ... + S(Ak).

#NOTE: This problem is related to problems 103 and 106.

#Answer:
	#73702

from time import time; t=time()
from mathplus import product

DATA = [[int(i) for i in s.split(',')] for s in open('105-sets.txt').read().splitlines()]

s = 0
for data in DATA:
    l = sorted(data)
    lenl = len(l)
    flag = False
    for i in range(lenl-1):
        if l[i] == l[i+1]:
            flag = True
            break
    if flag: continue
    for k in range(1, lenl):
        if sum(l[-k:]) >= sum(l[:k+1]): break
    else:
        ss = set()
        for k in product(*([(0,1)]*lenl)):
            ss.add(sum(k[i]*l[i] for i in range(lenl)))
        if len(ss) == 2**lenl: s += sum(l)

print(s)#, time()-t
