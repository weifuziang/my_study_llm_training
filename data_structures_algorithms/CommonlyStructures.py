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
2. 关注点：连续存储、***开始索引或者末尾索引（可以知道任意元素位置）***、数据类型、索引；
3. 注释：python中，并没有严格意义上的”数组“，用list模拟、array模块的数组、numpy库的ndarray

4. ***数组封装核心***
    1> 初始化：
        用什么样的存储？ --> list作为核心存储（self.__items=[0]）；
        数组的初始化容量 --> self.__capacity=8 、 self.__items=[0] * self.__capacity;
        数组的初始化大小 --> self.size=0
    
    2> 插入、删除操作：
        主逻辑：挨个移动数组元素，并覆盖
        插入：逻辑 --> 从末尾索引依次向后移动一位，直到插入索引（index）的位置，则停止移动，并将self.__items[index]=insertValue进行赋值
             实现 --> for i in range(self.__size,index,-1): self.__items[i]=self.__items[i-1]
                self.__size+=1  
                self.__items[index]=insertValue;
             注释 --> 由于只有知道开始或者末尾索引才能知道元素的位置,同时在插入的时候也要注意数组的capacity是否够用，若不够用则需要进行数组的扩容；
        
        删除：逻辑 --> 从删除索引位置（deleteIndex）开始依次向前移动一位（将删除索引覆盖掉，并将后面的元素都往前移动）
             实现 --> for i in range(deleteIndex,self.__size,1):self.__items[i]=self.__items[i+1]
                self.__size-=1
    3> 扩容
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


# arr = Array()
# print(arr.is_empty())
# arr.append(1)
# arr.append(4)
# arr.append(6)
# arr.append(9)
# print(arr.size)
# print(arr.__str__())
# print(arr.get(2))
# # arr.remove(0)
# arr.set(0, 100)
# arr.insert(0, 101)
# arr.forEach()
# arr.insert(0, 10)
# print(arr.__str__())

# 从10开始，以1的步长开始递减，直到2为止
# for i in range(10 , 2, -1):
#     print(i)

"""
链表（LinkedList）
1. 基本概念：逻辑上是线性结构的类型、存储上是分散存储；
2. 表现形式：每个节点(Node)包含一个元素和一个指向下一个节点的指针(pointer)； 
3. 关注点：
        插入和删除 --> 只需要修改指针的指向即可；
        扩容 --> 随时动态的增长或缩小，无需像数组一样预先指定大小；
        查询 --> 需要从头节点开始遍历链表，直到找到目标节点，***访问效率极低***；
        存储大小 --> 需要额外的空间存储下一个节点的指针，相比于数组存储相同的数据元素，需要更多的内存空间； 
        
4. 链表的种类：单向链表 --> 头节点、尾节点（指向空None）、每个节点包含值和指向下一个节点的指针；
             环形链表 --> 将单向链表的尾节点指向头节点（首尾相连），其中每个节点都可以视作头节点；
             双向链表 --> 同时记录了两个方向的指针，即指向后继节点（下一个节点）和前驱节点（上一个节点）的指针；

5. 链表的功能：size()、
             is_empty()
             insert(index,item)
             remove(index)
             append(item)#尾部追加
             set(index,item)#修改
             get(index)#元素的获取
             find(item)#元素位置的查询
             for_each()#遍历列表

6. ***链表封装核心***
    1> 初始化：链表节点类class（Node来存储元素的‘容器’）、链表head节点（self.__head=None）、链表大小（self.__size=0）
    2> 插入和删除：
            逻辑：从链表head节点遍历开始遍历(使用推导式range)，找到插入或者删除节点的前一个节点，然后进行指针操作；
            实现：插入--> node=self.__head 
                        for i in range(index-1):
                            node=node.next
                        node.next = Node(item,node.next)
                        self.__size+=1
                删除 --> node=self.__head 
                        for i in range(index-1):
                            node=node.next
                        node.next = Node(item,node.next.next)
            共同逻辑：使用推导式遍历找到目标位置的前一个node(index-1) ,即
                    node=self.__head 
                    for i in range(index-1):
                        node=node.next
    3> 修改和访问：
            逻辑：直接使用推导式range直到目标元素位置index即可
            实现：node = self.__head
                 for i in range(index):
                        node=node.next
    
    4> 查找和遍历
            逻辑：直接操作的是节点元素，而不是给定位置去查找，所以只能使用while的方式遍历
            实现：node = self.__head
                 while node:
                    node=node.next
"""

