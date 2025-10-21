password = 111111
money = 10000

print("---------------欢迎使用atm-------------")

# 1. 密码验证（带异常处理）
for i in range(3):
    try:                         
        guess = int(input("请输入密码："))
    except ValueError:
        print("密码必须是数字！")   
        continue                  
    if guess == password:
        print("欢迎使用！")
        break
    if i < 2:
        print("密码错误！请再试一次")
else:
    print("密码错误，请取卡")
    exit()

print(f"\n你当前余额为:{money}元")


for i in range(3):
    try:
        operation = int(input("请输入您的取款金额（100~5000，整百）："))
    except ValueError:
        print("金额必须是数字！")
        continue
    if operation % 100 == 0 and 100 <= operation <= 5000:
        print(f"\n您现在取的金额是：{operation}")
        money -= operation
        print("交易完成，请取卡")
        break
    if i < 2:
        print("数额只能是整百而且不能超过5000元")
else:
    print("您输入金额有误，请取卡")
    exit()


for n in range(3):
    result = int(input("如果您已经完成业务，请按1退出即可结束交易"))
    if result == 1:
        print("bye")
        exit()
        break
    else:
        if n < 2:
            print("指令不正确，请再输一次")
        else:
            print("交易完成，请取卡")
            exit()
else:
    exit()