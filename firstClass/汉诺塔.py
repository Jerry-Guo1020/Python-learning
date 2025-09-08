def hanoi(n, x, y, z):
    if n == 1:  # 这个是当x只有一个盘子的话 直接就可以移动到z
        print(x, '-->' ,z)
    else:
        # 将前面的n-1 个盘子从x移动到y上
        print(x, '-->' , z)  # 然后将最底下的那个移动到z
        #下一步： 将n-1个盘子移动到z
        hanoi(n-1, x, z, y)
        print(x, '-->' , z)
        hanoi(n-1, y, x, z)
n= int(input('请输入汉诺塔的层数：'))
hanoi(n, 'X', 'Y', 'Z')
