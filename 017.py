#!/usr/bin/python
# -*- coding: utf-8 -*-

#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

#Answer:
	#21124

from time import time; t=time()

dict_1 = "one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen".split(',')
dict_10 = "twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety".split(",")

def to_english(n):
    # 1 to 999
    a, b = n//100, n % 100
    if a == 0:
        if b < 20:
            ret = dict_1[b-1]
            return len(ret), ret
        c, d = b//10, b%10
        ret = dict_10[c-2]
        if d == 0: return len(ret), ret
        ret += "-" + dict_1[d-1]
        return len(ret)-1, ret
    else:
        ret = dict_1[a-1]
        cnt = len(ret)
        ret += " hundred"
        cnt += 7 
        if b == 0: return cnt, ret
        cnt2, ret2 = to_english(b)
        return cnt+3+cnt2, "%s and %s" %(ret, ret2)

s = sum(to_english(i)[0] for i in range(1, 1000))
s += 11 #"one thousand"
print(s)#, time()-t
