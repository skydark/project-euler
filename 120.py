#!/usr/bin/python
# -*- coding: utf-8 -*-

#Let r be the remainder when (a−1)n + (a+1)n is divided by a2.

#For example, if a = 7 and n = 3, then r = 42: 63 + 83 = 728 ≡ 42 mod 49. And as n varies, so too will r, but for a = 7 it turns out that rmax = 42.

#For 3 ≤ a ≤ 1000, find ∑ rmax.

#Answer:
	#333082500

from time import time; t=time()

M = 1000

print(sum(n*(n-2+n%2) for n in range(3, M+1)))#, time()-t
