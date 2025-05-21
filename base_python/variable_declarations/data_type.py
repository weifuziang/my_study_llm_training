#!/usr/bin/env python3

__author__ = 'zhangweiwei'
#start====提纲============================================================================================
# 基本数据类型-数值
#   整数int、浮点数float、复数complex、波尔bool
# 字符串
#   str
# 容器类
#   list 列表
#   tuple 元组
#   set 集合
#   dict 字典

# 特殊类型
#   None

# 上述类型
# 不可变的类型：数值、字符串、元组
# 可变类型：列表、集合、字典

#end===提纲=============================================================================================




# ========================================整数===================================
# ===数据比较大，数字可以使用下划线，python3.6之后支持
# num1=1_000_000_000
# print(num1)

# ===isinstance()会认为子类是一种父类类型，type()则不会认为子类是一种父类类型
# num1=10
# num2=True
# print(type(num1) == type(num2)) #返回结果为false; 结论type()则不会认为子类是一种父类类型
# print(isinstance(num2,int)) # 返回结果为true; 结论：bool 是int类型的子类型，即是int类型的一种

# === 小整数池【-5 ， 256】：这些整数提前创建好且不会被垃圾回收，避免了为整数频繁申请和销毁内存空间。不管在程序的什么位置，使用的位于这个范围内的整数都是同一个对象
# 大整数池：一开始大整数池为空，每创建一个大整数就会向池中存储一个；
# 不同的 Python 实现：小整数池的范围和实现细节可能因 Python 的不同实现（如 CPython、Jython、IronPython 等）而有所不同。上述提到的[-5, 256]范围是 CPython 的默认实现。
# num1=30
# num2=20
# 打印地址
# print(id(num1))
# print(id(num2))
#
# num1=300
# num2=300
# print(id(num1))
# print(id(num2))

# ========================================浮点数===================================
# 在任何的变成语言中，浮点数都存在丢失精度的情况
# num1 = 0.1
# num2 = 0.2
# num3 = num1 + num2
# print(num3)
# print(type(num3))

# 为了解决浮点数精度丢失情况，可以借用python的其他模块提供的功能
from decimal import Decimal

# num1 = Decimal('0.1')
# num2 = Decimal('0.2')
# num3 = num1 + num2
# print(num3)
# print(type(num3))

# 其他形式
# mum4 = 3.1e7
# num5 = 3.1e7
# num6 = mum4 + num5
# print(num6)
# print(type(num6))

# ========================================布尔类型===================================
# #bool 是int类型
# num1 = True
# num2 = False
# print(type(num1)),type(num2)
#
# #Python3中，bool 是 int 的子类，True 和 False 可以和数字相加。
# #True==1、False==0 会返回 True
# print(num1 + 10)
#
# # == 比较运算符号，判断==左右两边的值是否相等
# print(num1 == 1)
# print(num1 == 2)
#
# # is 用于比较两个对象的身份，即他们在内存中是否是同一个对象，是否在内存中是不是同一个位置
# print(num1 is 1)
# print(num2 is 0)

# ====================================字符串======================================================
#
# str1="he'll'o"
# print(str1)
# str2="hello\"world"
# print(str2)
# #续行符
# str3=("hello \
#       world")
# print(str3)
# str4="hello \\ world"
# print(str4)
# str5="hello\bworld"
# print(str5)
# str6="hello\tworld"
# print(str6)
# #回车，回到行首
# str7="hello\rworld"
# print(str7)
# #pycharm 和 控制台输出不一致，控制台输出wor； pycharm输出为worlo
# str7="hello\rwor"
# print(str7)
# str8="hello\nworld"
# str9="hello\nworld"
# print(id(str8))
# print(id(str9))

#=====================================隐士转换===========================================
# num1=1
# num2=4
# print(num2/num1)
#
# #无法隐士转化
# num1=10
# num2="20"
# print(num1+num2)

#显示转化，通过这种函数转化,默认是10进制，也可以是2进制 16进制 8进制
# num1=int("100",10)
# print(num1)
# print(type(num1))
#
# num2=float("0.5")
# print(num2)

# str1="hello world"
# print(str(str1))
# print(repr(str1))
# print(eval("2+3"))
#
# print(ord('1'))
# print(chr(65))
# print(chr(ord('a')+1))


# ==========================编码和解码========================
#跳过

# ======================input====================
# name = input("请输入一个名字：")
# print(name)


