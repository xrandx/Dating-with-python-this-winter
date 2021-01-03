array=[2,5,8,9,3,6]
a=[1,3,6]
matrix=[a,[2,5,7]]
array.append(1)
print(matrix)
print(array)
new_list=array+matrix
print(new_list)
new_list.pop(-3)
print(new_list)
new_list[0]="T"
print(new_list)
# new_list.clear()
# print(new_list)
print(new_list.index(5))
table=tuple(["Monday","Tuesday"])
print(table[1])

string="123456789"
print(string[1:-3])
f=open("test.txt", "w", encoding="utf-8")
f.write(string*10)
f.close()
