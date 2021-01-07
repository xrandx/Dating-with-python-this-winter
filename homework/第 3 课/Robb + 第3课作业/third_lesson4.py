#_Author_="Robb Zuo"

num = int(input("数组里包含数字的个数:"))

num_list = []

for i in range(num):
    num_list.append(int(input("输入第{0}个数字:".format(i+1))))

# print(num_list)
sum_num_list = []
for i in range(num):
    sum_num_list.append(0)

# print(sum_num_list)

for i in range(num):
    for n in range(i+1):
        sum_num_list[i] = sum_num_list[i] + num_list[n]


print("加法动态数组：", '\n',sum_num_list)
