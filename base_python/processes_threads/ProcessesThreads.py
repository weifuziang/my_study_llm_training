###===并发与并行===
"""
并发： 单个CPU处理多个任务，各个任务交替执行一段时间，一个cpu对应多个任务；
并行： 多个CPU同时执行多个任务，一个cpu对应一个任务；
"""
import concurrent
import multiprocessing
import os
import time



###===多进程===
"""
"""
# Linux or Unix
# print(os.fork())

# 跨平台
# multiprocessing.Process().start()

# demon
# 向文件中写入数据
# def write_file():
#      with open("/Users/wfz/MyJob/MyCode/llm/my_study_llm_training/data/test3","a") as f:
#          while True:
#              f.write("hello world 111\n")
#              f.flush()
#              time.sleep(1)
# #从文件中读取
# def read_file():
#     with open("/Users/wfz/MyJob/MyCode/llm/my_study_llm_training/data/test3","r") as f:
#         while True:
#             time.sleep(0.1)
#             print(f.readline())
# #自定义Process子类创建进程
# class Worker(multiprocessing.Process):
#     def run(self):
#         print("进程id: ",os.getpid() , "\t 父进程id: ",os.getppid())

###===进程池===
# def func():
#     for i in range(10):
#         print(os.getpid())
#         time.sleep(0.5)
#
# def func2(list1):
#     for i in range(10):
#         list1.append(i)
#         print(os.getpid(),list1)
#
# import random
# #放数
# def func3(queue):
#     while True:
#         queue.put(random.randint(1,100))
#         time.sleep(random.random())
# #取数
# def func4(queue):
#     while True:
#         print("=" * queue.get())

###===多线程===
"""
1. 多线程是指在同一进程中同时执行多个任务
"""


# import time
# import threading
# def func5():
#     flag = 0
#     while True:
#         print(threading.current_thread().name, f"{flag}" * 5)
#         flag = flag ^ 1 #替换0和1
#         time.sleep(0.5)
#
# #自定义Thread子类创建线程
# class Worker1(threading.Thread):
#     def __init__(self,name):
#         super().__init__()
#         self.name = name

def run(self):
    flag = 0
    while True:
        print(f"\r{self.name}:{str(flag) * 5}", end="")
        flag = flag ^ 1
        time.sleep(0.2)


# 创建一个字进程用于写文件
# p1 = multiprocessing.Process(target=write_file)
# 创建一个子进程用于读文件
# p2 = multiprocessing.Process(target=read_file)
# p1.start()
# p2.start()

# for i in range(10000):
#     process = Worker()
#     process.start()
#     # process.join()

# 进程池
# process_num = 50
# pool = multiprocessing.Pool(process_num)
# for i in range(process_num):
#     #非阻塞式
#     pool.apply_async(func())
#     #阻塞
#     # pool.apply(func)
# #阻止后续任务提交到进程池？？？
# pool.close()
# #阻塞主进程？？？
# pool.join()
# print("end")

# 进程间不共享全局变量
# list1 = []
# p1 = multiprocessing.Process(target=func2,args=(list1,))
# p2 = multiprocessing.Process(target=func2,args=(list1,))
# p1.start()
# p2.start()
# p1.join()
# p2.join()
# print(os.getpid(),list1)

# 使用Queue通信
# queue = multiprocessing.Queue()
# p1 = multiprocessing.Process(target=func3, args=(queue,))
# p2 = multiprocessing.Process(target=func4, args=(queue,))
# p1.start()
# p2.start()
# p1.join()
# p2.join()

# 进程池之间使用Manager().Queue 通信
# queue = multiprocessing.Manager().Queue()
# pool = multiprocessing.Pool(3)
# pool.apply_async(func=func3, args=(queue,))
# pool.apply_async(func=func4, args=(queue,))
# pool.close()
# pool.join()

# 线程
# thread1 = threading.Thread(target=func5,name="线程1")
# thread2 = threading.Thread(target=func5,name="线程2")
# thread1.start()
# thread2.start()
# worker3 = Worker1("线程3")
# worker4 = Worker1("线程4")
# worker3.start()
# worker4.start()

###===线程池===
# def func6(tname):
#     global word
#     for i, char in enumerate(word):
#         word[i] = chr(ord(char) ^ 1)
#         print(f"{tname}: {word} \n", end="")
#     return word
#
# import concurrent.futures
# word = list("idmmn!vnsme")
# with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
#     future1 = executor.submit(func6, "线程1")
#     future2 = executor.submit(func6, "线程2")
#     future3 = executor.submit(func6, "线程3")
#     future4 = executor.submit(func6, "线程4")
# print("".join(word))

###===互斥锁===
"""
1. 某个线程要更改共享数据时，先将其锁定，此时其他线程不能更改。直到该线程释放资源，将资源的状态变成“非锁定”，其他的线程才能再次锁定该资源；
2. 互斥锁保证了每次只有一个线程进行写入操作，从而保证了多线程情况下数据的正确性；
"""
import time
import threading

"""
可以看到,如果sleep(0.1)开启，则最终结果并不是30。这是因为在修改 g_num 前，有0.01秒的休眠时间，某个线程延时后，CPU立即分配计算资源给其他线程。
此时0.01秒的休眠还未结束，这个线程还未将修改后的数据赋值给 g_num，因此其他线程获取到的并不是最新值，所以才出现上面的结果。
"""
# def func():
#     global g_num
#     for _ in range(10):
#         lock.acquire()
#         tmp = g_num + 1
#         time.sleep(0.1)  # 若开启sleep，则共享变量就会被其他线程重置
#         g_num = tmp
#         lock.release()
#         print(f"{threading.current_thread().name}: {g_num} \n", end="")
#
# if __name__ == '__main__':
#     g_num = 0
#     lock = threading.Lock()
#     threads = [threading.Thread(target=func, name=f"线程{i}") for i in range(3)]
#     [t.start() for t in threads]
#     [t.join() for t in threads]
#     print(g_num)

"""
GIL: Python 全局解释器锁（Global Interpreter Lock）是一个锁，同一时间只允许一个线程保持python解释器的控制权；
这意味着在任何时间点都只能有一个线程处于执行状态。执行单线程程序时看不到 GIL 的影响，但它可能是 CPU 密集型和多线程代码中的性能瓶颈。
GIL并不是Python的特性，它是在实现Python解析器（CPython）时所引入的一个概念。
"""