###===单向链表的创建===
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
#
#
# class LinkedList:
#     def __init__(self):
#         """链表初始化"""
#         self.__head = None
#         self.__size = 0
#
#     def __str__(self):
#         """打印链表"""
#         result = []
#         current = self.__head  # 要从头节点开始
#         while current:
#             result.append(str(current.data))
#             current = current.next
#         return "->".join(result)
#
#     @property  # 大小方法转属性使用
#     def size(self):
#         """获取链表的大小"""
#         return self.__size
#
#     def is_empty(self):
#         """判断链表是否为空"""
#         return self.size == 0
#
#     def insert(self, index, item):
#         """插入node元素"""
#         if index < 0 or index > self.__size:
#             raise IndexError("Index out of range")
#         # 插入到头部： 新建Node --> 将插入元素的next指向head --> 新的Node再赋值给head
#         if index == 0:
#             self.__head = Node(item, self.__head)
#         # 插入到中间：用推导式range
#         else:
#             node = self.__head
#             for i in range(index - 1):  # 找到index-1(也就是插入位置的上一个节点)的node
#                 node = node.next  # node代表index-1的位置
#             # node.next代表index的位置，同时先new Node(item, node.next) 然后再赋值 node.next = Node(item, node.next)，
#             # 所以不会出现node.next对应的node丢失的问题;
#             # 具体逻辑为：新节点的next执行index位置（node.next）,index-1的节点的next指向新节点
#             node.next = Node(item, node.next)
#         self.__size += 1
#
#     def append(self, item):
#         """末尾追加元素"""
#         ###===self.size正好是尾节点的下一个node的index(神奇的下表index和size)
#         self.insert(self.__size, item)
#
#     ###===自己写===
#     # tmp_index = 0
#     # current = self.__head
#     # while current:
#     #     if index != tmp_index:
#     #         current = current.next
#     #         tmp_index += 1
#     #     else:
#     #         node = Node(item)
#     #         current_next = current.next
#     #         current.next = node
#     #         node.next = current_next
#     #         return True
#     ###===自己写===
#
#     def remove(self, index):
#         if index < 0 or index > self.__size:
#             raise IndexError("Index out of range")
#         if index == 0:
#             self.__head = self.__head.next
#         else:
#             node = self.__head
#             # 通过推导式找到要删除index的上一个index-1位置的node1节点
#             # 使用node.next.next获取index+1位置的node2节点
#             # 赋值将index-1位置的node1节点next指针指向index+1位置的node2节点
#             # 链表大小减一
#             for i in range(index - 1):
#                 node = node.next
#             node.next = node.next
#         self.__size -= 1
#
#     def set(self, index, item):
#         """修改的是节点的值，而不是把节点替换掉"""
#         if index < 0 or index > self.__size:
#             raise IndexError("Index out of range")
#         node = self.__head
#         for i in range(index):
#             node = node.next
#         node.data = item
#
#     def get(self, index):
#         """访问元素"""
#         if index < 0 or index > self.__size:
#             raise IndexError("Index out of range")
#
#         node = self.__head
#         for i in range(index):
#             node = node.next
#         return node.data
#
#     def find(self, item):
#         node = self.__head
#         # for i in range(self.__size - 1):
#         while node:
#             if node.data == item:
#                 return True
#             node = node.next
#         return False
#
#     def for_each(self):
#         """遍历链表"""
#         node = self.__head
#         while node:
#             print(node.data)
#             node = node.next


