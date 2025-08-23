# 学习字符串

# capitalize()将首字母改成大写
str1 = 'woshi'
print(str1.capitalize())

# casefold() 将所有字母改成小写
str2 = 'fjsafkafSSSSGHHKAsnfjkhfk'
print(str2.casefold())

# center(width) 将字符内容居中展示
print(str2.center(40))

# count(sub[,start[,end]]) 统计sub你要求内容在这个字符串里面出现的次数，然后start和end是可以划定范围的
print(str2.count('a'))

# find(sub) 输入您想搜索的内容 如果有返回那就回告诉你的位置，没有就-1
print(str2.find('fj'))

# join(sub) 用法就是您输入的内容每一个字符都是一个分隔符进行重复输出内容
print(str1.join('1234567'))


# replace(old, new) 更换功能，替换内容
print(str1.replace('woshi', 'Woshi'))

# 格式化 format()
print("{a} love {b}.{c}".format(a = "I", b = "you", c ="haha"))

# 把花括号打印出来
print("{{0}}".format("不打印"))

# 打印gb 知识点：Python字符格式化 通过format格式化来进行格式化，其中 {0}和{1}是占位符，分别别表示第一个和第二个参数
print('{0:.1f}{1}'.format(27.658, 'GB'))

