#!/usr/bin/python
# -*- coding: utf-8 -*-

#NOTE: This problem is a more challenging version of Problem 81.

#The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

	
#131	673	234	103	18
#201	96	342	965	150
#630	803	746	422	111
#537	699	497	121	956
#805	732	524	37	331
	

#Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the left column to the right column.

#Answer:
	#260324

from time import time; t=time()

DATA = [list(map(int, l.split(','))) for l in open('082-matrix.txt').read().splitlines()]
SIZE = 80

minpath = [[0]*SIZE for i in range(SIZE)]
for i in range(SIZE):
    minpath[i][0] = DATA[i][0]
for j in range(1, SIZE):
    for i in range(SIZE):
        minpath[i][j] = minpath[i][j-1] + DATA[i][j]
    flag = True
    while flag:
        flag = False
        for i in range(SIZE):
            if i == 0:
                s = minpath[1][j]+DATA[i][j]
            elif i == SIZE-1:
                s = minpath[SIZE-2][j]+DATA[i][j]
            else:
                s = min(minpath[i-1][j], minpath[i+1][j])+DATA[i][j]
            if s < minpath[i][j]:
                minpath[i][j] = s
                flag = True
print(min(minpath[i][-1] for i in range(SIZE)))#, time()-t
