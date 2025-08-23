a = list()
print(a)

b = 'fjskafjklj'
print(b)

b = list(b)
print(b)

c = (1, 1, 2, 3, 5, 8, 13, 21, 34)
print(c)
c = list(c)
print(c)


# 增删改查

# 增加
str1 = "fajkf"
str2 = "sjsflkewjf"

str3 = str1 + str2
print(str3)

# 弄出最大最小值、数组的长度
str4 = [1, 2, 3, 4]
print(max(str4))
print(min(str4))
print(len(str4))

tuple1 = (9, 5, 3, 6, 4, 8 )
print(max(tuple1))
print(min(tuple1))
print(len(tuple1))

# 扩展一个知识点——用sorted方法从小到大来排序、用revesed来进行从大到小排序[这个出来的是一个对象]
print(sorted(tuple1))
print(reversed(tuple1))


# 将这个元组转换成列表
print(list(reversed(tuple1)))

# 通过enumerate来增加每一个书的索引值
print(list(enumerate(tuple1)))


d = [1, 2, 3, 4, 5, 6, 7, 8]
e = [1, 2, 3, 4]
print(zip(d, e))
print(list(zip(d, e)))
