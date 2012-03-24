#!/usr/bin/python
# -*- coding: utf-8 -*-

# By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 362. What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 962. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, neither may a different letter have the same digital value as another letter.

# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).

# What is the largest square number formed by any member of such a pair?

# NOTE: All anagrams formed must be contained in the given text file.

#Answer:
	#18769

from time import time; t=time()
from mathplus import combinations, permutations, reduce, isqrt

DATA = [i[1:-1] for i in open('098-words.txt').read().split(',')]

def get_alphas(s):
    return tuple(s.count(chr(c)) for c in range(ord('A'), ord('Z')+1))

def alpha_to_num(s):
    return [ ord(c)-ord('A') for c in s ]

data = [(get_alphas(s), alpha_to_num(s)) for s in DATA]
data = sorted(data)

d = {}
for k, v in data:
    d.setdefault(k, [])
    d[k].append(v)

dd = {}
for k, v in d.items():
    if len(v) > 1:
        dd[k] = v
        #if len(v) > 2: print(v)

max_value = 0
cnt = 0
for k, v in dd.items():
    cnt += 1
    #print(cnt)
    active_k = [i for i in range(26) if k[i] > 0]
    len_active_k = len(active_k)
    if len_active_k > 10: continue
    full_f = [0]*26
    def test(s):
        if full_f[s[0]] == 0: return 0
        c = full_f[s[-1]]
        if c in (0, 2, 3, 7, 8): return 0
        d = full_f[s[-2]]
        if c == 5 and d != 2: return 0
        if c == 6 and d % 2 == 0: return 0
        if d % 2 == 1: return 0
        n = reduce(lambda x,y: x*10+y, (full_f[c] for c in s))
        return n if isqrt(n)**2 == n else 0
    def test_xy(x, y):
        global max_value
        for f in permutations(range(10), len_active_k):
            for j in range(len_active_k):
                full_f[active_k[j]] = f[j]
            if test(x) > 0 and test(y) > 0:
                max_value = max(max_value, test(x), test(y))
                #print(v, max_value)
    if len(v) == 2:
        test_xy(v[0], v[1])
    else:
        for x, y in combinations(v, 2):
            test_xy(x, y)

print(max_value)#, time()-t)
