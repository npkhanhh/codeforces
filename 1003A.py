n = int(input())
a = list(map(int, input().split()))

d = {}
res = 0
for i in a:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
    if d[i] > res:
        res = d[i]
print(res)