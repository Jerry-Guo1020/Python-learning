import random

people = ["g", "wn", "wyy", "zkx", "zyy"]
group_of_3 = random.sample(people, 3)
group_of_2 = [p for p in people if p not in group_of_3]

print("3人组：", group_of_3)
print("2人组：", group_of_2)