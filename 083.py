#!/usr/bin/python
# -*- coding: utf-8 -*-

#NOTE: This problem is a significantly more challenging version of Problem 81.

#In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297.

#131 673 234 103 18 
#201 96 342 965 150 
#630 803 746 422 111 
#537 699 497 121 956 
#805 732 524 37 331 

#Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by moving left, right, up, and down.

#Answer:
	#425185

from time import time; t=time()

DATA = [list(map(int, l.split(','))) for l in open('083-matrix.txt').read().splitlines()]
SIZE = 80

minpath = [[0]*SIZE for i in range(SIZE)]
minpath[0][0] = DATA[0][0]
for i in range(1, SIZE):
    minpath[i][0] = minpath[i-1][0] + DATA[i][0]
    minpath[0][i] = minpath[0][i-1] + DATA[0][i]
for i in range(1, SIZE):
    for j in range(1, SIZE):
        minpath[i][j] = min(minpath[i-1][j], minpath[i][j-1])+DATA[i][j]

flag = True
c = 0
while flag:
    flag = False
    c += 1
    for i in range(SIZE):
        for j in range(SIZE):
            if i == 0 and j == 0: continue
            if i == 0:
                s = minpath[1][j]
            elif i == SIZE-1:
                s = minpath[SIZE-2][j]
            else:
                s = min(minpath[i-1][j], minpath[i+1][j])
            if j == 0:
                s = min(s, minpath[i][1])
            elif j == SIZE-1:
                s = min(s, minpath[i][SIZE-2])
            else:
                s = min(s, minpath[i][j-1], minpath[i][j+1])
            s += DATA[i][j]
            if s < minpath[i][j]:
                minpath[i][j] = s
                flag = True
print(minpath[SIZE-1][SIZE-1])#, time()-t, c
