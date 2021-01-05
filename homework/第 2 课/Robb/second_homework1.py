#_Author_="Robb Zuo"

list = [ 1, 2, 3, 4, 5]
print(list)
# 增

list.append(8)
print(list)
# 删

list.pop(-2)
print(list)
# 改

list[0] = 9
print(list)

# 查
print(list.index(3))
list = str(list)

f = open('text.txt', 'w', encoding='utf-8')
f.write(list)
f.close()
