def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result

number = int(input('请输入一个整数'))
result = factorial(number)
print(factorial(number))
print("%d 的阶层是：%d" % (number, result))
