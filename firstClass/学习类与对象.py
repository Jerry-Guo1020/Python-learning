# 什么是类： 方法+属性

# 使用aaa的类
class aaa:

    # 使用ball方法
    def ball(self, name):     # 使用self的原因是：当一个对象被方法调用的时候，使用self的这个约定的形参，让Python知道“我现在正在给哪一个对象干活”
        self.name = name
    
    # 使用kick的方法
    def kick(self):
        print(f"大家好我是{self.name}")  #使用f-string来进行正确输入名字

a = aaa()
a.ball("lanqiu")

# print(a.kick()) 这个是错误的 因为kick() 里面已经有print()了
a.kick()



# 开始学习 _init_ 方法：

class bbb:
    def __init__(self, name2):
        self.name2 = name2
    
    def kick2(self):
         print(f"大家好我是{self.name2}")  #使用f-string来进行正确输入名字

b = bbb("西瓜")


b.kick2()