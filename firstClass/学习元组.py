# 学习基本的元组是什么
tuple1 = (1, 2, 3, 4, 5 )
print(tuple1)

# 判断是否是元组
print(type(tuple1))

# 元组跟整型的区别
tuple2 = (1)
tuple3 = (1,)
print(type(tuple2))
print(type(tuple3))  # 逗号是元组的关键

tuple4 = 1, # 甚至不用逗号也可以
print(type(tuple4))

# 插入数据
tuple1 = tuple1[:2] + ('哈哈',) + tuple1[2:]
print(tuple1)
