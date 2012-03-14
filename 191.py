#!/usr/bin/python
# -*- coding: utf-8 -*-

#A particular school offers cash rewards to children with good attendance and punctuality. If they are absent for three consecutive days or late on more than one occasion then they forfeit their prize.

#During an n-day period a trinary string is formed for each child consisting of L's (late), O's (on time), and A's (absent).

#Although there are eighty-one trinary strings for a 4-day period that can be formed, exactly forty-three strings would lead to a prize:

#OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA
#OAOL OAAO OAAL OALO OALA OLOO OLOA OLAO OLAA AOOO
#AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL
#AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA
#LAOO LAOA LAAO

#How many "prize" strings exist over a 30-day period?

#Answer:
	#1918080160

from time import time; t=time()

M = 30

state = [[0]*6 for i in range(M)]
#state: noAnoL, AnoL, AAnoL, noAL, AL, AAL
state[0] = [1, 1, 0, 1, 0, 0]
for i in range(M-1):
    state[i+1][0] = state[i][0]+state[i][1]+state[i][2]
    state[i+1][1] = state[i][0]
    state[i+1][2] = state[i][1]
    state[i+1][3] = state[i][0]+state[i][1]+state[i][2]+state[i][3]+state[i][4]+state[i][5]
    state[i+1][4] = state[i][3]
    state[i+1][5] = state[i][4]

print(sum(state[-1]))#, time()-t