# linkList = LinkedList()
# linkList.append(1)
# linkList.append(2)
# linkList.append(3)
# linkList.append(4)
# linkList.append(5)
#
# get = linkList.get(1)
# print(get)
# find = linkList.find(10)
# print(find)
# linkList.for_each()


# for i in range(0):
#     print(i)

"""
栈
1. 基本概念：一个线性结构;
2. 表现形式：维护了一个有序的数据列表(有索引)，有栈顶（top）和 栈底（bottom）
2. 特点：先进后出的原则(LIFO Last-In-First-Out)
3. 基本功能：size()、is_empty()、push(item)、pop()、peek()#获取栈顶元素但是不弹出

4. ***栈的构建核心***
    1> 初始化：存储容器（self.__items=[]）、栈大小属性（self.__size=0）
    
    2> 出栈：
        逻辑：从list最大的索引（self.__size-1）开始出栈，拿到元素后记成临时变量后，
            将该元素从list中删除，最后将self.__size -1；
        实现：item = items[self.__size-1]
             del items[self.__size-1]
             self.__size -= 1
             return item
    
    3> 入栈：
        逻辑：直接使用列表的append(),同时控制self.__size()
        实现：self.__items.append(item)
             self.__size += 1
    

"""


###===栈的实现===
class Stack:
    def __init__(self):
        self.__size = 0
        self.__items = []

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def push(self, item):
        self.__items.append(item)
        self.__size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        item = self.__items[self.__size - 1]  # 后进入的索引最大，会先出栈，所以从最大所以self.__size-1 开始
        del self.__items[self.__size - 1]
        self.__size -= 1  # 记得出栈后要把栈的size减一***
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.__items[self.__size - 1]


###===栈应用===
"""
1）有效括号
力扣20题https://leetcode.cn/problems/valid-parentheses/description/
（1）题目描述
给定一个只包括“(”，“)”，“[”，“]”，“{”，“}”的字符串s，判断字符串是否有效。
有效字符串需满足：
	左括号必须用相同类型的右括号闭合。
	左括号必须以正确的顺序闭合。
	每个右括号都有一个对应的相同类型的左括号。
（2）示例
示例 1：
输入：s = "()"
输出：true
示例 2：
输入：s = "()[]{}"
输出：true
示例 3：
输入：s = "(]"
输出：false
示例 4：
输入：s = "([])"
输出：true

解题思路：
1. 枚举出所有括号的右半边部分，只要遇到就进行栈的push()
2. 括号的右半边部分，通过match case 进行区分处理，并判断按照顺序pop()的元素是不是对应的括号左半边；
3. 判断按照顺序pop()的元素都要同时判断stack是不是空了；
4. 循环判断完之后，进行return的时候也要进行判读一次栈是否为空了；

"""


class Solution:
    def isValid(self, s):
        stack = Stack()
        for i in s:
            match i:
                case "(" | "[" | "{":
                    stack.push(i)
                case ")":
                    if stack.is_empty() or stack.pop() != "(":
                        return False
                case "]":
                    if stack.is_empty() or stack.pop() != "[":
                        return False
                case "}":
                    if stack.is_empty() or stack.pop() != "{":
                        return False

        # 主要需要判断最终栈是不是为空，是为了防止s="()[]{}{"可能返回true
        return True if stack.is_empty() else False


