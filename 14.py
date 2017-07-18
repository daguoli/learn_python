#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

i = int(input("please input a numben:"))
primeFactor = []
while i > 1:
	for j in range(2,i+1):
		#print "\n-----i=", i, ";j=", j, "-----"
		if (i % j == 0):
			#print j, "是质因数"
			primeFactor.append(j)
			i = i / j
			break
		else:
			j = j + 1
print "质因数为：", primeFactor
