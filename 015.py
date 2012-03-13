#!/usr/bin/python
# -*- coding: utf-8 -*-

#Starting in the top left corner of a 2×2 grid, there are 6 routes (without backtracking) to the bottom right corner.

#How many routes are there through a 20×20 grid?

#Answer:
	#137846528820

SIZE = 20

grid = [[0]*(SIZE+1) for i in range(SIZE+1)]
grid[0][0] = 1
for i in range(1, SIZE+1):
    l = grid[i]
    l[0] = 1
    for j in range(1, i):
        l[j] = l[j-1] + grid[i-1][j]
    l[i] = 2 * l[i-1]
print(grid[SIZE][SIZE])

# cheat: 40!/20!/20!
