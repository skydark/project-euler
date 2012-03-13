#!/usr/bin/python2
# -*- coding: utf-8 -*-

#The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

#We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

#There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

#If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

#Answer:
	#100  

from mathplus import Fraction

s = 1
for i1 in range(1, 9):
    for i2 in range(i1+1, 10):
        i = i1*i2
        for j2 in range(i1+1, 10):
            if i1*(10*i2+j2) == j2*(10*i1+i2):
                s *= Fraction(i1, j2)
print(s.denominator)
