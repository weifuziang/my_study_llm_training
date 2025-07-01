"""
常用的算法
"""
# from http.cookiejar import lwp_cookie_str

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
                break  # 排过序的就不再循环了
            # 如果，待排序元素，比有序空间里的元素小，则进行交换
            nums[j], nums[j - 1] = nums[j - 1], nums[j]


"""
归并排序：
    1. 思路：
     拆分：先将一个数组，递归的分割成无数个数组，然后再将数组通过合并两个有序的函数，递归合并
     合并：将两个有序的列表，取各自最小的元素进行比较，每次都将两者中最小的一个，移到临时数组中；
    
    2. 重点思路：
    拆分时，会有左右两个子递归，左右两个子递归代表了两组入栈和出栈，而且者两组出入栈是先后执行的，
    也就是说，当左边的子递归先完成了递送和回归的操作得到一个结果A，然后，再进行右边的子递归的递送和回归
    操作后，得到一个结果B，最后再一起处理结果A和结果B；
    
    debug一下，查看一下整个的递归过程
    
    3. 复杂度：
    时间复杂度：O(nlogn),
              x该算法的时间复杂度，主要取决于合并操作的循环次数,由于该算法用到了递归，故计算循环次数时，还需要考虑递归调用的总次数
              递归的过程就是二叉树和拆分和循环遍历，即时间复杂度为 树的层数logn * 每层的遍历次数n 
    空间复杂度：O(n),该算法在运行时，同一时刻只会有一个临时数组，所有只需考虑最大的临时数组占用的空间即可，
             显然临时数组的最大长度等于输入数组的长度。因此该算法的空间复杂度为O(n)

"""


# 归并
def merge(left, right):
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


# 拆分+调用归并
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    # 递归分割数组
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    # 合并已排序的子数组
    return merge(left, right)


# if __name__ == '__main__':
#     nums = [1,7,4,9,5,10,2,30,15,0,2]
#     print(merge_sort(nums))

"""
快速排序
    1. 基本原理：
        a. 依次按基准元素划分；
        b. 小于基准的放到左边，大于的放到右边；
        c. 左右双指针进行操作：先从右指针开始，因为你基准的开始是从左边拿的
    
    2. 核心思路：
       a. 初始基准元素直接用最左边了；
       b. 每一轮结束都需要把基准元素最终落到的那个索引返回；
       c. 为什么要用调用两次递归函数呢？原因是，上一轮返回的基准元素的索引mid，要进行下一轮循环时，如果只递归调用一次函数，
          那你到底是用left 还是用right呢？
       d. ***巧妙的一个点就是：在进行以基准元素为基准进行比较时，一般都是右边元素while比较，出现一个交换操作后，就进行左边元素的while比较；
                            是左右轮训，因为这样可以很好的记录和利用被交换元素之前的位置****；
    
    3. 时间复杂度：O(nlogn)
       空间复杂度：O(logn) ~ O(n)       


"""


def partition(nums, left, right):
    pivot = nums[left]
    while left < right:
        while left < right and nums[right] >= pivot:
            right -= 1
        # 左右交换：不会出现数据丢失，因为left已经被放到基准里了；
        nums[left] = nums[right]
        while left < right and nums[left] <= pivot:
            left += 1
        # 左右交换：不会出现数据丢失，因为left已经被放到基准里了；
        nums[right] = nums[left]
    nums[left] = pivot
    # 返回最终基准线的位置
    return left


def quickSort(nums, left, right):
    if left < right:
        mid = partition(nums, left, right)
        # 递归函数第一次调用
        quickSort(nums, left, mid - 1)
        # 递归函数第二次调用
        quickSort(nums, mid + 1, right)


# if __name__ == '__main__':
#     nums = [9, 4, 8, 6, 7,10,2,4,12,8,6,2,5,16,1]
#     quickSort(nums, 0, len(nums) - 1)
#     print(nums)

