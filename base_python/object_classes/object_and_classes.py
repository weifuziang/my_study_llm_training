# ======================面相对象之类和对象============================
"""
1. python 即支持面向过程的编程，也支持面向对象的编程
2. 面向过程：一种以过程为中心的编程方式，主要关心解决问题的步骤，并将这些步骤写成函数或者方法；
3. 面相对象：一种以对象为中心的编程方式，主要关注在解决问题的过程中涉及那哪些对象以及这些对象如何交互；
4. 类：
     1> 对大量对象共性的抽象；
     2> 创建对象的模板；
     3> 客观事物在人脑中的主观反映；
     4> 基本定义：

     类说明文档(用三引号引起来)
     类体
     类名一般使用大驼峰命名法
     类体可以包含类属性（类变量）、方法、实体属性（实例变量）等

     5> __init_() 方法：
     调用时机：在实例被创建之后，返回调用者之前；
     一般用来初始化一些数据，可以向init方法中传递参数；

     6> self 作为实例传参
     self代表类的实例自身。调用实例方法时，实例对象会作为第一个参数对传入，因此person.eat()时，
     相当于是调用了Person.eat(p)

     7> 方法
     方法分为：类方法（注解@classmethod）、静态方法(staticmethod)、实体方法

   对象：
     1> 在自然界中，只要是客观存在的事物都是对象；
     2> 类是抽象的，对象是对类的示例（Instance）,是具体的；
     3> 一个对象有自己的状态（属性）、行为（方法）和唯一标识（本质上指内存中所有创建的对象地址）；

"""


# class Person:
#     """人的类"""
#     home = "earth"  # 类属性（类变量）
#
#     @classmethod
#     def class_method(cls):  # 类方法：可以访问类和实体的属性; 被类和实体对象调用
#         print("类方法被调用")
#         print(cls.home)
#         print(cls.eat)
#
#     @staticmethod
#     def static_method():  # 静态方法：不访问实体属性和类属性；被类和实体对象调用
#         print("static_method")
#
#     def __init__(self, name, home=home):
#         self.age = 18  # 实体属性（实体变量）
#         self.name = name
#         self.home = home
#
#     def eat(self):  # 方法
#         print("eating......")
#
#     def drink(self):  # 方法
#         print("drinking......")
#
#     def eat_and_drink(self):
#         print(self.name)
#         print(self.age)
#         self.eat()
#         self.drink()


# 调用
# 类属性调用
# print(Person.home)
# print(Person.eat)
# print(Person.__doc__)

# 实体化
# person = Person("垣曲")
# print(person.home)
# print(person.age)
# print(person.name)
# person.eat()
# person.drink()

# p = Person("lisi","shanghai")
# p.eat_and_drink()
# print(p.age)
# print(p.name)
# print(p.home)
#
# #类名点属性可以修改类属性（类变量）
# Person.home = "yue_qiu"
# print(Person.home)

# 类方法调用
# print(Person.class_method())
# print(p.class_method())

# 静态方法调用
# p.static_method()
# Person.static_method()

# =========================特殊方法==================================
"""
1. __new__()
 对象实例化时的第一个调用的方法；
2.__init__()
 类初始化方法
3. __del__()
 对象的销毁器，定义了当对象呗垃圾回收时的行为，当引用计算==0时才会被销毁
4. __str__()
 定义了对类的实力调用str()时的行为
5. __repr__()
 定义对类的实例调用reper()行为，str() 和 repr() 最主要区别是前者输出人类可读内容，后者输出可以作为有效的
 python代码 ；
6. __getattribute__()
 属性访问拦截器，定义了属性被访问前的操作；
"""

##===动态给对象添加属性===
class Person1:
    home = "earth"
    def __init__(self, name=None):
        self.name = name
# p0=Person1("tian_qi")
# print(p0.home)
# p0.age = 33
# print(p0.age)

##===动态给类添加属性===
p = Person1("liu neng")
# print(p.name)
# Person1.age = 18
# print(Person1.age)


##===动态给对象添加方法===
"""
普通方法
"""
# def eat():
#     print("eating......")
# p.eat = eat()
# p.eat

"""
实例方法：被添加的方法需要传入self参数,且只绑定在当前对象上

"""
import types

def drink(self):
    print("drinking......")


# p2 = Person1("zhang san")
# print(p2.name)
# p2.drink = types.MethodType(drink, p)
# p2.drink()

##==动态给添加类方法
"""
添加类方法
"""
# @classmethod
# def come_from(cls):
#     print("come_from{}".format(cls.home))
#
"""
添加静态方法
"""
# def static_func():
#     print("static_func")
# Person1.come_from=come_from
# Person1.static_method=static_func
#
# Person1.come_from()
# Person1.static_method()

##===动态删除属性和方法===
"""
del 对象.属性
delattr(对象，属性名)
"""