# if __name__ == "__main__":
#     Solution = Solution()
#     s="()[]{}{"
#     solution = Solution.isValid(s)
#     print(solution)
#
#     s1="((([[[{{{}}}]]])))"
#     solution = Solution.isValid(s1)
#     print(solution)
"""
队列
1. 基本概念：线性结构；
2. 表现形式：同样也维护了一个有序的数据列表(链表)，队首、队尾；
3. 特点：队尾元素的插入、队首元素删除，即先进先出FIFO（First-In-First-Out）
4. 功能：size() is_empty() push(item)#向队尾添加元素 pop()#从队首取元素 peek()#访问队首元素

5. ***队列构建核心***
    1>  初始化前：链表Node类的初始化
        初始化：队首属性、队尾属性、队大小属性
       注释：抓住该数据结构的可操作的特征来做__init__()方法的初始化，即队首、队尾、队大小属性；
            展开讲,队列我操作入队列和出队的时候，需要时刻保持知道队首是谁、队尾是谁、队是否还有元素
    2> push(self,item):
        逻辑：已经知道队尾是谁，则可以直接操作队尾添加元素，同时，记得再次更新队尾；
        实现：if self.__size == 0: self.__head = Node(item) self.__tail = Node(item)
             self.__tail.next=Node(item)
             self.__tail=Node(item)
             self.__size +=1
    3> pop():
        逻辑：已知队首是谁了，则可以直接操作队首元素，同时，节点再次更新队首元素；
        实现：if self.__size == 0: raise IndexError("queue is empty")
             head = self.__head
             self.__head= self.__head.next
             self.__size -=1
             return head
        
"""

###===队列的实现===
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
#
#
# class Queue:
#     def __init__(self):
#         """
#         初始化
#         """
#         self.__size = 0
#         # 始终要知道队首是谁,仅为一个node地址标识，要求随时可以取到
#         self.__head = None
#         # 始终要知道队尾是谁，仅为一个node地址标识，要求随时可以取到
#         self.__tail = None
#
#     @property
#     def size(self):
#         return self.__size
#
#     def is_empty(self):
#         return self.__size == 0
#
#     def push(self, item):
#
#         node = Node(item)
#         if self.is_empty():
#             self.__head = node
#             self.__tail = node
#         else:
#             self.__tail.next = node  # 用已经知道的tail，直接追加
#             self.__tail = node  # 追加完，一定要更显队尾的标识符地址指向新追加的node元素
#         self.__size += 1
#
#         ###===自己的代码===
#         """
#         问题点：1. 需要时刻知道队首和队尾是谁；
#                2. 已经知道了队尾，那在进行入队的实时，可以直接操作self.__tail得这node元素
#         """
#         # if self.is_empty():
#         #     self.__head = Node(item, self.__tail)
#         # node = self.__head
#         # while node:
#         #     node = node.next
#         # node.next = Node(item, self.__tail)
#         # self.__size += 1
#
#     def pop(self):
#         """出队列"""
#         if self.is_empty():
#             raise IndexError("Queue is empty")
#         head = self.__head
#         self.__head = self.__head.next
#         self.__size -= 1
#         return head.data
#
#     def peek(self):
#         """访问队列首元素"""
#         if self.is_empty():
#             raise IndexError("Queue is empty")
#         return self.__head.data