"""
堆排序
    1. 基本思路如下，
       a. 构建大顶堆: 自底向上依次堆化（从非叶子节点开始，而非叶子节点的计算： 数组长度为n,最后一个非叶子节点的索引为(n//2) - 1 ）
       b. 交换堆顶和堆底元素: 交换后大顶堆结构被破坏
       c. 重新调整堆(重新堆化)：自顶向下堆化
       d. 重复上面b，c的步骤;
       
    2. 复杂度
        时间复杂度：O(nlogn)，与其他O(nlogn)的排序算法（归并、快排）对比，堆排序的常数因子比较大，因此在某些情况喜爱效率比较低；
        空间复杂度：O(1) 
    
    
    3. 总结：
       a. 大顶堆以数组形式的存储实际上就是广度优先遍历的顺序存储；
       b. 构建大顶堆时，非叶子节点的索引计算是，按照大顶堆首次以数组形式存储时的(n//2) - 1
       c. 无论是自底向上依次堆化，还是自顶向下的的堆化，其实都是一次对堆的根节点、左节点以及有节点的大小比较，将最大的元素放到根节点而已；
       


"""


def heapify(nums, n, i):
    """
    此方法本身就是自顶向下的堆化，因为会递归调用heapify
    :param nums: 列表或者数组
    :param n: 堆内的元素个数
    :param i: 开始堆化的索引
    :return:
    """
    # 假设i最大
    largest = i
    # 拿到左子节点的索引
    left = 2 * i + 1
    # 拿到右子节点的索引
    right = 2 * i + 2
    # 中、左、右节点的大小比较，即堆化的过程
    if left < n and nums[left] > nums[largest]:
        largest = left
    if right < n and nums[right] > nums[largest]:
        largest = right
    # 判读largest发生了变化后
    if largest != i:
        nums[largest], nums[i] = nums[i], nums[largest]
        heapify(nums, n, largest)


def heapSort(nums):
    n = len(nums)
    # 构建大顶堆，从最后一个非叶子节点（n//2 - 1），逐个递减
    # 此range()的递减循环就是自底向上的堆化 其实每次循环只调用了一次heapify()函数，即无递归
    # 堆的数组化存储中，堆靠近底部的元素会存在数组的最靠后的位置）
    # 问题点 range的最后落脚索引是 -1 ，是因为可以递归到0 ， 即 2 * 0 +1  ；2*0+2
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)
    # 依次交换堆顶和堆底元素
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        # 被破坏后的堆，自顶向下堆化构建，会多次递归调用
        heapify(nums, i, 0)
    return nums


# if __name__ == '__main__':
#     nums = [5, 4, 3, 10, 11, 22, 7, 6, 2, 1]
#     print(heapSort(nums))

"""
分治算法：
    1. 基本思路： 将原问题递归的分解为若干个规模较小、相互独立切性质相同的子问题，直到子问题足够的简单，简单到可以直接求解，然后再返回结果逐个解决上层问题；
                 操作过程为：可分解  --> 存在基本情况  --> 可合并
    2. 连通性：归并排序 和 快速排序算法就是分治思想的典型应用
"""
# 汉诺塔问题（ 作为简单了解）
"""
f(n-1): 
        a. 将source的n-1个元素 平移到缓冲区buffer，其间会借助于target； 
        b. 将缓冲区buffer的之前移动过来的n-1元素，平移到target；
        
f(n): 将source移走n-1个元素剩下的元素n,全部移动到target
  
"""


def print_abc(a, b, c):
    """打印3个柱子"""
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print()


def hanota(n, source, target, buffer):
    # 只有一个盘子时，直接从源柱子移动到目标柱子
    if n == 1:
        target.append(source.pop())
        return

    # 1. 将 n-1 个盘子从源柱子移动到缓冲柱子
    hanota(n - 1, source, buffer, target)
    print_abc(source, target, buffer)

    # 2. 将第 n 个盘子从源柱子移动到目标柱子
    hanota(1, source, target, buffer)
    print_abc(source, target, buffer)

    # 3. 将 n-1 个盘子从缓冲柱子移动到目标柱子
    hanota(n - 1, buffer, target, source)
    print_abc(source, target, buffer)


