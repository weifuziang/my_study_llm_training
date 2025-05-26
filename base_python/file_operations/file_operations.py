#===================================文件操作==========================
"""
r: 只读，文件不存在，报错；
rt: 读取文件中的整行
w: 写入，写入前清空原有数据，文件不存在会创建文件；
a: 追加写入，文件不存在会创建；
x: 创建文件并写入，若文件存在会报错；
b: 以二进制打开，用于非文本文件，如图片；
t: 以文本模式打开；
+：能读写；
"""
import os

# f = open("../../data/test.txt", "w")
# f.write("hello world \nworld count")
# f.close()
# fr = open("../../data/test.txt","r")
# print(fr.read())
# fr.close()
#
# fr5 = open("../../data/test.txt","r")
# print(fr5.read(2))
# fr5.close()

#readline([size]) 读取文件中的整行，可以通过size设置读取数据的长度
# fr6 = open("../../data/test.txt","rt")
# print(fr6.readline())
# print(fr6.readline(6))
# print(fr6.readline(2))
# fr6.close()

#readlines([size])读取所有行并返回列表，若给定size>0,返回总和大约为size字节的行，实际读取值可能大于size
#执行了readlines()，再执行readlines()会接着上一次的位置继续去读；
# f = open("../../data/test.txt","r",encoding="utf-8")
# # print(f.readlines())
# # print(f.readlines(2))
# print(f.seek(2,0))
# print(f.readline())
# print(f.seek(2,0))
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
# f.close()
#
# # os.rename("../../data/test.txt","../../data/test.txt")
# print(os.getcwd())
# print(os.path.abspath("../../data/test.txt"))
# print(os.path.exists("../../data/test.txt"))

#遍历递归目录
# for root,dirs,files in os.walk(os.getcwd()):
# for root,dirs,files in os.walk("../../../"):
#     print(root)
#     print(dirs)
#     print(files)

# 拷贝文件

fr = open("../../data/test.txt", "rb")
fw = open("../../data/test2.txt", "wb")
content = fr.read(1024)
while content:
    fw.write(content)
    content = fr.read(1024)
fw.close()
fr.close()



