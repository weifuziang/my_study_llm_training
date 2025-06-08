###===正则表达式===
"""
正则表达式（regular expression，常简写为regex、regexp或re），是一种用于匹配和操作文本的强大工具，
它是由一系列字符和特殊字符组成的模式，用于描述要匹配的文本模式。
正则表达式可以在文本中查找、替换、提取和验证特定的模式
"""
###===re模块===
import re

###===表示字符===
"""
.   --> 匹配除 \r,\n之外的任何单个字符。要匹配包括 \r ,\n在内的任何字符，请使用(.|\r|\n)的模式；
\d  --> 匹配一个数字字符。等价与[0-9]
\D  --> 匹配一个非数字字符。等价与[^0-9]
\w  --> 匹配包括下划线的任何单词字符。等价于[A-Za-z0-9]
\W  --> 匹配任何非单词字符。等价于 [^A-Za-z0-9]
\s  --> 匹配任何空白字符，[\f\n\r\t\v]
\S  --> 匹配任何非空白字符。等价于[^\f\n\r\t\v]
[xyz] --> 匹配所包含的任意一个字符。如[abc]可以匹配"plain"中的"a"
[^xyz] --> 匹配未列出的任意字符；
[a-z] --> 字符范围，匹配在Unicode编码表指定范围内的任意字符。
"""

###===表示数量===
"""
*  --> 匹配前面的子表达式零次或者多次。等价{0,}
+  --> 匹配前面的子表达式一次或者多次。等价{1,}
?  --> 匹配前面的子表达式零次或者一次，等价{0,1}
{n}  --> n是非负数，匹配确定的n次。eg: o{2} 不能匹配”Bob“中的”o“,但是能匹配”food“中的两个”o“
{n,} --> 至少匹配n次。
{n,m} --> 其中n<=m 最少匹配n次且最多匹配m次；
?  --> 非贪心量化：当该字符紧跟在任何一个其他重复修饰符（*，+，?，{n}，{n,}，{n,m}）后面时，匹配模式是非贪婪的。
       例如对于字符串“oooo”，o+? 将匹配单个“o”，而 o+ 将匹配所有“o”
"""

###===表示边界===
"""
^ --> 匹配字符串的开始位置；
$ --> 匹配字符串的结束位置；
\b --> 匹配一个单词边界，也就是指单词和空格间的位置
\B --> 匹配非单词边界
"""

###===匹配分组===
"""
x|y  --> 匹配 x 或者 y
(pattern) --> 匹配pattern并获取这一个匹配的字符串
(?P<name>pattern) --> 分组所匹配到的字符串可以通过符号分组名称name来访问；
(?P=name) --> 引用一个命名组合；
\num --> 向后引用一个字符串，该字符串与正则表达式的第num个用括号围起来的子表达式匹配。其中num从1开始。eg：
         (.)\1 匹配两个连续的相同字符；
"""

###===原始字符串
"""
如果在字符串前面添加一个r 表示原始字符串，忽略转义。
"""
import re
text = "abcdef123456"
# print(re.search(r"\w+", text))
# print(re.search("\w+", text))

###===案例===
###匹配手机号
test = [
    "13812345678",  # 合法
    "11456817239",  # 非法
    "19912345678",  # 合法
    "17138412356",  # 合法
    "1234567890",  # 非法
    "14752345673",  # 合法
    "1800123456",  # 非法
]
#匹配以1开头，第二位是3，4，5，7，8，9，后面是9位数字
# pattern = r"^1[345789]\d{9}$"
# for i in test:
#     print(f"{i:20}{"合法" if re.match(pattern, i) else "非法"}")
###匹配邮箱
import re

test = [
    "example@example.com",
    "user.name@subdomain.example.co",
    "username@.com",
    "@missingusername.com",
    "-dasd@qq.com",
]
# 匹配邮箱
# pattern = r"[\w!#$%&'*+-/=?^`{|}~.]+@[\w!#$%&'*+-/=?^`{|}~.]+\.[a-zA-Z]{2,}$"
# for i in test:
#     print(f"{i:40}{"合法" if re.match(pattern, i) else "非法"}")
###===网页中获取标签===
test = """<link rel="alternate" hreflang="zh" href="https://zh.wikipedia.org/wiki/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F">
<link rel="alternate" hreflang="zh-Hans" href="https://zh.wikipedia.org/zh-hans/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F">
<link rel="alternate" hreflang="zh-Hans-CN" href="https://zh.wikipedia.org/zh-cn/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F">
<link rel="alternate" hreflang="zh-Hans-MY" href="https://zh.wikipedia.org/zh-my/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F">
<link rel="alternate" hreflang="zh-Hans-SG" href="https://zh.wikipedia.org/zh-sg/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F">
<link rel="alternate" hreflang="zh-Hant" href="https://zh.wikipedia.org/zh-hant/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F">
<link rel="alternate" hreflang="zh-Hant-HK" href="https://zh.wikipedia.org/zh-hk/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F">
<link rel="alternate" hreflang="zh-Hant-MO" href="https://zh.wikipedia.org/zh-mo/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F">
<link rel="alternate" hreflang="zh-Hant-TW" href="https://zh.wikipedia.org/zh-tw/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F">
<link rel="alternate" hreflang="x-default" href="https://zh.wikipedia.org/wiki/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F">"""
# pattern = r"href=\"(.+?)\""
# for i in re.findall(pattern,test):
#     print(i) #此时只打印出来了()里的内容

###===替换文本中的所有数字为对应的词===
import re
test = "I have 2 apples and 3 oranges."
num_map = {"1":"one","2":"two","3":"three"}
print(re.sub(r"\d",lambda x:num_map[x.group(0)],test))

