#!/usr/bin/python
# -*- coding: utf-8 -*-

#The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

#Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

#Answer:
    #9110846700  

from mathplus import pow_mod

M = 1000
L = 10

p = 10**L
print(sum(pow_mod(i, i, p) for i in range(1, M)) % p)
