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
    #没有找到目标元素
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
    2. 比较完要进行交换操作；
    3. 比较的次数 n * n 所以需要双层for循环，在每一个子循环比较完，都会把一个最大的元素放到有序的列表内（抽象）；
    4. 双层for循环之间的关系 是被放到有序列表的元素就不在参与循环了，即
      for i in range(len(nums) -1):
        for j in range(len(nums)-i-1):
    
"""

def bubble_sort(nums):
    for i in range(len(nums) -1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
