#!/usr/bin/python
# -*- coding: utf-8 -*-

# Let (a, b, c) represent the three sides of a right angle triangle with integral length sides. It is possible to place four such triangles together to form a square with length c.

# For example, (3, 4, 5) triangles can be placed together to form a 5 by 5 square with a 1 by 1 hole in the middle and it can be seen that the 5 by 5 square can be tiled with twenty-five 1 by 1 squares.

# However, if (5, 12, 13) triangles were used then the hole would measure 7 by 7 and these could not be used to tile the 13 by 13 square.

# Given that the perimeter of the right triangle is less than one-hundred million, how many Pythagorean triangles would allow such a tiling to take place?

#Answer:
    #10057761

from mathplus import timer, isqrt, gcd

M =  100000000


@timer
def pe(M):
    s = 0
    for m in range(2, isqrt(M/2)):
        mm = (M-1) // (2*m)
        m2 = m * m
        start = 1 if m % 2 == 0 else 2
        for n in range(start, min(mm-m+1, m), 2):
            if gcd(m, n) != 1:
                continue
            n2 = n * n
            if (m2+n2) % (m2-n2-2*m*n) != 0:
                continue
            s += mm // (m+n)
    return s

print(pe(M))
