import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)
    
    def move(self):
        self.x -= 1
        print("当前我的位置是：", self.x, self.y)

class GoldFish(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        Fish.__init__(self)
        self.hungry = True
    
    def eat(self):
        if self.hungry:
            
            print("吃货的梦想就是天天有的吃")
        else:
            print("饱了")