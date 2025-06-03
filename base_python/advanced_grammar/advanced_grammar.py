"""
高级语法
"""
from typing import Iterator

###===========================================copy===========================================
"""
浅拷贝: 不可变元素，如果在copy之前做了改变，则地址也会变；可变元素，地址则不变
"""
# import copy

# (id(list1), id(list1[0]), id(list1[1]), id(list1[2]), id(list1[3]), list1)
# list1[0] = 10
# list1[3][0] = 600
# list1[3].append(700)
# list2 = copy.copy(list1)
# print(id(list2), id(list2[0]), id(list2[1]), id(list2[2]), id(list2[3]), list2)
#
# """
# 深拷贝：不可变元素，如果在copy之前做了改变，则地址也会变；可变元素，地址则也会变
# """
# list3 = copy.deepcopy(list1)
# print(id(list3), id(list3[0]), id(list3[1]), id(list3[2]), id(list3[3]), list3)
list1 = [1, 2, 3,[100,200,300]]
print

"""
1. 非容器类数据类型无法拷贝 (数字、字符串 和其他原子类型)；
2. 元组只包含了原子类型，则不能对其深拷贝；
3. 元组含有了非原子类型，深拷贝后，地址会发生变化；
"""
# var1 = 1
# var2 = copy.copy(var1)
# var3 = copy.deepcopy(var1)
# print(id(var1),id(var2),id(var3),var1)
#
# #地址不变
# tuple1 = (1,2,3)
# tuple2 = copy.copy(tuple1)
# tuple3 = copy.deepcopy(tuple1)
# print(id(tuple1),id(tuple2),id(tuple3),tuple1)

# #深copy地址发生了变化
# tuple1 = (1,2,3,[])
# tuple2 = copy.copy(tuple1)
# tuple3 = copy.deepcopy(tuple1)
# print(id(tuple1),id(tuple2),id(tuple3),tuple1)


###===========================================迭代器===========================================
"""
1. 迭代器只能往前不能往后迭代；
2. 字符串、列表、元组,集合都可用迭代器
"""
# for element in list1:
#     print(element)
# for element in {'one':1,'two':2,'three':3,'four':4,'five':5}:
#     print(element)
# for element in [1,2,3,4,5]:
#     print(element)
# with open("/Users/wfz/MyJob/MyCode/llm/my_study_llm_training/data/test3","w") as f:
#     f.write("H\ne\nf\ng\nom\n")
# for line in open("/Users/wfz/MyJob/MyCode/llm/my_study_llm_training/data/test3"):
#     print(line,end="====")

"""
判断是否为可迭代对象Iterable
"""
# from collections.abc import Iterable
#
# print(isinstance([],Iterable))
# print(isinstance((),Iterable))
# print(isinstance({},Iterable))
# print(isinstance("ddr",Iterable))
# print(isinstance(100,Iterable))

"""
判断是否是迭代器Iterator
"""
# print(isinstance([],Iterator))
# print(isinstance((),Iterator))
# print(isinstance({},Iterator))
# print(isinstance("ddr",Iterator))
# print(isinstance((i for i in range(10)),Iterator))

"""
迭代器
1. 迭代器的使用
2. 迭代器的创建???    
   回顾理解：主要是对__init__()、__iter__()、__next__()固定方法的重写即可
"""
#使用
# list1 = [1,2,3,[100,200,300]]
# iterator = iter(list1)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# for element in iterator:
#     print(element)

#自定义创建迭代器: 主要是对__init__()、__iter__()、__next__()固定方法的重写即可
# class Reverse:
#     """ 对一个序列执行反向循环的迭代器"""
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index -= 1
#         return self.data[self.index]
# rev = Reverse([2, 3, 5, 7, 11, 13, 17, 19])
# iter(rev)
# for char in rev:
#     print(char)

###===========================================生成器（generator）===========================================
"""
1. 推导式创建生成器
2. 函数创建生成器：1. 当生成器中使用yield关键字，每次循环会将yield后面的表达式，作为当前迭代的值返回；
            # 2. yield的使用是逐步产生值的，而不是一次性返回所有值；
            # 3. 可以避免一次性生成大量的数据，并占用大量的值；
"""
#推导式创建生成器
# generator1=(x for x in range(10))
# for x in generator1:
#     print(x)

#函数创建生成器：1. 当生成器中使用yield关键字，每次循环会将yield后面的表达式，作为当前迭代的值返回；
            # 2. yield的使用是逐步产生值的，而不是一次性返回所有值；
            # 3. 可以避免一次性生成大量的数据，并占用大量的值；
# def feibo():
#     a,b=0,1
#     while True:
#         yield b
#         a,b=b,a+b # 是对a和b的重新赋值
#
# g = feibo()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# def feibo2(n): #斐波那契数列的生成
#     a,b,counter=0,1,0
#     while counter < n:
#         yield b
#         a,b,counter=b,a+b,counter+1
#     return "done"

