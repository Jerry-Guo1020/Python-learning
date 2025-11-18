class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.fuel = 100
    
    def get_decriptive_name(self):
        return f"{self.year} {self.make} {self.model}"
    
    def check_fuel(self):
        print(f"当前的油量：{self.fuel}%")
        
    def update_fuel(self, new_fuel):
        if 0 <= new_fuel <= 100:
            self.fuel = new_fuel
        else:
            print("不对")
            
    def drive(self, distance):
        fuel_consumed = distance / 10
        if self.fuel >= fuel_consumed:
            self.fuel -= fuel_consumed
            print(f"车子行驶了{distance}km")
        else:
            print("油量不足")
            
# 方法三 通过类的内部分方法进行修改
my_car_plus = Car("beaz", "s680", 2025)
my_car_plus.update_fuel(50)
my_car_plus.check_fuel()
my_car_plus.drive(100)
my_car_plus.check_fuel()

