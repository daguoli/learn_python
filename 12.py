#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 题目：判断101-200之间有多少个素数，并输出所有素数。
# 判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 　

from math import sqrt


count=0

# i:需要判断的数字；j：除数
for i in range(101,201):
	flag=1 #默认为素数
	for k in range(2,i):
		if i%k == 0:
                        flag=0
			break
	if flag==1:
		print i, "是素数"
		count = count + 1
        flag=1
print "total count is:", count
