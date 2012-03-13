#!/usr/bin/python
# -*- coding: utf-8 -*-

#Take the number 192 and multiply it by each of 1, 2, and 3:

    #192 × 1 = 192
    #192 × 2 = 384
    #192 × 3 = 576

#By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

#The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

#Answer:
	#932718654

#from time import time; t=time()

print(932718654)#, time()-t
# 显然最大解的第一位是9,因为它至少是918273645
# n <= 5
# n == 5, 就是918273645
# n == 4, 按位数分割只有2, 2, 2, 3位, 第一位是9时这是不可能的
# n == 3, 按位数分割只有3, 3, 3位，同上
# n == 2, 9abc * 2 = 18def
# 剩余数字是234567
# a只能为234中的一个，因为不能进位
# 若a是4,则d无法选择，故a最大为3,令a为3，d为6或7
# 5只能在def中，由2×2+1或7×2+1得到
# 最后一位只能是2×2=4或6×2=12或7×2=14
# 若d为7,则b×2要进位，b只能为6，最后一位只能为2×2=4,得c=2,9362×2=18724不合要求
# 故取d为6,b×2不进位，f只能为4,b只能为2,c最大为7,9327×2=18654恰为解。
