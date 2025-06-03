###===并发与并行===
"""
并发： 单个CPU处理多个任务，各个任务交替执行一段时间，一个cpu对应多个任务；
并行： 多个CPU同时执行多个任务，一个cpu对应一个任务；
"""
import multiprocessing
import os

###===多进程===
"""
"""
#Linux or Unix
print(os.fork())

#跨平台
multiprocessing.Process().start()
