#-*- codeing = utf-8 -*-
#@Time : 2021-01-06 21:24
#@Author : 苏苏
#@File : 第三节课.py
#@Software : PyCharm

# True or x -> True
# False and x -> False


#1. 程序要满足：输入分数x(0<X<100),60以下不及格，60到80及格，80到90良好，90以上优秀


score = int(input("你的分数"))

if score<60:
    print("不及格")
elif score<80:
    print("及格")
elif score<90:
    print("良好")
else:
    print("优秀")















#上课笔记
'''
#while
knock_count=99
def open():
    print("open the door")
while knock_count !=0:
    knock_count -=1
    print("knock")
else:
    open()

for item in range(0,10,3):
        print(item)
'''


