#-*- codeing = utf-8 -*-
#@Time : 2021-01-03 20:58
#@Author : 苏苏
#@File : 第二节课作业.py
#@Software : PyCharm



array=[2,3,4,5,6]


array.append(8)
array.pop(-3)
array[1]=33
print(array)
print(array.index(2))
print(type(array))


file=open("array.txt","w",encoding="utf-8")
file.write(str(array))
file.close()
#在左侧栏里创建array.txt成功