"""
哈希表
1. 基本概念：哈希表（hash Table），也叫做散列表，由一系列键值对（key-value）组成
2. 特点：
        1> 向哈希表中输入一个key,可以在O(1)的时间内获取对应的value值；
        通常是根据key来查找value;
        2> 为了防止hash()冲突，会选用数组+链表来定义哈希表；
        3> 常见的哈希算法：除法哈希、乘法哈希、MurmurHash(速度快)、CityHash
           加密哈希算法：MD5（已被成功攻击）、SHA-1（已被成功攻击）、SHA-2、SHA-3
           文件完成性检查算法：Adler-32 CRC32
        4> hash冲突的解决方法：
            链式法：也是hash表的解决方法（数组+链表）
            开放寻址法？？？：当发生hash冲突事根据某种探查策略寻找下一个空槽位。常见的探查策略包括如下，
                            线性探查、二次探查、双重哈希
        5> ***负载因子***：
            哈希表中的元素个数和表容量大小的比例；
            较小的负载因子可以减少冲突的可能性；
            较大的负载因子可以提高哈希表的内存利用率
            通常的负载因子是0.7~0.8
3. 哈希表功能：
        size()、is_empty()、put(key,value)、remove(key)、display()、get(key)、for_each()



3. ***哈希表的创建***
    1> 初始化前：链表的Node类，注意此时的Node的初始化需要存储两个元素即key 和 value
    2> 初始化：哈希表的大小（self.__size）、
              哈希表本身的容量（self.__capacity）、
              存储容器（列表模拟的数组self.__table=[None]*self.__capacity）
              负载因子（self.__load_factor）: 决定了何时扩容，因为哈希碰撞，所以不能用self.__capacity单一因素作为评估扩容的指标
       注释：哈希表容器大小（capacity）、哈希表大小(size)以及负载因子的关系(load_factor)：
            先有数据结构的容器大小（空间大小），再有可以装的数据元素的大小（数量装载大小）、
            最后再有如果出现了空间大小和数据装载大小不匹配的时的评估指标，即负载因子；
    3> put(key,value):
        主逻辑：首先要判断是否要扩容；其次，获取key对于的数组索引，如果没有hash索引冲突直接放入；如果出现了hash索引重复，则进行链式操作;
               链式操作的主要分两种情况，1：插入的是重复的key值，则要对每一个已有的链式节点进行key值判断；
                                     2：插入的key是不重复的，只需要while循环到链表的尾部直接进行current.next=Node(key,value)赋值
        实现：if self.__size/self.__capacity >= self.__load_factor: self.__grow()
             index = self.__hash(key)
             current = self.__table[index]
             if current is not None:
                self.__table[index] = current
            else:#哈希冲突
                 # ***此方式可以拿到最后一个节点，但同时要结合 if current1.next: current1 = current1.next
                 # 避免跳出while循环完之后，current1.next = new_node赋值时的空指针异常；
                while current:
                        if current.key == key:
                            current.value = value
                            return
                        # ***此方式就很好的解决了，在"while current:"循环的时候，出现最后一个node对象是None情况
                        # 很好的防止了跳出while循环完之后，current1.next = new_node赋值时的空指针异常
                        if not current.next:
                            break
                        current=current.next
                    current.next = Node(key,value)
                    self.__size += 1
        注意***：在出现哈希碰撞后，该索引位置进行的链式查询，要注意如下：
                a. "while current"循环完后,在进行追加时current.next = Node(key,value)赋值时候出现空指针异常；
                b. 修正后如果使用"while current.next",是无法循环拿到最有一个node节点的；
                c. 最合理的方式是"while current: ...... if current.next: current = current.next"
    4> grow():
        主逻辑：创建新的存储容器，并进行容量的double，将旧容器再循环复值给新容器；
            注意扩容的时候有人在并发的put，此时可以先将self.__size=0,然后再进行新旧容器的搬迁；
        实现：self.__capacity *=2
             self.__table, self.__old_table=[None]*self.__capacity, self.__table
             self.__size=0 #防止有人并行的在写入，所以先置零
             for node in self.__old_table:
                while node:
                    self.put(node.key, node.value)
                    node=node.next
                    self.__size += 1
        注意***：在进行搬家的时候，有人并行put操作；
                搬家的时候可直接使用put操作，不要自己再写了；

    5> remove(key):
        主逻辑：找到的node节点所在的数组索引里是不是只有一个节点，如果不是则需要链式循环查询，但是一旦查询到了，进行删除的时候，
               需要区分是不是头节点，如果不是头节点，你还需要知道前一个node，
               所以,需要一个pre=Node的变量来记录前一个node节点
        实现：index = hash(key)
             current = self.__table[index]
             pre=None
             while current:
                if current.key == key:
                    if pre is None: #头节点
                        current=None
                    else: #非头节点
                        pre.next=current.next
                    self.__size -= 1
                    return True
                pre = current #记录前一个节点
                current = current.next
             return False
        注意：在出现哈希碰撞后，该索引位置进行的链式节点循环查找删除时，要注意如下，
             a. 头节点的删除和非头节点的删除方式不同；
             b. 非头节点删除时，需要引入pre（前一个节点）变量存储，才能实现指针操作删除current节点
                pre.current=current.next.next
"""

