# 全局变量和局部变量

# 全局变量的案例
def haha(price, rate):
    Price = price * rate
    print("这里打印全局变量的old_price" + old_price)
    return Price

old_price = float(input("请输入原价："))
rate = float(input("请输入折扣:"))


new_price = haha(old_price, rate)
print("最终价格"+ new_price)
