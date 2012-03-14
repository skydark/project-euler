#!/usr/bin/python
# -*- coding: utf-8 -*-

#If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

#The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

#By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.

#Answer:
	#756872327473

from time import time; t=time()

M = 10**12

m, n = 1, 1
while True:
    next_n = m+n
    next_m = next_n+n
    if m*next_m > M:
        m += n
        print((m*m+n*n+1)//2)#, time()-t
        break
    m, n = next_m, next_n
