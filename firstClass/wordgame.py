import random
secret = random.randint(1, 10)

print('------------------小游戏--------------')
temp = input("请输入你喜欢的数字")
guess = int(temp)
while guess != 8:
    
    guess = int(temp)
    if guess == secret:
        print("恭喜你猜对了")
        break
    else:
         if guess > secret:
             print("to big")
             temp = input("猜错了哦 再输入一次吧")
         else:
             print("to small")
             temp = input("猜错了哦 再输入一次吧")
print("game over")
    
