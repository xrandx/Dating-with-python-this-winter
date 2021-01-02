#第一题
temp1 = input("请输入第一个数")
temp2 = input("请输入第二个数") #用input函数输入两个数
temp1=int(temp1)
temp2=int(temp2) #将两个数由字符型转为数值型
print(temp1 + temp2)
print(temp1 - temp2)
print(temp1 * temp2)
print(temp1 / temp2) #对这两个数字进行加减乘除
print(temp2 + temp1)
print(temp2 - temp1)
print(temp2 * temp1)
print(temp2 / temp1) #对这两个数字进行加减乘除

#第二题
string = input("请输入一串字符") #用input函数输入字符
number = input("请输入一个整数") #用input函数输入一个整数
number =int(number) #将输入的数字转成数值型
print(number * string) #拼接打印n遍