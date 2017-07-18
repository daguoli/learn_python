#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 输入三个整数x,y,z，请把这三个数由小到大输出。

i = int(input("please input integer i："))
j = int(input("please input integer j："))
k = int(input("please input integer k："))

list = [ i, j , k ]
new_list = sorted(list)
print "顺序排列后为：", new_list  

