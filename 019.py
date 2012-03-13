#!/usr/bin/python
# -*- coding: utf-8 -*-

#You are given the following information, but you may prefer to do some research for yourself.

    #* 1 Jan 1900 was a Monday.
    #* Thirty days has September,
      #April, June and November.
      #All the rest have thirty-one,
      #Saving February alone,
      #Which has twenty-eight, rain or shine.
      #And on leap years, twenty-nine.
    #* A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

#Answer:
	#171

from time import time; t=time()

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

cnt = 0
day = (1+366) % 7
for year in range(1901, 2001):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) :
        months[1] = 29
    else:
        months[1] = 28
    for month in months:
        if day == 0: cnt += 1
        day = (day+month) % 7

print(cnt)#, time()-t
