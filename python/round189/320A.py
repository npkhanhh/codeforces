s = input()
one = 0
four = 0
res = 'YES'
for i in s:
    if i != '1' and i != '4':
        res = 'NO'
        break
    if one == 0 and i == '4':
        res = 'NO'
        break
    if i == '1':
        one = 1
        four = 0
    elif i == '4' and four == 2:
        res = 'NO'
        break
    elif i == '4':
        four += 1


print(res)
