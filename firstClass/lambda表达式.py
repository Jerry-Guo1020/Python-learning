# lambda表达式
def fun1(x):
    return 2 *x +1
print(fun1(5))

# 使用lambda的话就是
g = lambda x : 2 * x + 1
print(g(5))

#现在是学习用filter来进行

# 这个使用一个列表然后呢 来进行分辨要求 none的话一般是去正或者是true
print(list(filter(None, [1, 0, False, True])))


# 然后现在用一个函数

def fun3(z):
    return z % 2
temp = range(10)
show = filter(fun3, temp)
print(list(show))

#或者直接用lambda的方式是
print(list(filter(lambda y : y % 2, range(10))))


#map()序列
print(list(map(lambda y : y * 2, range(10))))

