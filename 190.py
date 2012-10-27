#!/usr/bin/python
# -*- coding: utf-8 -*-

# Let Sm = (x1, x2, ... , xm) be the m-tuple of positive real numbers with x1 + x2 + ... + xm = m for which Pm = x1 * x22 * ... * xmm is maximised.

# For example, it can be verified that [P10] = 4112 ([ ] is the integer part function).

# Find Σ[Pm] for 2 ≤ m ≤ 15.

#Answer:
    #371048281

from mathplus import timer


@timer
def pe(m):
    ret = (2./(m+1))**(m*(m+1)//2)
    for i in range(2, m+1):
        ret *= i**i
    return int(ret)

print(sum(pe(i) for i in range(2, 16)))
