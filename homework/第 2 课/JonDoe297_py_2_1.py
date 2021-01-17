# -*- coding: utf-8 -*-
# @Time    : 2021/1/1111 4:14 PM
# @Author  : agrroc
# @File    : py_2_1.py

lists = [1, 3, 5, 7]  # 定义一个列表
print(lists)  # [1, 3, 5, 7]

lists.append(11)  # 进行增加操作
print(lists)  # [1, 3, 5, 7, 11]
lists.insert(-1, 9)
print(lists)  # [1, 3, 5, 7, 9, 11]

lists.pop(-2)  # 进行删除操作，删除倒数第二个元素
print(lists)  # [1, 3, 5, 7, 11]

lists[0] = 2  # 进行修改操作，把第一个位置改为2
print(lists)  # [2, 3, 5, 7, 11]

print(lists.index(5))  # 进行查找操作 2

lists = str(lists)  # 转为字符串
f = open("text.txt", "w", encoding="utf-8")  # 按照utf-8编码输出为txt文件
f.write(lists)
f.close()