###===哈希表的创建===
# class Node:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None
#
#
# class HashTable:
#     def __init__(self):
#         self.__size = 0  # 链表大小
#         self.__capacity = 2  # 数组容量大小
#         self.__table = [None] * self.__capacity  # 数组存储的结构的初始化
#         self.__load_factor = 0.7  # 负载因子（元素个数/数组容量）
#
#     def display(self):
#         """显示哈希表内容"""
#         for i, node in enumerate(self.__table):
#             print(f"索引是{i}", end="")
#             current = node
#             while current:
#                 print(f"({current.key} , {current.value}) -> ", end="")
#                 current = current.next
#             print("None")  # 如果什么都没有，则直接返回None
#         print()
#
#     def __hash(self, key):
#         """根据key的hash值计算数组下标的计算"""
#         return hash(key) % self.__capacity
#
#     def __grow(self):
#         """哈希表的扩容"""
#         self.__capacity *= 2
#         self.__table, self.__old_table = [None] * self.__capacity, self.__table
#         # 既然创建了新的扩容容器，那么链表的大小也要从0开始，
#         # 最主要的原因是：在扩容的同时，会有并发执行put操作
#         self.__size = 0
#         for node in self.__old_table:
#             current = node
#             while current:
#                 self.put(current.key, current.value)
#                 current = current.next
#                 self.__size += 1
#
#     def put(self, key, value):
#         """哈希表的写入"""
#         # 判断是否要扩容
#         # if self.__size / self.__capacity >= self.__load_factor:
#         # self.__grow()
#         # 获取数组索引
#         index = self.__hash(key)
#         new_node = Node(key, value)
#         # 判断数组中是否有node节点
#         if self.__table[index] is None:
#             self.__table[index] = new_node
#         # 出现了hash冲突，则进行链式追加
#         else:
#             current = self.__table[index]  # 获取链表的头节点
#             # 此种方式，虽然避免了 current1.next = new_node赋值时的空指针异常；
#             # 但是会出现链式循环无法拿到最后一个节点的判断
#             # while current1  and current1.next:
#
#             # 此方式可以拿到最后一个节点，但同时要结合 if current1.next: current1 = current1.next
#             # 避免跳出while循环完之后，current1.next = new_node赋值时的空指针异常；
#             while current:
#                 if current.key == key:
#                     current.value = value
#                     return
#                 # 此方式就很好的解决了，在"while current:"循环的时候，出现最后一个node对象是None情况
#                 # 很好的防止了跳出while循环完之后，current1.next = new_node赋值时的空指针异常；
#                 if not current.next:
#                     break
#                 current = current.next
#             # 如果key不存在，则插入到链表尾部
#             current.next = new_node
#         self.__size += 1
#
#     def remove(self, key):
#         """删除元素"""
#         index = self.__hash(key)
#         current = self.__table[index]
#         # 用来区分数组对应下标的链表，到底是不是多个，previous用来代表上一个节点
#         # 通过previous有没有node，来区分出来我要删除的node是不是头节点
#         previous = None
#         while current:
#             if key == current.key:
#                 if previous:  # 非头元素
#                     previous.next = current.next
#                 else:  # 头元素:之前单线current.next是None，所以就单独使用了一个else self.__table[index]=None
#                     self.__table[index] = current.next
#                 self.__size -= 1
#                 return True
#             previous = current  # 用来记录上一个节点
#             current = current.next
#         return False
#
#     def get(self, key):
#         """元素的访问"""
#         index = self.__hash(key)
#         current = self.__table[index]
#         while current:
#             if key == current.key:
#                 return current.value
#             current = current.next
#         return None
#
#     def for_each(self, func):
#         """遍历"""
#         for node in self.__table:
#             current = node
#             while current:
#                 func(current.key, current.value)
#                 current = current.next
#
#
# if __name__ == "__main__":
#     hs = HashTable()
#     hs.put(1, 10)
#     hs.put(2, 20)
#     hs.put(3, 30)
#     hs.put(4, 40)
#     hs.put(5, 50)
#     hs.put(6, 60)
#     hs.put(7, 70)
#     #哈希表冲突后，添加元素的测试，需要把put方法中的链表扩容注释掉，同时，将链表的容量写成最小
#     hs.put(1, 80)
#     hs.put(7, 90)
#     # hs.put(3, 50)
#
#     # hs.put(4, 40)
#     # hs.put(1, 50)
#     # # 哈希碰撞的链式结构的最有一个节点的修改
#     # hs.put(3, 70)
#     hs.display()
#     # hs.put(4, 40)
#     # hs.put(4, 50)
#     # hs.remove(3)
#     # get = hs.get(1)
#     # print(get)
#     # hs.for_each(print)

