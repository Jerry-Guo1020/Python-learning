# 基类 Animal
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} 发出声音: {self.sound}")

# 子类 Lion
class Lion(Animal):
    def __init__(self, name):
        # 狮子的声音是固定的，所以直接传入 "吼叫"
        super().__init__(name, "吼叫")

    def make_sound(self):
        # 重写方法，使其更具特色
        print(f"{self.name}，丛林之王，正在大声咆哮！")

# 子类 Elephant
class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name, "鸣叫")

    def make_sound(self):
        print(f"{self.name}，这头大象，正在用长鼻子高声鸣叫！")

# 管理类 Zoo
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = [] # 用一个列表来存储动物实例

    def add_animal(self, animal):
        """向动物园添加一个动物"""
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f"欢迎 {animal.name} 来到 {self.name}！")
        else:
            print("抱歉，只能添加 Animal 类型的动物。")

    def all_make_sound(self):
        """让动物园里所有的动物一起叫"""
        print(f"\n--- {self.name} 开始热闹起来了！ ---")
        if not self.animals:
            print("动物园里还没有动物呢。")
            return
        for animal in self.animals:
            animal.make_sound() # 调用每个动物自己的 make_sound 方法

# --- 测试动物园系统 ---
# 1. 创建动物实例
leo = Lion("辛巴")
dumbo = Elephant("小飞")
parrot = Animal("波利", "你好！") # 创建一个基本的 Animal 实例

# 2. 创建动物园实例
my_zoo = Zoo("快乐动物园")

# 3. 添加动物到动物园
my_zoo.add_animal(leo)
my_zoo.add_animal(dumbo)
my_zoo.add_animal(parrot)
my_zoo.add_animal("一块石头") # 测试无效添加

# 4. 让所有动物一起叫
my_zoo.all_make_sound()
