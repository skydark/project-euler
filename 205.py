#!/usr/bin/python
# -*- coding: utf-8 -*-

#Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
#Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

#Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.

#What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg

#Answer:
	#0.5731441

from time import time; t=time()

def dice(size, n):
    old_flags = [1]*size
    for k in range(2, n+1):
        flags = [0] *(k*(size-1)+1)
        for i, j in enumerate(old_flags):
            for l in range(i, i+size):
                flags[l] += j
        old_flags = flags
    return [0]*n+flags

both_size = 37
pyr = dice(4, 9)
cub = dice(6, 6)
cub = [sum(cub[:i]) for i in range(both_size)]
prob = sum(pyr[i]*cub[i] for i in range(both_size))
prob = prob*1. /((4**9)*(6**6))
print(round(prob*1e7)/1e7)#, time()-t
