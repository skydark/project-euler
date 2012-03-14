#!/usr/bin/python
# -*- coding: utf-8 -*-

#Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

#Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

#We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

#As n increases, the proportion of bouncy numbers below n increases such that there are only 12951 numbers below one-million that are not bouncy and only 277032 non-bouncy numbers below 1010.

#How many numbers below a googol (10100) are not bouncy?

#Answer:
	#51161058134250

from time import time; t=time()
from mathplus import memorize

L = 100
@memorize
def f(rang, length):
   if length == 1 or rang == 1: return rang
   return sum(f(i, length-1) for i in range(1, rang+1))

print(f(10, L)+sum(f(10, i) for i in range(1, L+1))-10*L-1)#, time()-t
