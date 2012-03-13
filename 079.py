#!/usr/bin/python
# -*- coding: utf-8 -*-

#A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

#The text file, keylog.txt, contains fifty successful login attempts.

#Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.

#Answer:
	#73162890

from time import time; t=time()

DATA = open("079-keylog.txt").read().splitlines()

def accept(s, r):
    offset = 0
    for c in r:
        offset = s.find(c, offset)+1
        if offset == 0: return False
    return True

n = 0
# according to keylog data, we can use some trick
n = 70000000
while True:
    #n += 1
    n += 10	# trick
    s = str(n)
    if '4' in s or '5' in s or s[0] != '7': continue	# trick
    for r in DATA:
        if not accept(s, r): break
    else:
        print(n)#, time()-t
        break
