#!/usr/bin/python
# -*- coding: utf-8 -*-

# The sequence 1, 1, 1, 3, 5, 9, 17, 31, 57, 105, 193, 355, 653, 1201 ...
# is defined by T1 = T2 = T3 = 1 and Tn = Tn-1 + Tn-2 + Tn-3.

# It can be shown that 27 does not divide any terms of this sequence.
# In fact, 27 is the first odd number with this property.

# Find the 124th odd number that does not divide any terms of the above sequence.

#Answer:
    #2009

from mathplus import timer

C = 124


@timer
def pe225(count):
    def test(n):
        pool = set()
        t1, t2, t3 = 1, 1, 1
        while t1 * t2 * t3 != 0:
            if (t1, t2, t3) in pool:
                return True
            t4 = (t1 + t2 + t3) % n
            t5 = (t1 + t2 * 2 + t3 * 2) % n
            t6 = (t1 * 2 + t2 * 3 + t3 * 4) % n
            pool.add((t1, t2, t3))
            pool.add((t2, t3, t4))
            pool.add((t3, t4, t5))
            t1, t2, t3 = t4, t5, t6
        return False
    n = 1
    while count > 0:
        n += 2
        while not test(n):
            n += 2
        count -= 1
    return n

print(pe225(C))
