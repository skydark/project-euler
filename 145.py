#!/usr/bin/python
# -*- coding: utf-8 -*-

#Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

#There are 120 reversible numbers below one-thousand.

#How many reversible numbers are there below one-billion (109)?

#Answer:
	#608720

from time import time; t=time()

L = 9
cnt = 0
def find(n):
    if n % 2 == 1:
        if (n+1) % 4 == 0:
            s = 20*500**((n-3)//4)*5
        else: 
            s = 0
    else:
        s = 20 * 30**(n//2-1)
    return s
for i in range(2, L+1):
    cnt += find(i)
print(cnt)#, time()-t
