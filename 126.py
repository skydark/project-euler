#!/usr/bin/python
# -*- coding: utf-8 -*-

#The minimum number of cubes to cover every visible face on a cuboid measuring 3 x 2 x 1 is twenty-two.

#If we then add a second layer to this solid it would require forty-six cubes to cover every visible face, the third layer would require seventy-eight cubes, and the fourth layer would require one-hundred and eighteen cubes to cover every visible face.

#However, the first layer on a cuboid measuring 5 x 1 x 1 also requires twenty-two cubes; similarly the first layer on cuboids measuring 5 x 3 x 1, 7 x 2 x 1, and 11 x 1 x 1 all contain forty-six cubes.

#We shall define C(n) to represent the number of cuboids that contain n cubes in one of its layers. So C(22) = 2, C(46) = 4, C(78) = 5, and C(118) = 8.

#It turns out that 154 is the least value of n for which C(n) = 10.

#Find the least value of n for which C(n) = 1000.

#Answer:
	#18522

from time import time; t=time()
from mathplus import range

# 4(k-1)(a+b+c)+2(ab+bc+ca)+8(k-1)(k-2)/2

N = 1000
M = 20000

cache = [0] * M
for a in range(1, M):
    for b in range(1, a+1):
        ab = a * b
        if ab * 2 >= M: break
        a_b = a + b
        for c in range(1, b+1):
            s =(a_b * c + ab) * 2
            if s >= M: break
            cache[s] += 1
            ss = 4 * (a_b + c)
            for k in range(0, M, 8):
                s += ss + k
                if s >= M: break
                cache[s] += 1

for i, v in enumerate(cache):
    if v == N:
        break

print(i, time()-t)
