
class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.fuel = 100
    
    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"
    
    def check_fuel(self):
        print(f"当前油量: {self.fuel}%")
