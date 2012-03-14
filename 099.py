#!/usr/bin/python
# -*- coding: utf-8 -*-

#Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.

#However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.

#Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

#NOTE: The first two lines in the file represent the numbers in the example given above.

#Answer:
	#709

from time import time; t=time()
from math import log

DATA = [map(int, l.split(',')) for l in open('099-base_exp.txt').read().split()]

x = [(log(x)*y, i) for i, (x, y) in enumerate(DATA)]

print(max(x)[1]+1)#, time()-t