"""
树
1. 基本概念；一系列具有层次关系的节点（Node）组成
2. 特点：父节点、子节点、根节点、叶节点（位于树的底端，没有子节点的节点）、边（连接两个节点的线段）；
        节点的度：节点的子节点数量；
        节点的层：从根开始定义起，根为第一层，根的子节点为第2层，以此类推；
        节点的深度（向上）：从根节点到该节点所经过的边的数量，根的数量为0；
        节点的高度（向下）：从距离该节点最远的叶节点到该节点所经过的边的数量，所有叶子节点高度为零；
        树的高度：从根节点到最远叶子节点所经过边的数量；
        注意：高度和深度说的都是边的数量、层指的是节点有几层     
3. 二叉树：每个节点最多只能有两个子节点，两个子节点分别被称为左子节点和右子节点，
            以左节点为根节点的子树成为左子树、右边的成为右子树；
4. 二叉树的特点：可以使用数组结构存储（增减效率低不是主流）、链表结构存储（主流）
5. 常见的二叉树：完全二叉树（最下面一层的节点未被填满，且靠左填充）；
               满二叉树（所有层的节点被完全填满）
               平衡二叉树：任意节点的左右子树高度之差不超过1；
               二叉搜索树（有序）：每个节点的值，大于其左子树中的所有节点值，并且小于右子树中的所有节点值；
               AVL树：AVL树是一种子平衡的二叉搜索树，插入和删除时会进行旋转操作来保证书的平衡性；
               红黑树：特殊的二叉搜索树，除了二叉搜索树的要求之外，它还具备以下特点：
                      每个节点或者是黑色，或者是红色；
                      根节点是黑色；
                      每个叶节点都是黑色，这里的叶节点是指空（None）的节点；
                      红色节点的两个子节点必须是黑色的，即每个叶到根的所有路径上不能有两个连续的红色节点；
                      从任意一个节点到其每个叶的所有路径上包含相同数目的黑色节点；
                堆：特定条件的完全二叉树，主要分为两种：
                    大顶堆： 每个父节点的值都大于等于其子节点的值。根节点为树中的最大值；
                    小顶堆： 每个父节点的值都小于等于其子节点的值。根节点为树中的最小值；
                霍夫曼树：最优二叉树，是一种带权路径长度最短的二叉树，常用于数据压缩，它的构建基于字符出现频率的概率；
                B树：自平衡的多路查找树，不是严格意义上的二叉树，但与二叉树的结构类似，经常用于数据库、文件系统等需要磁盘访问的应用；
                B+树：是B树的优化版本，它将数据集中存储在叶子节点，并通过链表连接来实现高效的范围查询，并且非叶子节点仅存储索引，提高了磁盘利用率；
               
3. 功能：size() is_empty() search() remove() for_each(func,order)

"""

###===二叉树的创建===
from collections import deque


