current_num = 0
while True:
    if current_num > 5:
        break
    current_num += 1
    if current_num % 2 == 0:
        continue
    print(current_num)