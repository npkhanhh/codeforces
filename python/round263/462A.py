from sys import stdin

n = int(stdin.readline())
a = []
b = [(1, 0),(-1, 0), (0, 1), (0, -1)]
for _ in range(n):
    a.append(stdin.readline().strip())

res = 'YES'
for i in range(n):
    for j in range(n):
        cur = 0
        for t in b:
            if 0 <= i+t[0] < n and 0 <= j+t[1] < n and a[i+t[0]][j+t[1]] == 'o':
                cur += 1
        if cur % 2 != 0:
            res = 'NO'
            break
    if res == 'NO':
        break
print(res)
