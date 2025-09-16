brand = ["李宁","耐克","阿迪达斯","鱼c工作室"]
slogan = ["-切皆有可能","Just do it","Impossible is nothing","让编程改变世界"]
print("鱼c工作室的口号是:", slogan[brand.index('鱼c工作室')])



# 学习字典的基本知识

#第一种用法：
dict1 = {"李宁":"-切皆有可能","耐克":"Just do it","阿迪达斯":"Impossible is nothing","鱼c工作室": "让编程改变世界"}
print("鱼c工作室的口号是:", dict1['鱼c工作室'])


# 第二种用法

dict2 = dict((('F', 30), ('I', 105), ('S', 115), ('H', 104),))
print(dict2)

# 第三种用法

dict3 = dict(小甲鱼 = "让编程改变世界", 啊哈哈哈 = "就发好疯狂积分")
print(dict3)
print(dict3['小甲鱼'])


# 第四种用法

dict4 = {}
print(dict4.fromkeys((1, 2, 3)))    # 这个一开始是空的 是因为我还没有加入东西进去
print(dict4.fromkeys((1, 2, 3), 'Number'))  # 给这三个内容的类型进行定义？
print(dict4.fromkeys((1, 2, 3), ('one', 'two', 'three')))




# 连续的东西
dict5 = {}
dict5 = dict5.fromkeys(range(32), "给你点赞")
print(dict5)
