#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

a = int (input("please input number:"))
n = int (input("please input the count"))

sum=0
Tn=0

for i in range(1,n+1):
        x = a * (10 ** (i-1))
	Tn = Tn + x
        print "T%s" % i, ":", Tn
        sum = sum + Tn
print "sum is:", sum	

