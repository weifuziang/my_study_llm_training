"""
项目重点说明：
1. 基础类的抽取；
2. 特定类的继承，方法的重写，父类方法的调用；
3. 类之间的交互，即为了后期具体实体对象之间的的交互做准备；

"""

class Birds:
    def __init__(self,name,color,skill_description):
        self.name = name
        self.color = color
        self.skill_description = skill_description
    def fly(self):
        print(f"{self.name} is flying.")
    def call(self):
        print(f"{self.name} is calling.")
    def use_skill(self):
        print(f"{self.skill_description} is being used.")

class RedBird(Birds):
    def __init__(self):
        super().__init__("红火","红色","撞击前方障碍物")
    def fly(self):
        print("红火以稳定的速度全速前进。。。")
    def call(self):
        print("红火发出 'wei 呀....'的叫声")

class YellowBirds(Birds):
    def __init__(self):
        super().__init__("小黄", "黄色", "瞬间加速，穿透薄障碍物")

    def fly(self):
        print("小黄快速向前飞行...")

    def call(self):
        print("小黄发出 '啾啾啾....' 的叫声")

# 定义蓝鸟子类
class BlueBirds(Birds):
    def __init__(self):
        super().__init__("小蓝", "蓝色", "分裂成三只小鸟，分散攻击")

    def fly(self):
        print("小蓝优雅地向前飞行...")

    def call(self):
        print("小蓝发出 '叽叽叽....' 的叫声")

class Obstacle:
    def __init__(self,name ,strength):
        self.name = name
        self.strength = strength
    def be_attacked(self,bird):
        print(f"{bird.name} 冲向了 {self.name}")
        bird.use_skill()
        # bird.fly()
        # bird.call()
        if isinstance(bird,YellowBirds):
            damage = 20
        elif isinstance(bird,BlueBirds):
            damage = 10
        elif isinstance(bird,RedBird):
            damage = 100

        self.strength -= damage
        if self.strength <= 0:
            print(f"{self.name} 被摧毁了")
        else:
            print(f"{self.name} 还剩余 {self.strength} 点强度")

if __name__ == "__main__":
    yellowBirds = YellowBirds()
    RedBirds = RedBird()
    blueBirds = BlueBirds()

    obstacle = Obstacle("木头堡垒", 100)
    obstacle.be_attacked(yellowBirds)
    obstacle.be_attacked(blueBirds)
    obstacle.be_attacked(RedBirds)
