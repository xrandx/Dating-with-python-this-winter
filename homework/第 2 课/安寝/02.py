li = [2,4,6,8,10,12]
li.append(14)
li.pop(0)
li[0] = 100
print(li.index(10))
f = open("kkw.txt", 'w', encoding="utf-8")
f.write(str(li))
f.close()