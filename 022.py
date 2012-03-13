#!/usr/bin/python
# -*- coding: utf-8 -*-

#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938  53 = 49714.

#What is the total of all the name scores in the file?

#Answer:
	#871198282

names = sorted(map(lambda s: s[1:-1], open('022-names.txt').read().split(',')))

scores = [(i+1) * sum(ord(c)-64 for c in name) for i, name in enumerate(names)]

print(sum(scores))
