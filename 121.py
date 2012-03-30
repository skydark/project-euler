#!/usr/bin/python
# -*- coding: utf-8 -*-

#A bag contains one red disc and one blue disc. In a game of chance a player takes a disc at random and its colour is noted. After each turn the disc is returned to the bag, an extra red disc is added, and another disc is taken at random.

#The player pays £1 to play and wins if they have taken more blue discs than red discs at the end of the game.

#If the game is played for four turns, the probability of a player winning is exactly 11/120, and so the maximum prize fund the banker should allocate for winning in this game would be £10 before they would expect to incur a loss. Note that any payout will be a whole number of pounds and also includes the original £1 paid to play the game, so in the example given the player actually wins £9.

#Find the maximum prize fund that should be allocated to a single game in which fifteen turns are played.

#Answer:
	#2269

from time import time; t=time()
from mathplus import factorial, product, reduce, op

N = 15
s = 0
for l in product(*([(0, 1)]*N)):
    if sum(l) * 2 > N:
        s += reduce(op.mul,
                ((i + 1) if v == 0 else 1 for i, v in enumerate(l)),
                1)

print(factorial(N+1)//s)#, time()-t)
