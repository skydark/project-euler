#!/usr/bin/python
# -*- coding: utf-8 -*-

#A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

#For example,

#44 → 32 → 13 → 10 → 1 → 1
#85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

#Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

#How many starting numbers below ten million will arrive at 89?

#Answer:
	#8581146

from time import time; t=time()
#import psyco; psyco.full()

M = 10**7
data = [0]*M
for i in range(10):
    data[i] = i*i
for i in range(10, M):
    data[i] = data[i//10]+(i%10)**2
#flags: 
# 0: not decided
# 1: deciding
# 2: ->89
# 3: not -> 89
pool = [0]*M
pool[89] = 2
#print time()-t

def decide(n):
    flag = pool[n]
    if flag == 0:
        pool[n] = 1
        pool[n] = decide(data[n])
        return pool[n]
    if flag == 1: # circle found
        return 3
    return flag

s = 0
for n in range(M):
    if decide(n) == 2: s += 1
print(s)#, time()-t
