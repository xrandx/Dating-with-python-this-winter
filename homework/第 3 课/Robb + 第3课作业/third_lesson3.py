#_Author_="Robb Zuo"

str_input = input("请输入一段字符串：")
num_input = int(input("请输入一个整数："))

if num_input > len(str_input) or num_input < 0:
    print("Wrong!")
else:
    str_behind = []
    str_forward = []
    for i in range(num_input):
        str_forward.append(str_input[i])

    for i in range(num_input, len(str_input)):
        str_behind.append(str_input[i])
    str_output = str(str_behind[0])
    for i in range(1, len(str_input)-num_input):
        str_output += str(str_behind[i])
    for i in range(num_input):
        str_output += str(str_forward[i])

    print(str_output)

