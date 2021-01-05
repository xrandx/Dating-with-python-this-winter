#_Author_="Robb Zuo"

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['likes', 'dislikes', 'own']
]

new_L = []
new_L.append(L[0][1])
new_L.append(L[2][0])
new_L.append(L[1][1])

print(str(new_L[0]) + ' ' + str(new_L[1]) + ' ' + str(new_L[2]))