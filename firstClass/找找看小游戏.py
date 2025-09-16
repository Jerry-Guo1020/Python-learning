# 找找看小游戏


num1 = {}

# 第一种：有一个找找看的列表 然后呢 新定义一个元组然后通过if的语句来排除重复的地方
num1 = {1, 2, 3, 6, 9, 4, 5, 13, 5, 6, 2, 6 }
temp = []
for each in num1:
    if each not in temp:
        temp.append(each)
print(temp)


# 第二种：
num1 = list(set(num1))
print(num1)
