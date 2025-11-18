# Class

# 1、请补全下面的 Dog 类，使其具有 name 和 age 属性，以及 bark() 方法（打印“汪汪！”）

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("汪汪！")

# 2、创建一个 Dog 的实例，名字为“猪猪”，年龄为3岁，并调用它的 bark() 方法。

d = Dog("猪猪", 3)
print(f"狗狗的名字是：{d.name}")
print(f"狗狗的年龄是：{d.age}")
d.bark()

 
class Car:
    def __init__(self, make, model, year):
        """加入车的属性"""
        self.make = make
        self.model = model
        self.year = year
        # 按照要求加入油量，默认属性
        self.fuel = 100
    
    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"
    
# 3、为 Car 类添加一个默认属性 fuel = 100，并编写一个 check_fuel() 方法，打印当前油量。

    def check_fuel(self):
        print(f"当前油量：{self.fuel}%")

# 4、请写出三种修改 Car 实例的 fuel 属性的方式：

# 先新建一个示例
my_car = Car("benz", "s680", 2025)
my_car.check_fuel()

print("方法一：直接修改属性")
my_car.fuel = 80
my_car.check_fuel()

print("方法二")
def set_fuel(car_instance, value):
    car_instance.fuel = value
set_fuel(my_car, 65)
my_car.check_fuel()

# 7、创建一个 Battery 类，具有 size 属性和 describe() 方法。
class Battery():
    def __init__(self, size=75):
        self.size = size
    
    def describe(self):
        print(f"这一辆车有一个{self.size}kwh的电池")
        

# 5、创建一个 ElectricCar 类，继承自 Car，并添加一个特有属性 battery_size = 75。

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # 8、在 ElectricCar 中使用 Battery 实例作为属性。
        self.battery = Battery()

# 6、在 ElectricCar 中重写 get_descriptive_name() 方法，使其返回值包含“电动”字样。
    def get_descriptive_name(self):
        long_name = super().get_descriptive_name()
        return f"电动{long_name}"

     # 重写 check_fuel 方法，因为电动车没有油量
    def check_fuel(self):
        print("电动汽车没有油箱！")
        
# --- 测试 ElectricCar ---
my_tesla = ElectricCar("Tesla", "Model S", 2023)
# 调用重写后的方法
print(my_tesla.get_descriptive_name()) # 输出: 电动 2023 Tesla Model S
# 调用继承自父类但未被重写的方法
my_tesla.check_fuel() # 输出: 电动汽车没有油箱！
# 调用组合的 Battery 对象的属性和方法
print(my_tesla.battery.size) # 输出: 75
my_tesla.battery.describe() # 输出: 这辆车有一个 75-kWh 的电池。


# 9、将 Car 和 ElectricCar 分别放在 car.py 和 electric_car.py 中，并在主程序中导入并使用它们。
 
# 10、动物园系统 设计以下类：

# Animal：基类，有 name 和 sound 属性，以及 make_sound() 方法。 Lion、Elephant：继承自 Animal，重写 make_sound()。 Zoo：包含多个动物实例，可以添加动物并让所有动物一起叫。