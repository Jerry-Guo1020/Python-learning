# A = int(input())
# B = int(input())
# jiafa = A + B
# jianfa = A - B
# chengfa = A * B

# if B == 0:
#     chufa = "出错啦"
# else:
#     chufa = "{:.2f}".format(A / B)

# print(f"{A} + {B} = {jiafa}")
# print(f"{A} - {B} = {jianfa}")
# print(f"{A} * {B} = {chengfa}")
# print(f"{A} / {B} = {chufa}")


# a,b = map(int,(input().split()))
# temp = a
# a = b
# b = temp
# print(f"a={a},b={b}")

# a = int(input())
# if a > 0:
#     print("+")
# elif a < 0:
#     print("-")
# else:
#     print("0")

# a = float(input())
# b = 27 + 23 + 3*a
# print(b)
# c = 1.2 * a
# print(c)

# if b < c:
#     print("Bike")
# elif b > c :
#     print("Walk")
# else:
#     print("All")

# x, y = map(int,input().split())
# if x < 60 or y <60:
#     print("不合格")
# else:
#     z = (x+y)/2
#     result = z
#     if result >= 90:
#         print("成绩优秀")
#     else:
#         print("通过")

# a = int(input())
# if a % 4 == 0 and a % 100 != 0 and a % 400 != 0 :
#     print("YES")
# else:
#     print("NO")

# def haha(s):
#     count = 0
#     for char in s:
#         if char.isdight():
#             count += 1 
#     return count
# T = int(input())
# for _ in range(T):
#     s = input()
#     haha2 = haha(s)
#     print(haha2)

# def count_digits(s):
#     count = 0
#     for char in s:
#         if char.isdigit():
#             count += 1
#     return count
# T = int(input())
# for _ in range(T):
#     s = input()
#     digit_count = count_digits(s)
#     print(digit_count)



# T = int(input())
# for _ in range(T):
#     s = input()
#     count = 0
#     for char in s:
#         if char.isdight():
#             count += 1
#     print(count)


# def calculate_average(s):
#   numbers = [int(num) for num in s.split()]
#   if not numbers:
#     return 0.0  
#   return sum(numbers) / len(numbers)

# T = int(input())

# for _ in range(T):
#   s = input()
#   average = calculate_average(s)
#   print(f"{average:.1f}") 

def aaa(x):
    if x == 0:
        result = 0
    else:
        result = 1 / x
    return result

if __name__ == "__main__":
    x = float(input())
    result = aaa(x)
    print('f({:})={:.3f}'.format(x,result))