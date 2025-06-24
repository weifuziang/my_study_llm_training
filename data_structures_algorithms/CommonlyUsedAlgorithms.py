"""
常用的算法
"""

"""
查找类算法-二分查找
    基本特点：
    1. 又称折半查找，适用于有序列表；
    2. 其利用数据的有序性，每轮缩小一半搜索范围，直至找到目标元素
    
    复杂度：
    时间复杂度:O(logn)
    空间复杂度：O(1)
    
    主要逻辑：
    1. 左右区间left、right的索引的初始化 left,right = 0 ,len(arr)-1；
    2. 执行条件while left <= right
    3. 中间mid索引的计算 : mid = left + (right-left) // 2
    4. 左右区间left、right的索引的循环变更：if arr[mid] < item: left = mid +1 else: right = mid -1 
 
    核心思考：
    1. 数理逻辑的构建：左右区间的无限查找，那就一定有left、right 以及left 和right的动态变更；
    2. 每次找的是区间的中间元素，那一定就有中间区间索引mid的计算：mid=left + (right-left) // 2
       既然是有序的集合，那mid计算的时候一定要有一个基点那就是left
"""


def binarySearch(arr, item):
    """二分查找"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == item:
            return mid
        if arr[mid] < item:
            left = mid + 1
        else:
            right = mid - 1
    # 没有找到目标元素
    return -1


# if __name__ == '__main__':
#     nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     print(binarySearch(nums, 6))

"""
排序类算法-冒泡排序
    基本概念：
    1. 将待排序数组分为无序区间和有序区间两部分，主要是相邻两个元素做比较；
    2. 逐个将无序区间中的最大值冒出到末尾，直到无序区间的所有元素都冒出到有序区间
    
    时间复杂度：O(n^2)
    空间复杂度：O(1)
    
    思路：
    1. 相邻两数的比较，因此就需要nums(j) 、nums(j+1)
    2. 比较完，就要进行交换操作（每一次都要交换）；
    3. 比较的次数 n * n 所以需要双层for循环，在每一个子循环比较完，都会把一个最大的元素放到有序的空间内（抽象）；
       且有序的空间是在数组的后边
    4. 双层for循环之间的关系 是被放到有序列表的元素就不在参与循环了，即
      for i in range(len(nums) -1):
        for j in range(len(nums)-i-1):
    
    5. 总结：
        在无序区间内两个元素的比较并交换，且有序空间在右边，依次先出从右到左的从大到小的元素
    
"""


def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


"""
选择排序
    1. 基本原理：依次在无序区间中遍历找到最小元素，然后将最小元素与无序区间中的第一位交换;
    
    2. 思路：
       a. 同样也是需要两个元素的比较，但此时可以不是相邻的两个元素；
       b. 两个元素比较完，不会立马进行交换，而只是记录最小元素的索引；
       c. 有序空间在前，无序空间在后，且是从小到大，因此每一轮比较完，都是将最小的元素放在无序区间的第一位，并且，并入
          有序空间的最后一位；
    
    空间复杂度：O(n^2)
    空间复杂度：O(1)
    
    3. 总结：
       跟冒泡排序对比，性能优化点在，依旧是在无序区间内两个元素的比较，但是没有进行交互的，只是记录了索引
       且有序空间在左边，依次先出从左到右的从小到大的元素；

    
"""


def select_sort(nums):
    for i in range(len(nums) - 1):
        # 默认记录无序区间的索引，并认为是最小的
        min_index = i
        for j in range(i + 1, len(nums)):
            # 从无序区间的第二位元素开始和min_index位置的数据进行比较，
            # 如果发现j元素要小于min_index则进行min_index的重新复制
            if nums[j] <= nums[min_index]:
                min_index = j
            # 本轮循环完，做真实元素的交换
        nums[i], nums[min_index] = nums[min_index], nums[i]


"""
插入排序
    1. 基本原理：依次从无序区间选择一个元素，插入到有序区间的正确为止，直到无序区间的所有元素都被插入到
       有序区间；
    
    2. 思路：
        选择无序区间的第一个元素作为待插入元素，将其保存在临时变量，然后从有序区间的最后一个元素开始比较，
        若大于待插入元素，则将其后移一位，然后继续和前一位比较，直到找到正确的位置，将元素插入即可；
        
    3. 复杂度
       时间复杂度：O(n^2)
       空间复杂度：O(1)
    
    3. 总结：
        跟冒泡排序对比，插入排序是，使用待排序的元素，***在有序的区间***内进行比较和交换的；
        且有序空间在左边，依次出现从左到右的从小到大的元素；


"""


def insert_sort(nums):
    """插入排序"""
    # 第一个元素已经作为有序空间内的一员，所以要从第二元素开始，即range(i,len(nums))
    for i in range(1, len(nums)):
        # 在有序空间内，从最大的元素开始比较
        for j in range(i, 0, -1):
            # 如果，待排序元素，比有序空间里的元素大，则break，即不进行交换
            if nums[j] >= nums[j - 1]:
                break
            # 如果，待排序元素，比有序空间里的元素小，则进行交换
            nums[j], nums[j - 1] = nums[j - 1], nums[j]


"""
归并排序：
    1. 思路：
     向将一个数组，递归的分割成无数个数组，然后再将数组通过合并两个有序的函数，递归合并
     将两个有序的列表，取各自最小的元素进行比较，每次都将两者中最小的一个，移到临时数组中；
    
    2. 

"""

#归并
def merge_sort(left, right):
    """归并排序：合并两个有序的数组，且是从小到大的"""
    nums = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums.append(left[i])
            i += 1
        else:
            nums.append(right[j])
            j += 1
    nums += left[i:]
    nums += right[j:]
    return nums

#拆分+调用归并
def mergesort(nums):
    pass