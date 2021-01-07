#_Author_="Robb Zuo"

num_input = float(input("请输入分数："))

if num_input >100 or num_input< 0:
    print("输入分数范围不正确")
elif num_input < 60:
    print("不及格")
elif num_input >= 60 and num_input <80:
    print("及格")
elif num_input >= 80 and num_input <90:
    print("良好")
else:
    print("优秀")


