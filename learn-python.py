#!/usr/bin/python
#coding=utf-8

# 函数
print "\n\n---function-----"
def printinfo( name, age ):
   "打印任何传入的字符串"
   print "Name: ", name;
   print "Age:", age;
   return;
 
#调用printinfo函数
printinfo( "miki", "50" );


'''
# 时间
import time 
print "\n\n----time----"
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
'''


#print "Hello, World!";print "你好，世界！";

'''
if True:
    print "True";
else:
    print "False";
'''

# raw_input("\n\nPress the enter key to exit.")

'''
# 字符串
print "\n\n----string----"
str = "Hello World!"
print str
print str[0]
print str[2:]
print str * 2
print str + "TEST"
'''

'''
# 数组
print "\n\n----list----"
list = [ 'sun', 'join', 123, 70.2 ]
otherlist = [ '222', 'happy' ]
print list
print list[1:3]
print list[2:]
print otherlist * 2
print otherlist + list
'''

'''
# 字典
print "\n\n----dict----"
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name':'join','age':'17','code':'55038'}
print dict
print tinydict
print tinydict.keys()
print tinydict.values()
'''

