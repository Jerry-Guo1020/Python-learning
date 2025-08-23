# 原始字符串与反斜杠的关系
# 比如我要输出一个路径 c:\now\good
# 为什么会出现跳行呢？ 因为 \n 会误认为是跳行

str1 = 'c:\now'
print(str1)


str2 = 'c:\\now'
print(str2)

str3 = 'c:\now\good'
print(str3)

str4 = 'c:\\now\\good'
print(str4)

str5 = r'c:\now\good'
print(str5)