# ============字符串拼接，print============================
# print("hello",end="")
# print("abc")
#
# str1="num1 = %d, num2 = %s "%(10,"dddd")
# print(str1)
#
# str2="dd={}ff={}ee={}".format(1,3,5)
# print(str2)
#
# str3="num1={0},num2={2},num3={1}".format(1,3,5)
# print(str3)
#
# str4="num1={f0},num2={f2},num3={r1}".format(f0=1,f2=3,r1=5)
# print(str4)


#==================三目运算==================
# num1 = 2
# num2 = 3
# max_num = num1 if num1 < num2 else num2
# print(max_num)




# ================序列====================
#序列（sequence）是一种基本且核心的数据结构，它允许我们以有序的方式存储和操作数据。序列可以包含不同类型的元素，并且支持通过索引来访问和修改这些元素
#常见的序列类型包括： 列表（List）、元组（Tuple）、字符串（String）

#序列常见操作： 索引、切片、相加、乘法、检查成员、计算长度、计算最大值和最小值

#================列表 List=====================
#列表是一个可变的、有序的元素集合；
#从头开始，索引以0开始,逐渐递增；从末尾开始，索引以-1开始，逐渐向前递减
list1=[100,200,300,400,500]
# print(list1)
# print(type(list1))
# print(len(list1))
# print(list1[0])
# print(list1[1])
#获取最后一个元素
# print(list1[-1])

#切片
#复制所有元素
# print(list1[:])
# print(list1[2:4])
#每间隔一个取一个值
# print(list1[::2])
# #每间隔两个取一个值
# print(list1[::3])
# print(list1[::4])
# print(list1[::5])
# print(list1[0:3:1])
# print(list1[:2])
# print(list1[2:])
# print(list1[::-1])

#range
# print(range(0,10,1))
# print(range(10,0,1))

#列表中添加元素
# print(list1.insert(3,1000))
# print(list1)
# list1.append(3000)
# print(list1)
# #列表遍历
# for e in list1:
#     print(e)
# #列表相乘
# print(list1 * 2)
#删除列表里的元素
# del list1[0]
# print(list1)

#列表推导式
# squares = [item**2 for item in range(1,10,1) if item % 2 == 0]
# print(squares)
#
# #zip函数
# list2 = [2,3,4,5,6,7,8,9,10]
# list3 = ['a','b','c','d','e','f','g','h']
# zipped = zip(list2,list3)
# print(list(zipped))


#=============================STRING====================================
# str1 = "hello world"
# print(str1)
# print(str1[0])
# print(str1[-1])
# print(str1[0:-1])

# str2 = "I am a string"
# str3 = " but I am a inter"
# print(str2 + str3)
#
# #字符串相乘
# str4 = "I am a string"
# print(str4 * 2)
#
# #检查成员是否为字符串中的元素
# str5 = "I am a string"
# print("str" in str5)

# #特殊字符可以正常生效
# print("hello\nworld")
# #同时打印出来特殊字符
# print(r"hello\n world")

#字符串分割
# str6 = "hello,world,ooh,my,gard"
# dd = str6.split(',',2)
# print(dd)
# print(dd[0])
#
# #join使用
# list1 = ["a","b","c"]
# join = "-".join(list1)
# print(join)

# str2 = "dfsdfsfs"
# print(str2.find("d",1,5))


#=============================元组=======================================
"""
元组的特点：
1. tuple是不可变的，不能直接对元组汇总的元素进行修改
2. tuple是有序的，即都有下标（索引），可切片获取
3. 可以放不同的类型
4. 定义： ()  即小括号；
"""
# #创建
# tuple1 = (100,200,300,400,500)
# print(tuple1)

# #元组推导式
# tuple_generator = (x for x in range(10))
# print(tuple_generator)
# tuple2 = (100,)
# tuple2 = tuple(tuple_generator)
# print(tuple2)

# #访问元组
# tuple3 = (100, 200, 300, 400, 500)
# print(tuple3[2])
# print(tuple3[-1])
# print(tuple3[2:4])

# #元组相加
# tuple4 = (100, 200, 300, 400, 500)
# tuple5 = ("a", "b", "c", "d", "e", "f")
# print(tuple4 + tuple5)
# print(tuple4 * 2)
#
# #检查成员是否为元组中的元素
# print(100 in tuple4)
#
# #获取元组长度
# print(len(tuple4))
#
# #求元组中的最值
# print(max(tuple4),min(tuple4),sum(tuple4))

# #遍历元组
# for i in tuple4:
#     print(i)
#
# for i in range(len(tuple5)):
#     print(tuple5[i])
#
# for i ,val   in enumerate(tuple5):
#     print(val , i )

#元组的不可变




