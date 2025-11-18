
from car import Car 
from electric_car import ElectricCar 


my_beetle = Car("Volkswagen", "Beetle", 2019)
print(my_beetle.get_descriptive_name())
my_beetle.check_fuel()

print("-" * 20)


my_leaf = ElectricCar("Nissan", "Leaf", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe()
