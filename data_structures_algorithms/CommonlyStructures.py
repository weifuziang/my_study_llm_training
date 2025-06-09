"""
抽象数据类型：对数据的一种抽象描述，关注数据的逻辑特性和操作；主要包含：数据对象和操作集合
    1. 数据对象：描述了该数据类型所包含的 数据元素 以及 他们之间的逻辑关系；
    2. 操作集合：定义了对数据对象可以执行的操作；eg: 栈 常见的操作包括 入栈、出栈、产看栈顶元素；
    3. 抽象数据类型强调数据的逻辑性和操作性；
数据结构：是抽象数据类型的具体实现，它关注的是数据在计算机内存中的存储方式和操作的具体实现算法
"""

"""
数组 
基本概念：线性数据结构，将相同类型的元素按照顺序存储在连续的内存空间中，每个元素都有一个索引；
关注点：连续存储、开始索引、数据类型；
注释：python中，并没有严格意义上的”数组“，用list模型、array模块的数组、numpy库的ndarray
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
        """末尾插入元素"""
        self.insert(self.__size, item)


arr = Array()
print(arr.is_empty())
arr.append(1)
arr.append(4)
arr.append(6)
arr.append(9)
print(arr.size)
print(arr.__str__())
# arr.insert(0, 10)
# print(arr.__str__())

# 从10开始，以1的步长开始递减，直到2为止
# for i in range(10 , 2, -1):
#     print(i)