# feibo_ = feibo2(7)
# # print(next(feibo_))
# # print(next(feibo_))
# # print(next(feibo_))
# # print(next(feibo_))
# # print(next(feibo_))
#
# #获取return返回的值
# try:
#     while True:
#         print(next(feibo_))
# except StopIteration as result:
#     print("stopIteration:" ,result.value)

###===send()函数：向生成器中发送值,同时也是跟yield配置使用？？？
"""
1. 需要先启动生成器，且启动时会先执行默认值一次；？？？
"""
# def send_iterator():
#     task_id=-1
#     a = -1
#     b = "A"
#     while True:
#         match task_id:
#             case 1:
#                 task_id= yield a #返回a ,同时接受send()发过来的值给task_id
#                 a=a+1
#             case 2:
#                 task_id= yield b #返回b ,同时接受send()发过来的值给task_id
#                 b= chr(ord(b) + 1)
#             case _:
#                 task_id = yield None
#
#
# f = send_iterator()
# # print(next(f))#启动生成器 方法1
# # f.send(None) #启动生成器 方法2
# print(f.send(None))  # 0
# print(f.send(1))
# print(f.send(2))
# print(f.send(2))
# print(f.send(1))
# print(f.send(2))
# print(f.send(1))


###===========================================命名空间&&作用域===========================================
"""
1. 四种命名空间：local（局部） 、 enclosing（闭包） 、global （全局）、 build-in（内置）
2. 闭包的应用：装饰器、模拟 OOP 的封装、计数器
3. 全局变量 vs 闭包：
    ❌ 缺点：全局变量容易被其他代码修改，不安全。
    ✅ 优点：count 被封装在闭包里，外部无法直接修改，更安全。



"""
###===举例===
x = 1 #global
# def operaton():
#     global x #函数内修改global变量
#     x =10
#     y =100 #local变量
#     def inner():
#         print(y) #闭包内修改local变量
#         # nonlocal y #闭包内修改global变量 enclosing变量
#         # y =20
#         print(y)
#         print(x)
#     inner()
#     print(y)
#     print(x)
#
# operaton()


###===enclosing===
#计数器的应用：此时闭包会记住每次计算的x值作为全局变量，在add中不断累加
# def counter(x):
#     def add(y):
#         return x+y
#     return add
#
# counter1 = counter(5)
# print(counter1(6))
# print(counter1(2))
# print(counter1(1))

#模拟oop的封装
# def person():
#     name = "Unknown"   # "私有"变量
#     def get_name():
#         return name
#     def set_name(new_name):
#         nonlocal name
#         name = new_name
#     return get_name,set_name,
#
# get_name, set_name = person()
# print(get_name())
# set_name("Alice")
# print(get_name()) # 输出 "Alice"

#===装饰器的应用？？？？
"""
1. 本质是一个接收函数作为输入并返回一个新的包装后的函数对象，所以装饰器应该是一个闭包形式的函数；
2. 作用：在不修改原有函数代码的基础上，动态的增加或者修改函数的功能；
3. 多个装饰器时，是从上到下一次执行
"""
#例子1：
from math import sqrt
def decorator(f):
    def inner(y):
        y = abs(y)
        return f(y)
    return inner

def func(x):
    """开根号"""
    return sqrt(x)
#直接传递函数的装饰器调用
f = decorator(func)
print(f(-4))

#装饰器的@decorator使用
@decorator
def func2(x):
    """开根号2"""
    return sqrt(x)

print(func2(-9))

#例子2：多个装饰器的装饰过程
def get_integer(f):
    def inner1(x):
        # x=int(x)
        x=-x
        return f(x)
    return inner1

def get_absolute(f):
    def inner2(x):
        x =abs(x)
        return f(x)
    return inner2

# @get_absolute
@get_integer
def func3(x):
    """开根号"""
    return sqrt(x)
print(func3(-16))

#例子3：带参数的装饰器
from math import sqrt
def times(n):
    def get_absolute(f):
        def inner(x):
            x =abs(x)
            for i in range(n):
                x = f(x+n)
                return x
        return inner
    return get_absolute
@times(20)
def func2(x):
    return sqrt(x)
print(func2(-16))


#例子4：
def call_counter(func1):
    count = 0
    def wrapper2(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"函数 {func1.__name__} 被调用了 {count} 次")
        return func1(*args, **kwargs)
    return wrapper2

@call_counter
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # 输出: 函数 greet 被调用了 1 次 → Hello, Alice!
greet("Bob")    # 输出: 函数 greet 被调用了 2 次 → Hello, Bob!

#类的装饰器: 必须实现__init__()函数中传递func并进行类成员的赋值,__call_()函数中传递func的入参，并return func(x)
class DecoratorClass:
    def __init__(self, f):
        self.f = f

    def __call__(self, x):
        x=abs(x)
        return self.f(x)
@DecoratorClass
def func(x):
    return sqrt(x)

print(func(-4))










