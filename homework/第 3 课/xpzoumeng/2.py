##2
#输入n
n = int(input())

#计算平均值
average = 0.0
for i in range(n):
    a = float(input())
    average += a / n

print(average)