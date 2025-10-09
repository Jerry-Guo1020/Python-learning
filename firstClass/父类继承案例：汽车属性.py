class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
    
    def read_odomter(self):
        print(f"这个车子有{self.odometer_reading}的里程哦")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("你不能回滚里程表")
    
    def increment_odometer(self, miles):
        self.odomter_reading += miles


if __name__ == "__main__":
    my_car = Car("benz", "s480", 2025)
    print(my_car.get_descriptive_name())

    print(my_car.read_odomter())

class Car:
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

my_leaf = ElectricCar("haha", "xixi", 2024)
print(my_leaf.get_descriptive_name())