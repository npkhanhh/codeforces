n = int(input())
res = []
c = 0
for i in range(n):
    s = ''
    for j in range(n):
        if (i + j) % 2 == 0:
            s += 'C'
            c += 1
        else:
            s += '.'
    res.append(s)
print(c)
for i in res:
    print(i)
