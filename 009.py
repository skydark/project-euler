#!/usr/bin/python
# -*- coding: utf-8 -*-

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2

#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#Answer:
	#31875000

# a+b+c = s, a^2+b^2 = c^2 = (s-a-b)^2 = s^2-2as-2bs+2ab+a^2+b^2
# => (s-a)(s-b)=s*s/2

s = 1000

assert s % 2 == 0
t = s*s//2
for a in range(1, s-int(t**.5)):
    if t % (s-a) == 0:
        b = s - t//(s-a)
        c = s - a - b
        if c > 0:
            print(a*b*c)
            break
