"""
1. python是解释型语言，除了语法错误之外，其余的异常都是在执行的时候爆出；

"""
##=============try except==============
# try:
#     #resut = 3 / 0
#     resut = 3 / 1
#     print("running...")
# except:
#     print("error")
# print("end...")
#
# ##except匹配输出
# try:
#     result = 3 / 0
# except ZeroDivisionError as e:
#     print(e)
# except (RuntimeError, TypeError,NameError) as e:
#     print(e)
# except Exception as e:
#     print(e)
# # except:
# #     print("Unexpected error")
# else:
#     print(result)
# finally:
#     print("finally...")
# print("END。。。")

# =================================异常抛出============================
"""
raise:异常类型("异常描述")
"""
# def int_add(x,y):
#     if isinstance(x ,int) and isinstance(y,int):
#         return x+y
#     else:
#         raise TypeError("参数类型错误")
# print(int_add(1,2))
# # print(int_add(1,"2")) # 报错

"""
自定义异常

1. 复习：
    __str__() ： 定义了对类的实例调用 str() 时的行为

"""


class MyException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


# try:
#     raise MyException(1)
# except TypeError as e:
#     print("触发自定义异常：", e)

# try:
#     raise MyException(1)
# except MyException as e:
#     print("触发自定义异常：", e)

#异常的传递
# try:
#     try:
#         try:
#             print(1 / 0)
#         except NameError as e:
#             print("第三层", e)
#     except TypeError as e:
#         print("第二层", e)
# except Exception as e:
#     print("第一层", type(e), e)



# =================================断言 assert============================
"""
assert 用于判断一个表达式，在表达式条件为False的时候出发异常，常用语调试程序
assert 表达式 [,异常描述]
    等价于：
if not 表达式：
    raise AssertionError([异常描述])
"""
# def int_add(x,y):
#     assert isinstance(x,int) and  isinstance(y,int),"参数类型异常"
#     return x+y
# int_add(1,"") #报错

# =================================关键字============================
"""
1. with的使用 ???
# with expression as variable:
#     代码块
使用 with 关键字系统会自动调用 f.close() 方法， with 的作用等效于 try-except-finally 中的 finally 子句 语句
"""
#with
try:
    # with open('/Users/wfz/MyJob/MyCode/llm/my_study_llm_training/data/test2.txt',"w") as f:
    with open('/Users/wfz/MyJob/MyCode/llm/my_study_llm_training/data/test2.txt') as f:
        f.write("我是谁")
finally:
    print("文件关闭",f.close())

##===常见的异常===
"""
1. BaseException: 所有内置异常的基类，不被用户继承；
2. Exception: 所有内置的非系统退出类异常都派生此类，可用户自定义继承；
3. ArithmeticError: 此基类用户派生针对于各种算术类错误引发的异常；
4. BufferError: 当缓冲区相关的操作无法执行时将被引发；
5. LookupError: 此基类用户派生 映射或序列所使用的键或索引无效时引发的异常：IndexError ,KeyError
                 可通过codecs.lookup直接引发
6. AssertionError: 当assert语句失败时被引发；
7. AttributeError: 当属性引用或者赋值是被引发；
8. IndexError:
9. KeyError:
10. KeyboardInterrupt:
11. MemoryError:
12. NameError:


"""

