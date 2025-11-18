
from car import Car 

class Battery:
    """模拟电动汽车电池"""
    def __init__(self, size=75):
        self.size = size

    def describe(self):
        print(f"这辆车有一个 {self.size}-kWh 的电池。")

class ElectricCar(Car):
    """Car的子类，代表电动汽车"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def get_descriptive_name(self):
        long_name = super().get_descriptive_name()
        return f"电动 {long_name}"

    def check_fuel(self):
        print("电动汽车没有油箱！")