# if __name__ == "__main__":
#     n = 3
#     a = list(range(n, 0, -1))
#     b = []
#     c = []
#     hanota(n, a, c, b)

# Karatsuba（卡拉楚巴） （作为简单了解）
"""
Karatsuba（卡拉楚巴）大整数乘法算法  
    1. 基本原理： 一种高效的大整数乘法算法，关键思想是通过分治法减少了传统乘法的计算量，从而降低了***乘法的时间复杂度
    
    2. 基本公式
        a. 表达式：A×B --> C = A×B = (10m×A1+A0)×(10m×B1+B0) = 102m×A1×B1 + 10m×(A1×B0+A0×B1) + A0×B0
        b. 抽象：
            A1×B1：高位部分的乘积。
            A0×B0：低位部分的乘积
            A1×B0+A0×B1：混合部分，涉及到高位与低位的交叉乘积。
    
        c. 程序化
            令z0=A0×B0
            令z1=(A1+A0)×(B1+B0) 
            令z2= A1×B1
            此时结果C=102m× z2 + 10m×(z1−z2−z0) + z0
            
    3. 高效优化的点：
            Karatsuba通过减少了1个乘法操作，将原本的4次乘法运算变成了3次乘法运算，时间复杂度：T(n)=3T(n2)+O(n)，O(nlog3)≈O(n1.585)
    

"""


def karatsuba(x, y):
    """卡拉楚巴算法"""
    # 将 x 和 y 转换为字符串
    x_str, y_str = str(x), str(y)
    n = max(len(x_str), len(y_str))

    # 如果存在负数，将其转换为正数再调用 karatsuba
    if x_str[0] == "-":
        return -karatsuba(-x, y)
    if y_str[0] == "-":
        return -karatsuba(x, -y)

    # 如果只剩1位则返回乘积
    if n == 1:
        return x * y

    # 确保数字长度一致
    x_str = x_str.zfill(n)
    y_str = y_str.zfill(n)

    # 计算分割点
    m = n // 2

    # 将数字划分为高位部分和低位部分
    high1, low1 = int(x_str[:-m]), int(x_str[-m:])
    high2, low2 = int(y_str[:-m]), int(y_str[-m:])

    # 递归调用 karatsuba
    z0 = karatsuba(low1, low2)
    z1 = karatsuba(low1 + high1, low2 + high2)
    z2 = karatsuba(high1, high2)

    return pow(10, 2 * m) * z2 + pow(10, m) * (z1 - z2 - z0) + z0


# if __name__ == "__main__":
#     karatsuba1 = karatsuba(21, 10)
#     print(karatsuba1)

"""
动态规划
1. 基本概念：也是将原问题拆分为若干子问题，然后递归求解子问题，最后在组合子问题的解进而得到原问题的解；
   对比：分治算法解决的问题，子问题通常是相互独立；而动态规划解决的问题，子问题具有重叠现象，所谓重叠现象，是指不同的子问题会有相同的子子问题；

2. 现实问题：
    a. 爬楼梯问题：爬有n个台阶的楼梯，每次可以爬1或2个台阶。有多少种不同的方法可以爬到楼顶？
"""
###应用---爬楼梯问题
"""
思考过程：由于每次只能1一个或者两个台阶，所以第n个台阶可能就是从第n-1个台阶爬1阶上来的；
        也可能是从第n-2个台阶爬2阶上来的，所以爬到第n阶的方法数就等于爬到第n-1阶的方法数加上爬到第n-2的方法数；
        故可以得到状态转移方程：f(n)=f(n-1)+f(n-2)
"""
# def climb(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return climb(n - 1) + climb(n - 2)

###应用---最大的连续子数组之和
"""
思考过程：用f(x)表示以x结尾的最大子数组之和，考虑处于位置i时，有两种选择：
        a. 与之前的子数组组成连续子数组，此时子数组之和f(i)=f(i-1) + nums[i]
        b. 中断连续，从头开始一个新的连续子数组，此时f(i)=nums[i]
        c. 得到的状态方程：f(i)=max(f(i-1) + nums[i],nums[i])
"""


