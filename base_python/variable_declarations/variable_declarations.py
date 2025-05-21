#!/usr/bin/env python3

__author__ = 'zhangweiwei'

import keyword

#注释的两种方式
"""
你好啊
"""
#hello world


#变量的应用
a = 10
b = 20
c = "zhangweiweiwei"
print(a + b)
print("hello world")
print(c)
e,f,g=10,11,12
print(e,f,g)
#变量值交换
a,b=b,a
print(a,b)

#关键字
print(keyword.kwlist)
print(keyword.softkwlist)
print(keyword.iskeyword("None"))





