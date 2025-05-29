"""
1. 导入模块
2. 局部导入
3.

"""
from curses.textpad import rectangle

#======================================导入模块==================================
"""
全部导入为import ： 导入模块的所有成员；
"""
# import my_add as addObj
# print(addObj.add(1, 2))
# print(addObj.num)


"""
局部导入 from import ： 也可以做重新命名的
"""
# from my_add import num as num2
# print(num2)
# from my_add import  add as add3
# print(add3(1, 2))
#
# #导入模块中的所有不以单下划线开头的成员
# from my_add import *
# print(add(1, 2))
# print(age)
# print(num)

###===在被导入的模块中，使用__all__设置哪些内容可以被导入=====
# from my_add import *
# print(num)
# print(age)
# print(add(1,2))

###=== __name__ :
"""
1. 当python文件被直接运行时，该我呢间的__name__属性为"__main__"
2. 当python文件被当做模块导入时，__name__属性会被设置为该模块的名称（即python文件名，不包含.py后缀）
1. 使用 __name__  ==  “__main__” 避免测试代码被执行


"""
# print(__name__)
# if __name__ == '__main__':
#     import my_add as addObj #会打印my_add这个模块中的文件名，即__main__="my_add"
#     print("你是谁？")

#==========================模块搜索顺序================================
"""
当前目录、PYTHONPATH环境变量中的目录、包含标准的Python模块以及这些模块所依赖的任何extension module的目录
"""
import sys
# print(sys.path)
# #可以通过sys.path.append(路径)向 sys.path中临时添加路径
# sys.path.append("./..")
# print(sys.path)

###===列出对象的属性、方法、或者当前作用域中定义的名称，以字符串返回；
# import math
# import my_add
# class Module:
#     def __init__(self):
#         self.x=1
#         self.y=2
#     def my_function(self):
#         pass
#
# print(dir(math))
# print(dir())
# module = Module()
# print(dir(module))

##===导入包===
# # import 包名.模块名 [as 别名]
# import graphic.circle as circle1
# import graphic.rectangle as rectangle1
# print(circle1.area(10))
# print(rectangle1.area(20,10))

# #局部导入包下的模块：from 包名 import 模块名
# from graphic import circle
# print(circle.area(10))

#局部导入包下模块的成员：from 包名.模块名 import 成员名 [as 别名]
# from graphic.circle import area
# print(area(10))

#局部导入from import * 从包中导入模块：并不会查找所有子模块，而是在__init__.py中定义__all__显示索引
##具体看__init__.py中的写法
# from graphic import *
# print(rectangle.area(10,20)) #报错
# print(circle.area(10))

# #import graphic.circle
# import graphic
# print(graphic.circle.area(10)) #报错

###===常用标准库===