class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """搜索二叉树"""

    def __init__(self):
        self.__root = None
        self.__size = 0

    @property
    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    # 直接复制过来的，可以先不用管
    def print_tree(self):
        """打印树的结构"""

        # 先得到树层高
        def get_layer(node):
            """递归计算树的层数"""
            if node is None:
                return 0
            else:
                left_depth = get_layer(node.left)
                right_depth = get_layer(node.right)
                return max(left_depth, right_depth) + 1

        layer = get_layer(self.__root)

        # 层序遍历并打印
        queue = deque([(self.__root, 1)])
        current_level = 1
        while queue:
            node, level = queue.popleft()
            if level > current_level:
                print()
                current_level += 1
            if node:
                print(f"{node.data:^{20 * layer // 2 ** (level - 1)}}", end="")
            else:
                print(f"{"N":^{20 * layer // 2 ** (level - 1)}}", end="")
            if level < layer:
                if node:
                    queue.append((node.left, level + 1))
                    queue.append((node.right, level + 1))
                else:
                    queue.append((None, level + 1))
                    queue.append((None, level + 1))
        print()

    def search(self, item):
        """二叉搜索树查找元素是否存在"""
        return self.__search_pops(item)[0] is not None

    def __search_pops(self, item):
        """基础的查找方法，同时返回current 和 parent节点"""
        current = self.__root
        parent = None
        while current:
            if current.value == item:
                break  # 跳出循环
            parent = current
            current = current.left if item < current.value else current.right
        return current, parent

    # 添加操作，仅仅只有左右节点的添加 或者 存在不动
    def add(self, item):
        """二叉搜索树的添加"""
        new_node = Node(item)
        if self.is_empty():
            self.__root = new_node
        else:  # 不是空，说明只有两种情况；current存在,和current不存在
            current, parent = self.__search_pops(item)
            if current:  # 节点值存在，直接返回
                return
            if item < parent:  # current不存在，使用父节点进行判断追加
                parent.left = new_node
            else:
                parent.right = new_node
        self.__size += 1

    # 相对复杂，删除完了要各种倒腾
    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            raise IndexError
        # 查找要删除的节点
        current, parent = self.__search_pops(item)
        # 没有找到
        if not current:
            return
        # 找到了，此时要抓主要矛盾，即被删除节点的情况（没有一个节点，有一个节点，有两个节点），这个大矛盾抓住之后，再同时考虑，每种情况里，有没有父节点
        # 也就是说删除操作是在，被删除节点本身，被删除节点的子节点，以及被删除节点的父节点 之间进行操作的；

        # 情况1：被删除节点没有一个子节点，即，可以是叶子节点，也有可能是根节点；
        if not current.left and not current.right:
            if parent:  # 有父节点，说明就是叶子节点
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            else:  # 没有父节点，说明current就是根节点
                self.__root = None

        # 情况2：被删除节点只有一个子节点，可能为左子节点，也有可能为右子节点；
        if not current.left or not current.right:
            # 公共代码的提取，总归是需要知道是左右子节点哪个不是None
            child = current.left if current.left else current.right
            if parent:#current有父节点
                if parent.left == current:
                    parent.left = child
                else:
                    parent.right = child
                # 自己写的
                # if current.left :
                #     parent.left = current.left
                # else:
                #     parent.right = current.left
            else: #current就是根节点
                self.__root = child

        # 情况3：被删除节点有两个子节点；
        else:
            #找到右子树中最小的那个元素，放到current的位置
            get_min_node = self.__get_min(current.right)
            if parent:
                #巧妙的办法：先记录找到node的data值，然后将其node对象删掉，最后将data值赋值给current的value
                data = get_min_node.data
                self.remove(data)
                #只用用找到的get_min_node对当前current进行赋值
                current.data = data
                #此时做了一次最小元素的删除，但是在最终也会做一次self.__size -= 1，所以此时要加1
                self.__size += 1
            else:
                self.__root = get_min_node

        self.__size -= 1

    def __get_min(self,node):
        """右子树里最小的元素一定是在left的left里，所以while只需要一直current.left就好"""
        current = node
        while current.left:
            current =current.left
        return current


