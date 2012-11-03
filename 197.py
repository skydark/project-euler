#!/usr/bin/python
# -*- coding: utf-8 -*-

# Given is the function f(x) = ⌊230.403243784-x2⌋ × 10-9 ( ⌊ ⌋ is the floor-function),
# the sequence un is defined by u0 = -1 and un+1 = f(un).

# Find un + un+1 for n = 1012.
# Give your answer with 9 digits after the decimal point.

#Answer:
    #1.710637717

from mathplus import timer, floor


@timer
def pe197():
    u = 0
    uu = 0
    s = -1
    v = -1
    epsilon = 10**(-9)
    for n in range(10**12):
        uu, u, v = u, v, floor(2**(30.403243784-v*v))*epsilon
        if uu == v:
            break
    return u + v

print(pe197())
