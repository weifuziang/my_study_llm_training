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
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        self.__size = 0  # 链表大小
        self.__capacity = 2  # 数组容量大小
        self.__table = [None] * self.__capacity  # 数组存储的结构的初始化
        self.__load_factor = 0.7  # 负载因子（元素个数/数组容量）

    def display(self):
        """显示哈希表内容"""
        for i, node in enumerate(self.__table):
            print(f"索引是{i}", end="")
            current = node
            while current:
                print(f"({current.key} , {current.value}) -> ", end="")
                current = current.next
            print("None")  # 如果什么都没有，则直接返回None
        print()

    def __hash(self, key):
        """根据key的hash值计算数组下标的计算"""
        return hash(key) % self.__capacity

    def __grow(self):
        """哈希表的扩容"""
        self.__capacity *= 2
        self.__table, self.__old_table = [None] * self.__capacity, self.__table
        # 既然创建了新的扩容容器，那么链表的大小也要从0开始，
        # 最主要的原因是：在扩容的同时，会有并发执行put操作
        self.__size = 0
        for node in self.__old_table:
            current = node
            while current:
                self.put(current.key, current.value)
                current = current.next
                self.__size += 1

    def put(self, key, value):
        """哈希表的写入"""
        # 判断是否要扩容
        # if self.__size / self.__capacity >= self.__load_factor:
        # self.__grow()
        # 获取数组索引
        index = self.__hash(key)
        new_node = Node(key, value)
        # 判断数组中是否有node节点
        if self.__table[index] is None:
            self.__table[index] = new_node
        # 出现了hash冲突，则进行链式追加
        else:
            current = self.__table[index]  # 获取链表的头节点
            # 此种方式，虽然避免了 current1.next = new_node赋值时的空指针异常；
            # 但是会出现链式循环无法拿到最后一个节点的判断
            # while current1  and current1.next:

            # 此方式可以拿到最后一个节点，但同时要结合 if current1.next: current1 = current1.next
            # 避免跳出while循环完之后，current1.next = new_node赋值时的空指针异常；
            while current:
                if current.key == key:
                    current.value = value
                    return
                # 此方式就很好的解决了，在"while current:"循环的时候，出现最后一个node对象是None情况
                # 很好的防止了跳出while循环完之后，current1.next = new_node赋值时的空指针异常；
                if not current.next:
                    break
                current = current.next
            # 如果key不存在，则插入到链表尾部
            current.next = new_node
        self.__size += 1

    def remove(self, key):
        """删除元素"""
        index = self.__hash(key)
        current = self.__table[index]
        # 用来区分数组对应下标的链表，到底是不是多个，previous用来代表上一个节点
        # 通过previous有没有node，来区分出来我要删除的node是不是头节点
        previous = None
        while current:
            if key == current.key:
                if previous:  # 非头元素
                    previous.next = current.next
                else:  # 头元素:之前单线current.next是None，所以就单独使用了一个else self.__table[index]=None
                    self.__table[index] = current.next
                self.__size -= 1
                return True
            previous = current  # 用来记录上一个节点
            current = current.next
        return False

    def get(self, key):
        """元素的访问"""
        index = self.__hash(key)
        current = self.__table[index]
        while current:
            if key == current.key:
                return current.value
            current = current.next
        return None

    def for_each(self, func):
        """遍历"""
        for node in self.__table:
            current = node
            while current:
                func(current.key, current.value)
                current = current.next


if __name__ == "__main__":
    hs = HashTable()
    hs.put(1, 10)
    hs.put(2, 20)
    hs.put(3, 30)
    hs.put(4, 40)
    hs.put(5, 50)
    hs.put(6, 60)
    hs.put(7, 70)
    #哈希表冲突后，添加元素的测试，需要把put方法中的链表扩容注释掉，同时，将链表的容量写成最小
    hs.put(1, 80)
    hs.put(7, 90)
    # hs.put(3, 50)

    # hs.put(4, 40)
    # hs.put(1, 50)
    # # 哈希碰撞的链式结构的最有一个节点的修改
    # hs.put(3, 70)

    hs.display()

    # hs.put(4, 40)
    # hs.put(4, 50)
    # hs.remove(3)
    # get = hs.get(1)
    # print(get)
    # hs.for_each(print)
