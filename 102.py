#!/usr/bin/python
# -*- coding: utf-8 -*-

#Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

#Consider the following two triangles:

#A(-340,495), B(-153,-910), C(835,-947)

#X(-175,41), Y(-421,-714), Z(574,-645)

#It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

#Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.

#NOTE: The first two examples in the file represent the triangles in the example given above.

#Answer:
	#228

from time import time; t=time()

DATA = [[int(i) for i in l.split(',')] for l in open('102-triangles.txt').read().splitlines()]

def get_line(p, q):
    #if p[1] < q[1]: p, q = q, p
    return p[1]-q[1], q[0]-p[0], p[0]*q[1]-p[1]*q[0]

def get_pos(line, p):
    r = line[0]*p[0]+line[1]*p[1]+line[2]
    if r == 0: return 0
    return 1 if r > 0 else -1

def same_side(line, p, q):
    return get_pos(line, p) == get_pos(line, q)

s = 0
Z = (0, 0)
for data in DATA:
    A = data[0], data[1]
    B = data[2], data[3]
    C = data[4], data[5]
    lines = [get_line(A, B), get_line(B, C), get_line(C, A)]
    if same_side(get_line(A, B), C, Z) and \
        same_side(get_line(B, C), A, Z) and \
        same_side(get_line(A, C), B, Z):
        s += 1

print(s)#, time()-t
