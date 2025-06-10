"""
抽象数据类型：对数据的一种抽象描述，关注数据的逻辑特性和操作；主要包含：数据对象和操作集合
    1. 数据对象：描述了该数据类型所包含的 数据元素 以及 他们之间的逻辑关系；
    2. 操作集合：定义了对数据对象可以执行的操作；eg: 栈 常见的操作包括 入栈、出栈、产看栈顶元素；
    3. 抽象数据类型强调数据的逻辑性和操作性；
数据结构：是抽象数据类型的具体实现，它关注的是数据在计算机内存中的存储方式和操作的具体实现算法
"""

"""
数组 
1. 基本概念：线性数据结构，将相同类型的元素按照顺序存储在连续的内存空间中，每个元素都有一个索引；
2. 关注点：连续存储、***开始索引或者末尾索引（可以知道任意元素位置）***、数据类型；
3. 注释：python中，并没有严格意义上的”数组“，用list模型、array模块的数组、numpy库的ndarray

***数组封装核心***
1. 初始化：
    用什么样的存储？ --> list作为核心存储（self.__items=[0]）；
    数组的初始化容量 --> self.__capacity=8 、 self.__items=[0] * self.__capacity;
    数组的初始化大小 --> self.size=0
    
2. 插入、删除操作
   主逻辑：数组元素挨个移动，并覆盖
   插入：逻辑 --> 从末尾索引依次向后移动一位，直到插入索引（index）的位置，则停止移动，并将self.__items[index]=insertValue进行赋值
        实现 --> for i in range(self.__size,index,-1): self.__items[i]=self.__items[i-1]
                self.__size+=1  
                self.__items[index]=insertValue;
        注释 --> 由于只有知道开始或者末尾索引才能知道元素的位置,同时在插入的时候也要注意数组的capacity是否够用，若不够用则需要进行数组的扩容；
        
   删除：逻辑 --> 从删除索引位置（deleteIndex）开始依次向前移动一位（将删除索引覆盖掉，并将后面的元素都往前移动）
        实现 --> for i in range(deleteIndex,self.__size,1):self.__items[i]=self.__items[i+1]
                self.__size-=1
3. 扩容
    主逻辑：创建新的存储（self.new__items=[0]*self.__capacity*2）,将旧存储（self.__items)元素挨个赋值，
           然后，将新存储地址赋值给旧存储（self.items=self.new__items）
           最后，数组容量进行真是变更（self.capacity=self.__capacity*2）
           
    实现：扩容 --> self.new__items=[0]*self.__capacity*2）
         旧元素迁移 --> for i in range(self.__size): self.new__items[i]=self.__items[i]
         地址回签 --> self.__items=self.new__items
         数组容量变更 --> self.capacity=self.__capacity*2
           

"""


###===数组的创建===
# 使用集合封装
class Array:

    def __init__(self):
        """初始化数组"""
        self.__capacity = 8
        self.__items = [0] * self.__capacity

        self.__size = 0

    def __str__(self):
        """打印数组"""
        arr_str = "["
        for i in range(self.__size):
            arr_str += str(self.__items[i])
            if i < self.__size - 1:
                arr_str += ", "
        arr_str += "]"
        return arr_str

    @property  # 将方法直接转化为属性的方式来调用
    def size(self):
        """获取数组元素个数"""
        return self.__size

    def is_empty(self):
        """判断数组是否为空"""
        return self.__size == 0

    def __grow(self):
        """数组扩容"""
        # 需要用到临时list容器 self.new__items
        self.new__items = [0] * self.__capacity * 2
        for i in range(self.__size):
            self.new__items[i] = self.__items[i]
        self.__items = self.new__items
        self.__capacity *= 2

    def insert(self, index, item):
        """插入元素"""
        if index < 0 or index > self.__size:
            raise IndexError("Index out of range")
        if self.__size == self.__capacity:
            self.__grow()
        for i in range(self.__size, index, -1):
            self.__items[i] = self.__items[i - 1]
        self.__items[index] = item
        self.__size += 1

    def append(self, item):
        """末尾插入元素：同样也调用insert方法，目的是为了统一性，如果不调用，直接用list的append()方法，将不会出现数组扩容操作"""
        self.insert(self.__size, item)

    def remove(self, index):
        """
        删除元素
        :param index:
        :return:
        """
        if index < 0 or index > self.__size:
            raise IndexError("Index out of range")
        for i in range(index, self.__size):
            self.__items[i] = self.__items[i + 1]  # 操作数组依次向右移动，index位置的元素会直接被index+1（即 i+1）覆盖掉
        self.__size -= 1

    def set(self, index, item):
        """修改元素"""
        if index < 0 or index > self.__size:
            raise IndexError("Index out of range")
        self.__items[index] = item

    def get(self, index):
        """访问元素"""
        if index < 0 or index >= self.__size:
            raise IndexError
        return self.__items[index]

    def find(self, item):
        """查看元素"""
        for i in range(self.__size):
            if self.__items[i] == item:
                return i
        return -1

    def forEach(self):
        for i in range(self.__size):
            print(self.__items[i])


arr = Array()
print(arr.is_empty())
arr.append(1)
arr.append(4)
arr.append(6)
arr.append(9)
print(arr.size)
print(arr.__str__())
print(arr.get(2))
# arr.remove(0)
arr.set(0, 100)
arr.insert(0, 101)
arr.forEach()
# arr.insert(0, 10)
# print(arr.__str__())

# 从10开始，以1的步长开始递减，直到2为止
# for i in range(10 , 2, -1):
#     print(i)
