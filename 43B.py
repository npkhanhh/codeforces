s = input()
d = {}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
s2 = input()
res = 'YES'
for i in s2:
    if i == ' ':
        continue
    if i in d:
        d[i] -= 1
        if d[i] == 0:
            del d[i]
    else:
        res = 'NO'
        break
print(res)
