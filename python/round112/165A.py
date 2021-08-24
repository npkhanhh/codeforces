from sys import stdin

a = []
n = int(stdin.readline())
res = 0
for _ in range(n):
    a.append(list(map(int, stdin.readline().split())))
for i in range(n):
    cur = [0, 0, 0, 0]
    for j in range(n):
        if i == j:
            continue
        if a[i][0] == a[j][0] and a[i][1] < a[j][1]:
            cur[0] = 1
        if a[i][0] == a[j][0] and a[i][1] > a[j][1]:
            cur[2] = 1
        if a[i][1] == a[j][1] and a[i][0] < a[j][0]:
            cur[1] = 1
        if a[i][1] == a[j][1] and a[i][0] > a[j][0]:
            cur[3] = 1
    if sum(cur) == 4:
        res += 1
print(res)

