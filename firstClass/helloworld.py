print("hello,world1")
x=1
y=2
print(x+y)

# 三引符号跟双引号
haha = """
ajfiljaflaj
jfkewjkefherkjelkgj
fijflkewfjelcfkwlrfkelfkerrf;
"""

print(haha)


# 双引号只能单独一行啊哈
haha2 = "ajfiljaflajksjafkafekljalkfakfhrejejfkjflejrks;lkfhwekictrglhgteop;djghtv "

print(haha2)

# 学习字符串长度
course = "woshidashuaige"

print(len(course))

print(course[13])
print(course[0:3])
print(course[-1])
print(course[-2])

# 如果从索引0开始一直到字符串结尾，结尾没有的话，那么就是跟原始字符串相同
print(course[0:])

# 这是卡还是没有索引的情况下，虽然你没有写 但是他的默认是从0开始的
print(course[:3])

# 这个是没有任何的索引，那么就是直接弄原始字符串相同
print(course[:])


#通过反斜杠来避免双重代码
course2 = "hello\"jasklfjasekf"
print(course2)

# 如何短句变长句
one = "jerry"
two = "guo"
# 第一种：直接加
full = one + two
print(full)

# 第二种：给他中间来一个空格
full2 = one + " " + two
print(full2)

# 第三种： 使用格式化
