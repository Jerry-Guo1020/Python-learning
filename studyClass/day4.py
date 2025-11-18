fruit_prices = {"apple": 5, "banana": 3, "orange": 4}
fruit_prices["grape"] = '6'
print(fruit_prices)

for key, value in fruit_prices.items():
    print(f"{key} cost {value}$!")