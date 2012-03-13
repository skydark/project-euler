#!/usr/bin/python
# -*- coding: utf-8 -*-

#In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

	
#131	673	234	103	18
#201	96	342	965	150
#630	803	746	422	111
#537	699	497	121	956
#805	732	524	37	331
	

#Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.

#Answer:
	#427337

#from time import time; t=time()

DATA = [list(map(int, l.split(','))) for l in open('081-matrix.txt').read().splitlines()]
SIZE = 80

minpath = [[0]*SIZE for i in range(SIZE)]
minpath[0][0] = DATA[0][0]
for i in range(1, SIZE):
    minpath[0][i] = minpath[0][i-1] + DATA[0][i]
    minpath[i][0] = minpath[i-1][0] + DATA[0][i]
for i in range(1, SIZE):
    for j in range(1, SIZE):
        minpath[i][j] = min(minpath[i-1][j], minpath[i][j-1]) + DATA[i][j]
print(minpath[SIZE-1][SIZE-1])#, time()-t

