# 学习函数
# 定义函数 用def
def haha():
    print(1)
    print(2)
    print(3)

haha()

def haha2(name):
    '这个是用了形参'
    # 这个也是注释
    print(name + "我爱你，因为你用了实参")

haha2('ajfikf')

def haha3 (num1, num2):
    print("这个是一个加法运算哦")
    print(num1 + num2)

haha3(3, 5)

# 函数的分类： 形式参数（形参）、实际参数（实参）
# 形参：就是我用一个定义过程的name是形参
# 实参：我实际调用函数传入的数据就是实参

haha2("小明") # 这个是用实参展示出来
print(haha2.__doc__)  # 使用了形参正确访问文档字符串

# 第二种：
def some(name,details):
    print(name + "->" + details)

some("小明","爱跳舞")     # 但是这种我有可能会弄反数据，解决办法：
some(details="爱跳舞", name="小明")

# 第三种：
def test(*params):    # 使用* 的原因：不需要提前知道用户会传几个参数
        print("参数的长度是：", len(params))
        print("第二个参数是：", params[1])
test(1, "小明", 3.14, 5, 6, 7)




