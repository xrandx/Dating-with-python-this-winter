#-*- codeing = utf-8 -*-
#@Time : 2021-01-08 18:30
#@Author : 苏苏
#@File : 第三节课作业2.py
#@Software : PyCharm




initial_num = int(input("type a number"))
num = int(input("type the number again"))
sum=0

while True:
    print(num)
    sum += num
    num -= 1
    if num == 0:
        break


print(sum)


print(sum/initial_num)