##__slots__限制实例属性与实例方法
"""
1. 使用__slots__变量，来限制该类的实例能添加的属性，重点只限制对象的实例；
2. 类属性 类方法和静态方法还可以添加。不受限制
"""

# class Student():
#     __slots__=("name","age")
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def sleep(self):
#         print("{}  sleep".format(self.name))

# ps = Student("liu",30)
# ps.sleep()
# 对象属性添加是不可以的
# ps.eat="鸡蛋"
# print(ps.eat)
# 类属性添加是可以的
# Student.drink="喝水"
# print(Student.drink)
# ps = Student("liu",30)
# print(ps.name)

## ===================================面向对象之三大特性================================
"""
1. 封装
    1> 定义：将变量和函数，封装到类的属性和方法中；
    2> 作用：将一些细节私有化，只暴漏出必要的接口供调用者使用；
        私有化：
            单下划线（非公开API）:
            双下划线（名称改写）:私有属性、私有方法

2. 继承
    1> 子类不能继承父类的私用属性和私有方法，因为存在名称改写；
    2> 单继承 、多继承
    

3. 多态

"""

##===封装===
# class Person2:
#     age = 38
#     #私有属性
#     def __init__(self,name,age = 18):
#         self.__name = name
#         self.age = age
#     #获取私有属性的方法
#     def get_name(self):
#         return self.__name
#
#     #私有方法
#     def __private_method(self):
#         print("private method")
#
#     #私有方法调用
#
#     def get_something(self):
#         self.__private_method()
#
#     #@property注解: 将一个方法转化成属性来调用，即.方法名，不需要后面的"()"
#
#     @property
#     def sleep(self):
#         print(f"{self.__name} is sleeping")
#
#     #只读属性
#     #@property注解: 将私有属性去掉双下划线，作为方法的命名名称，方法中返回私用属性(即属性转方法,且将属性转成了只读属性)
#     @property
#     def name(self):
#         return self.__name
#
#     #读权限属性：setter
#     @name.setter
#     def name(self,name):
#         if name == "zhangsan":
#             print("不允许设置zhangsan")
#         else:
#             self.__name = name
#
#     #@property注解的名字不能和变量名一致，否则会出现死循环的问题
#     @property
#     def age(self):
#         return self.age
#
#
# person_ = Person2("liuliuliu",28)
# print(person_.get_name())
# # print(person_.__name) #报错
# print(person_.age)
# person_.get_something()
# # person_.__private_method() #报错
#
# person_.sleep
# print(person_.name)
# person_.name="gai liu zi"
# print(person_.get_name())
#
# person_.name="zhangsan"
# print(person_.get_name())
#
# print(person_.age)# 用@property 注解了age命名的方法，会直接报错

##===继承===
#单继承
# class Person:
#     """人类"""
#     home = "earth"
#     def __init__(self, name=None):
#         self.name = name
#     def drink(self):
#         print("drinking......")
#
# class YellowRace(Person):
#     """黄种人"""
#     color = "yellow"
#
# class WhiteRace(Person):
#     """白种人"""
#     color = "white"
#
# class BlackRace(Person):
#     """黑种人"""
#     color = "black"
#
# yellowRace = YellowRace("zhangsan")
# print(yellowRace.name)
# print(yellowRace.color)
# yellowRace.drink()

#多继承

# class Person:
#     """人的类"""
#
#     home = "earth"
#
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print("eating...")
#
# class YellowRace(Person):
#     """黄种人"""
#
#     color = "yellow"
#
#     def run(self):
#         print("runing...")
#
# class Student(Person):
#     """学生"""
#
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#
#     def study(self):
#         print("先吃在学...")
#         #父类中方法的调用
#         Person.eat(self)
#         super().eat()
#
#     #重写父类中的方法
#     def eat(self):
#         print("用勺子吃....")
#
#         print("studying...")
#     #重写父类中的__init__()方法: 使用super().__init__调取
#     # def __int__(self,name ,age,weight):
#     #     super().__init__(name)
#     #     self.age = 18
#     #     self.weight = 20
#
# class ChinesStudent(YellowRace,Student):
#     """中国学生"""
#     country="中国"


# student = ChinesStudent("张三","三年级")
# student.study()
# student.eat()
# print(student.country)
# print(student.color)
#
# #查看方法调用顺序
# print(ChinesStudent.__mro__)

#====================================多态===========================================
"""
1. 同一事物在不同场景下呈现不同状态；
"""
class Person2:
    def sleep(self):
        pass
    def running(self):
        pass

class Animal:
    def go(self):
        pass
    def eat(self):
        pass
class Dog(Animal):
    def go(self):
        print("跑。。。")
class Fish(Animal):
    def go(self):
        print("水里游。。。")

#将不同的实例传入，执行不同的方法
def go(animal):
    animal.go()
    animal.eat()
    # animal.running()
    # animal.eat()

dog = Dog()
fish = Fish()
go(dog)
go(fish)




