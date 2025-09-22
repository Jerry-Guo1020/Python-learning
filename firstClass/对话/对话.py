# 打开文件
f = open("D:\\Python\\firstClass\\对话\\communication.txt", 'r', encoding='cp936')
print(f)
ff = f.read()
print(ff)
f.close()
