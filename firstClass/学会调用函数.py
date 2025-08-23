# 学会调用函数
def fun1():
    print('正在调用函数1')
    def fun2():
        print('正在调用函数2')
    fun2()

fun1()

#nonlocal
def fun3():
    x = 5
    def fun4():
        nonlocal x
        x *= x
        return x
    return fun4()
print(fun3())
