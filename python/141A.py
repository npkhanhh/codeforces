d = {}
s1, s2 = input()+input(), input()
for c in s1:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1
res = 'YES'
for c in s2:
    if c not in d:
        res = 'NO'
        break
    else:
        d[c] -= 1
        if d[c] == 0:
            del d[c]
if len(d.keys()) > 0:
    res = 'NO'
print(res)
