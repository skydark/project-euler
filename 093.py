#!/usr/bin/python
# -*- coding: utf-8 -*-

#By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic operations (+, −, *, /) and brackets/parentheses, it is possible to form different positive integer targets.

#For example,

#8 = (4 * (1 + 3)) / 2
#14 = 4 * (3 + 1 / 2)
#19 = 4 * (2 + 3) − 1
#36 = 3 * 4 * (2 + 1)

#Note that concatenations of the digits, like 12 + 34, are not allowed.

#Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

#Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 1 to n, can be obtained, giving your answer as a string: abcd.

#Answer:
	#1258

from __future__ import division

from time import time; t=time()
from mathplus import permutations, combinations, memorize

s = 0
abcd = []

def get_ret2(a, b):
    r = [a+b, a-b, a*b, b-a]
    if a != 0: r.append(b/a)
    if b != 0: r.append(a/b)
    return r

@memorize
def get_ret3(abc):
    ss = set()
    for i in permutations(abc):
        a, b, c = i[0], i[1], i[2]
        for r in get_ret2(a, b):
            ss.add(tuple(sorted((r, c))))
    return set(r for ab in ss for r in get_ret2(*ab))

for k in combinations(range(1, 10), 4):
    ss = set()
    for i in permutations(k):
        a, b, c, d = i[0], i[1], i[2], i[3]
        for r in get_ret2(a, b):
            ss.add(tuple(sorted((r, c, d))))
    ret = set(r for abc in ss for r in get_ret3(abc))
    i = 1
    while True:
        if i not in ret: break
        i += 1
    i -= 1
    if i > s:
        s = i
        abcd = sorted(k)


print(''.join(str(i) for i in abcd))#, s, time()-t)
