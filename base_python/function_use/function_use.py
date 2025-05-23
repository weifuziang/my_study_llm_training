# ===============函数的定义================
"""
1. 带名字的代码块，用于完成具体的任务，可重复使用
2. 内建函数、自定义函数；
3. 函数的好处：简短而清晰、效率高、提高重用性、分工协作开发、集中管理、利于维护

"""

# 函数定义
# def printStar():
#     """
#         函数功能的说明
#     :return:
#     """
#     row = 2
#     while row > 0:
#         print("*" * 3)
#         row -= 1
# printStar()
# print("*" * 20)
# printStar()


# 入参函数的定义
# def printStarComm(row, col):
#     while row > 0:
#         print("*" * col)
#         row -= 1
# printStarComm(5, 6)

# 形参和实参
"""
1. 形参没有分配存储空间，也没有值，相当于一个占位符，
   会在栈区中给函数分配存储空间， 然后给形参/局部变量分配存储空间，传递的是实际的数据；
   
"""

# ======函数的参数传递======
"""
1. 对象引用、对象、指针、类型
a=10
a="helloworld"
以上代码中，10是数字类型，" helloworld " 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是指向数字类型对象，也可以是指向 String 类型对象。

2. 引用的概念
变量和数据是分开的，数据保存在内存中的一个位置，变量中保存着数据在内存中的地址，变量中记录数据的地址，就叫做引用；
使用id()可以查看变量中保存数据所在的内存地址；
注意：如果变量已经被定义，当给一个变量赋值的时候，本质上是修改了数据的引用，变量不再对之前的数据引用，变量改为对新赋值的数据引用，变量的名字类似于便签纸贴在数据上。

3. 传递的可变和不可变类型的区别
不可变类型：number(数字)、String(字符串)、Tuple(元组)
    类似c++的值传递，如整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在fun（a）内部修改a的值，只是修改另一个复制的对象，不会影响 a 本身    注释：修改了地址，旧地址的内容不影响
    
可变的类型：List(列表)、Set(集合)、Dict(字典)
    类似c++的引用传递，如列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
    注释：地址不变，里面的内容改变
  
***Python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。***
"""

#
# # 不可变类型的传递
# def changeInt(a):
#     print("函数内的局部开始之前： ", id(a))
#     a = 10
#     print("函数内的局部变更之后：", id(a))
# b = 1
# print("未传递之前：", id(b))
# changeInt(b)
# print(b)
# print("传递之后：", id(b))
#
# # 可变对象的传递
# def changeList(a):
#     a[1] = 40
#     print("函数内的值: ", a)
#     print("函数内的地址: ", id(a))
# a = [1, 3, 5]
# changeList(a)
# print("函数外的值：", a)
# print("函数外的地址：", id(a))
#
# # var1 *= 2 与 var1 = var1 *2的区别
# def multiply2(var1):
#     print("函数内 var1的地址： ", id(var1))
#     var1 *= 2
#     print("var1*=2 的地址：", id(var1))
#     var1 = var1 * 2
#     print("var1=var1 * 2 的地址：", id(var1))
# #对于可变类型来说，var1 *= 2 是不改变var1的地址的，而var1=var1 *2 是会改变地址的
# list1 = [1, 2, 3]
# print("list1的初始ID：", id(list1))
# multiply2(list1)
# #对于不可变类型，var1 *= 2 与 var1 = var1 *2没有区别，var1地址都会改变
# b=10
# print("b=10初始地址：",id(b))
# multiply2(b)

# 函数可使用的参数形式
# 形参和实参的数量和位置要一致
# def func(a, b, c):
#     print(a, b, c)
#
# func(1, 2, 3)


# 关键字参数：形参和实参位置不一致的传递,以及默认值参数
# def func2(name, age, gender="female"):
#     print(name, age, gender)
#
#
# func2(age=18, name="zww", gender="male")
# func2(age=18, name="zww")
#
#
# # ***不定长参数
# def printInfo(num, *tuple):
#     print(num, tuple)
#
#
# printInfo(1, 2, 3, 6, "9")


# 如果不定长的参数后面还有参数，必须通过关键字参数传递
# def printInfo2(num, *varTuple, num2):
#     print(num, num2, varTuple)
#
#
# printInfo2("1", "2", "3", "4", 4, 0, num2=3)
# 注释：
"""
1. 不定长参数，指的是入参的个数不确定有多少个；
2. 会先通过位置进行必须参数的匹配，然后再是不定长参数的匹配；
3. 不定长参数后面的参数，必须通过关键字参数传递；
4. ***不定长参数会以元组tuple的形式导入，存放所有未命名的变量参数；
"""

# ***可变长参数的传递
# def printInfo3(num, **varDict):
#     print(num, varDict)
#
#
# printInfo3(1, key=2, key2=3, dd=4)
# 注释
"""
1. ***可变长参数会以字典的形式导入，后面就不能再有其他的参数了
"""

# ***解包传参
"""
1. 若函数的形参是定长参数，可以通过 * 和 ** 对列表、元组、字典等解包传参
"""

# def func(a, b, c):
#     return a + b + c


# tuple1 = (1, 2, 3)
# print(func(*tuple1))
# list1 = [1, 2, 3]
# print(func(*list1))
# # 字典类型作为解包传参，其key值一定要和函数的参数必须一致
# dict = {'a': 1, 'b': 2, 'c': 3}
# print(func(**dict))

