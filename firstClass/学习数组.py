# 学习数组

# 第一个数组的基本概念

num = [1, 2, 3, '第一个']

print(num)


# 数组的增加操作

# append()函数，只能加一个一次
num.append('第二个')
print(num)

# extend函数，一次可以多加,但是这个的extend的目的是为来继承数组
# 因此添加的内容是以一个数组的形式来填加到数组
num.extend(['第三个','第四个'])
print(num)

# insert函数
num.insert(0, '牡丹')
print(num)

# 交换元素
temp = num[0]
num[0] = num[1]
print(num)
num[1] = temp
print(num)

# 用remove删除元素
num.remove(1)
print(num)

# 用del删除元素
del num[0]
print(num)

# 同时可以用del 去删除整个数组
# del num
# print(num)

# slice查询 他是左闭右开的情况
num[1 : 3]
num[:3]
num[1: ]


# 使用pop()从后开始删除
num.pop()
print(num)


# 数组比较大小

# 第一种 先定义数组 然后再比较大小获取布尔值
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 > list2)
print(list1 < list2)

# 第二种 多比较类型
list3 = [7, 8, 9]
print((list1 < list2) and (list1 == list3))

# count的方法哈 用于就是统计在该列表总出现的次数
print(list1.count(1))

# index 方法 ，用于就是你要查询的东西位于列表的位置
print(list1.index(1))

# reverse 方法 用于就是反转列表内容排序
# 一般可能会有人想： print(list3.reverse()) 但是这个是会输出none的结果

# 应该是：
list3.reverse()
print(list3)  # 输出 [9, 8, 7]


# sort 方法 用于就是乱的数组内容然后排序的作用
list6 = [0,555,3646,979641,34,49416,366]
print(list6)
list6.sort()
print(list6)