def max_subarray(nums):
    result, f = nums[0], 0
    for i in nums:
        # 连续子数组之和若小于0，则中断连续
        if f < 0:
            f = 0
        # 累加连续子数组之和
        f += i
        # 更新最大值
        if result < f:
            result = f
    return result


# if __name__ == '__main__':
#     nums = [-2, -1, -3, -4, -1, 1, -2, -5, -4]
#     print(max_subarray(nums))

"""
0-1背包：
    1. 题目：0-1背包问题是一个经典的动态规划问题。其基本描述是：给定一组物品，每个物品都有一个重量和一个价值，在背包容量有限的情况下，如何选择物品放入背包，使得背包中物品的总价值最大化，且总重量不超过背包的容量
        	物品：有n个物品，每个物品i的重量为weight[i]和价值value[i]。
        	背包容量：背包可以承载的最大重量为W。
        	目标：选择若干物品放入背包，使得总重量不超过W，且总价值最大。
        
        注：每个物品只能放一次

    2. 解题思路：
    
             相关因素：物品、背包；物品的数量 物品的重量 物品的价值 背包的容量；
             
             定义一个二维数组dp[i][j] 表示前i个物品中，总重量不超过j的情况下，能够取得的最大价值
             a. i表示考虑第i个物品；
             b. 表示背包当前容量为j;
             
             状态转移
             a. 对于每个物品i,有两个选择：
             c. 不选择第i个物品，此时最大价值就是前i-1个物品在容量j下的最大价值，即dp[i-1][j]
             d. 选择第i个物品：此时背包剩余容量为j-weighti ,所以最大价值为valuei = dp[i-1][j-weighti],前提是j>=wi
             状态转移方程：dp[i][j]=max(dp[i-1][j],dp[i-1][j-weighti]))
             
    3. 优化点： 当i=1 ,j=1,2,3时， 其中，j=2,3循环是无意义的！ 因为在i=1(只有一个物品的情况下)，把背包容量扩大，针对于0-1背包问题是没有意义的；
    
    4. 总结：
            a. 现有逻辑思路，然后将逻辑思路转化为数理逻辑，最后再转化为代码实现；
            b. 核心逻辑就是：抽象出当前这物品i 放与不放的抉择，在什么条件下放什么的逻辑过程； 
                当前物品i的前一次背包状态,即价值: dp[i-1][j]
                 当前物品i,放进去后，本次背包的状态，即价值：valuei + dp[i][j-weighti]
    5. 不理解的点???：dp[i][j-weighti]中的j-weighti ???
       拉个屎之后理解：j-weighti其实就是，总的背包容量减去当前物品i的重量之后，剩下的容量还够容纳之前被放过的物品i-1位置的容量；
                    之所以是i-1的原因是，执行下面的代码可以看到，i-1那一类其实是记录了不同背包容量j的物品价值；
               
            
    
"""
def knapsack(weights, values, W):
    n = len(weights)
    # 初始化二维数组dp，dp[i][j]表示前i个物品中，背包容量为j时的最大价值
    dp = [[0] * (W + 1) for _ in range(n)]

    # 每次增加一个可选物品，增加物品后遍历一次背包重量
    for i in range(n):
        for j in range(1, W + 1):
            # 如果当前物品放的进背包，进行比较
            if weights[i] <= j:
                dp[i][j] = max(dp[i - 1][j], values[i] + dp[i - 1][j - weights[i]])
            # 如果当前物品放不进背包，使用上轮相同j的状态
            else:
                dp[i][j] = dp[i - 1][j]

            print(f"前{i + 1}个物品，背包容量为{j}时")
            for row in range(len(dp)):
                print(dp[row])

    return dp[n - 1][W]

if __name__ == "__main__":
    weights = [1, 2, 2]  # 物品的重量
    values = [9, 2, 20]  # 物品的价值
    W = 3  # 背包的最大容量
    print(knapsack(weights, values, W))

