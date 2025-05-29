"""
高级语法
"""
from typing import Iterator

###===========================================copy===========================================
"""
浅拷贝: 不可变元素，如果在copy之前做了改变，则地址也会变；可变元素，地址则不变
"""
import copy
list1 = [1, 2, 3,[100,200,300]]
print(id(list1),id(list1[0]),id(list1[1]),id(list1[2]),id(list1[3]),list1)
list1[0]=10
list1[3][0]=600
list1[3].append(700)
list2 = copy.copy(list1)
print(id(list2),id(list2[0]),id(list2[1]),id(list2[2]),id(list2[3]),list2)

"""
深拷贝：不可变元素，如果在copy之前做了改变，则地址也会变；可变元素，地址则也会变
"""
list3 = copy.deepcopy(list1)
print(id(list3),id(list3[0]),id(list3[1]),id(list3[2]),id(list3[3]),list3)

"""
1. 非容器类数据类型无法拷贝 (数字、字符串 和其他原子类型)；
2. 元组只包含了原子类型，则不能对其深拷贝；
3. 元组含有了非原子类型，深拷贝后，地址会发生变化；
"""
var1 = 1
var2 = copy.copy(var1)
var3 = copy.deepcopy(var1)
print(id(var1),id(var2),id(var3),var1)

#地址不变
tuple1 = (1,2,3)
tuple2 = copy.copy(tuple1)
tuple3 = copy.deepcopy(tuple1)
print(id(tuple1),id(tuple2),id(tuple3),tuple1)

#深copy地址发生了变化
tuple1 = (1,2,3,[])
tuple2 = copy.copy(tuple1)
tuple3 = copy.deepcopy(tuple1)
print(id(tuple1),id(tuple2),id(tuple3),tuple1)


###===========================================迭代器===========================================
"""
1. 迭代器只能往前不能往后迭代；
2. 字符串、列表、元组,集合都可用迭代器
"""
for element in list1:
    print(element)
for element in {'one':1,'two':2,'three':3,'four':4,'five':5}:
    print(element)
for element in [1,2,3,4,5]:
    print(element)
with open("/Users/wfz/MyJob/MyCode/llm/my_study_llm_training/data/test3","w") as f:
    f.write("H\ne\nf\ng\nom\n")
for line in open("/Users/wfz/MyJob/MyCode/llm/my_study_llm_training/data/test3"):
    print(line,end="====")

"""
判断是否为可迭代对象Iterable
"""
from collections.abc import Iterable

print(isinstance([],Iterable))
print(isinstance((),Iterable))
print(isinstance({},Iterable))
print(isinstance("ddr",Iterable))
print(isinstance(100,Iterable))

"""
判断是否是迭代器Iterator
"""
print(isinstance([],Iterator))
print(isinstance((),Iterator))
print(isinstance({},Iterator))
print(isinstance("ddr",Iterator))
print(isinstance((i for i in range(10)),Iterator))

"""
迭代器
1. 迭代器的使用
2. 迭代器的创建???
"""
#使用
list1 = [1,2,3,[100,200,300]]
iterator = iter(list1)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
for element in iterator:
    print(element)

#创建
class Reverse:
    """ 对一个序列执行反向循环的迭代器"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]
rev = Reverse([2, 3, 5, 7, 11, 13, 17, 19])
iter(rev)
for char in rev:
    print(char)

