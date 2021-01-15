from sys import stdin

a = []
for _ in range(int(stdin.readline())):
    a.append(list(map(int, stdin.readline().split())))

a = sorted(a, key=lambda x: (x[0], x[1]))
res = -1
for i in a:
    if i[1] >= res:
        res = i[1]
    else:
        res = i[0]
print(res)
