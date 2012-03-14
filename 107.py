#!/usr/bin/python
# -*- coding: utf-8 -*-

#The following undirected network consists of seven vertices and twelve edges with a total weight of 243.

#The same network can be represented by the matrix below.
    	#A	B	C	D	E	F	G
#A	-	16	12	21	-	-	-
#B	16	-	-	17	20	-	-
#C	12	-	-	28	-	31	-
#D	21	17	28	-	18	19	23
#E	-	20	-	18	-	-	11
#F	-	-	31	19	-	-	27
#G	-	-	-	23	11	27	-

#However, it is possible to optimise the network by removing some edges and still ensure that all points on the network remain connected. The network which achieves the maximum saving is shown below. It has a weight of 93, representing a saving of 243 − 93 = 150 from the original network.

#Using network.txt (right click and 'Save Link/Target As...'), a 6K text file containing a network with forty vertices, and given in matrix form, find the maximum saving which can be achieved by removing redundant edges whilst ensuring that the network remains connected.

#Answer:
	#259679

from time import time; t=time()

MAX = 65535
network = [list(map(lambda x: int(x) if x != '-' else MAX, i.split(','))) 
    for i in open('107-network.txt').read().splitlines()]
size = 40
edges = [(network[i][j], i, j) for i in range(size) for j in range(size) if network[i][j] != MAX]
assert len(network) == size and len(network[0]) == size
old_sum = sum(e[0] for e in edges)//2

v = set()
e = set()
s = 0
v.add(0)
while len(v) < size:
    min_e = min(e for e in edges if e[1] in v and e[2] not in v)
    v.add(min_e[2])
    e.add(min_e)
    s += min_e[0]

print(old_sum-s)#, time()-t
