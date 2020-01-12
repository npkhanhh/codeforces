n = int(input())
a = list(map(int, input().split()))

d = {}
res = [-1]
stop = False
for i, value in enumerate(a):
    for j in range(i + 1, n):
        if value + a[j] not in d:
            d[value + a[j]] = [i + 1, j + 1]

for i, value in enumerate(a):
    if value in d:
        res = d[value]
        res.insert(0, i+1)
        break

print(*res)
