#_Author_="Robb Zuo"

int_input = int(input("请输入一个整数："))

num_rec = []

for i in range(int_input):
    num_rec.append(int(input("请输入第{0}个数字:".format(i+1))))

add_num = 0

for i in range(int_input):
    add_num = add_num + num_rec[i]

average_num = add_num / int_input
print("平均值为:", average_num)