#!/usr/bin/python
# -*- coding: utf-8 -*-

#Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

#Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

#We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

#Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

#Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

#Find the least number for which the proportion of bouncy numbers is exactly 99%.

#Answer:
	#1587000

from time import time; t=time()

def type_of_num(n):
    # ret: 0 - bouncy 1-increasing 2- decreasing 3-both
    ret = 0
    s = str(n)
    ss = ''.join(sorted(s))
    if ss == s: ret += 1
    if ss[::-1] == s: ret += 2
    return ret

n = 1
s = 0
while True:
    if s == n*99: break
    ret = type_of_num(n)
    if ret == 0:
        s += 100
    elif ret == 1:
        m = n % 10
        s += 100 - (10-m)*(11-m)//2
    elif ret == 2:
        m = n % 10
        s += 100 - (m+1)*(m+2)//2
    else:#ret == 3
        m = n % 10
        s += 100 - (10-m)*(11-m)//2 - (m+1)*(m+2)//2 + 1
    n += 1
print((n-1)*100)#, time()-t
