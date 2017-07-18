#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 题目：输入某年某月某日，判断这一天是这一年的第几天？

year = int (input("请输入年："))
mouth = int (input("请输入月："))
day = int (input("请输入日："))

mouths = [ 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334 ]
if mouth in range ( 1, 13 ):
    sort = mouths[mouth -1] + day

# 闰年的处理
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)) and (mouth > 2):
    sort = sort + 1 

print "这是这一年的第", sort, "天"
    