# 强制使用位置参数或关键字参数
"""
1.??? /前的参数必须使用位置参数，*后的参数必须用关键字传递
"""

# def func1(a, b, c, /, e, f, *, g, h):
#     print(a, b, c, e, f, g, h)
#
#
# func1(1, 2, 3, 4, 5, g=6, h=7)

# 防止函数修改列表
"""
对列表进行处理，但不该表原来列表的内容
"""
# import copy
# def func2(var1):
#     var1[1]=1000
#     print("函数内处理后：",var1)
# list1 = [1, 2, 3]
# print("函数外处理前：", list1)
# func2(copy.deepcopy(list1))
# print("函数外处理后：", list1)

# 函数说明文档
"""
编写了函数说明文档后，可以通过help(函数名)获取函数说明文档
"""
# def func3(age=18):
#     """根据年龄判断是否未成年"""
#     result = "未成年"[age > 18 :]
#     return result
# print(func3(19))
# help(func3)

# =====================================返回值==========================================
"""
返回值

1. 返回值是函数完成工作后，给调用者一个结果；
2. return 关键字可以返回结果，并结束正在执行的函数；
3. 如果return后面跟[表达式]，在结束函数的同时向调用方返回一个表达式；
4. return 后面什么都不跟，则会默认返回一个None;
"""
# def f(a,b,c):
#     pass
#     return
# print(f(1,2,3))
#
# def f2(a,b,c):
#     pass
# print(f2(1,2,3))
#
# def f2(a,b,c):
#     return a+b+c
# print(f2(1,2,3))
#
# def f3(a,b,c):
#     return a+b+c ,[a,b,c]
# print(f3(1,2,3))


# ==========================变量的作用域===============================
"""
1. 四种作用域：局部作用域（local --> 嵌套作用域 即闭包函数外的函数中（enclosing）--> 全局作用域（Global）--> 内建作用域（Built-in）
2. ***只有模块（module）、类（class）以及函数（def lambada）才会引入新的作用域，其他代码块（if/elif/else try/except for/while）
   是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问，如下代码（3）
"""
# 作用域
# a = int(2.9) #内建
# b = 0 #全局
# def outer():
#     c = 1 #内嵌
#     def inner():
#         d=2 #局部
#         print(d,c,b,a)
#     return inner
# in_function = outer()
# in_function()
#
# #代码（3）
# #代码块
# num=2
# if num > 1:
#     msg = "hello world"
# print(msg)
# #函数
# def test():
#     msg_test="hello world"
# print(msg_test) #直接找不到，会报错

"""
global 关键字
1. 全局作用域，在函数中可使用global关键字，才能被修改；
2. 在函数中不使用 global 声明全局变量时，不能修改全局变量的本质是不能修改全局变量的指向，即不能将全局变量指向新的数据；
3. ***不可变类型的全局变量其指向的数据不能修改，所以，不使用global无法修改全局变量；
4. ***可变类型的全局变量其指向的数据可以修改，所以，不使用global也可以修改全局变量；
5. 在函数内使用global关键字的时候，需要先声明global var1 然后在赋值 var1=100;
"""
# var1 = 10
#
# def func1():
#     var1 = 20
#     print(var1)
#
#
# func1()
# print(var1)
#
# def func2():
#     global var1
#     var1 = 20
#     print(var1)
# func2()
# print(var1)

"""
nonlocal 关键字

1. 嵌套作用域的变量，想要被局部作用域修改，则使用nonlocal;
2. 被嵌套的函数（func2），又叫做闭包；

"""
# def func1():
#     a=10 #嵌套作用域（闭包外的作用域）
#     def func2():
#         nonlocal a
#         a=20
#         print(a)
#     func2()
#     print(a)
# func1()

# =============================================递归=============================================
"""
递归

1. 本质：递归调用就是在函数体中又调用了函数本身，即函数嵌套；
2. 核心思想：将大工作划分为最贱减小的小工作；
3. 核心方法: a.确定大工作和小工作之间的规律；b.确定递归结束的条件； 
"""

# # 复习逻辑运算
# # match
# match month := 4:
#     case 1 | 3 | 5 | 7 | 8 | 10 | 12:
#         print(f"{month}月有31天")
#     case 4 | 6 | 9 | 11:
#         print(f"{month}月有30天")
#     case 2:
#         print(f"{month}月可能有28天")
#     case _:
#         print(f"{month}月有?天")
# print(month)
# # 赋值运算符
"""
1. := 海象运算符号，在***表达式中同时进行赋值和返回赋值的值
"""


# num1 = 2
# print((num2 := 3 ** 2) > num1)  # 在表达式中即赋值了num2值 同时也返回了num2的值
# # print((num2=3**2) > num1) #直接报错
# # print((num2=3) > num1) #直接报错
# print(num2 := 1)
# print(num2)

# 三目运算
# print(4 if 3 > 1 else 3)
# num1 = 2
# num2 = 3
# max_num = num2 if num1 > num2 else num1
# print(max_num)

# 递归解题 : 终止条件式 n > 1不成立，则返回 else 1 语句里的1， 且不再调用 n * get_factorial(n)
def get_factorial(n):
    return n * get_factorial(n - 1) if n > 1 else 1
print(get_factorial(5))
