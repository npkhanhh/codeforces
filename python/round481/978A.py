n = int(input())
a = list(map(int, input().split()))[::-1]
d = {}
res = []
for i in a:
    if i in d:
        continue
    d[i] = 1
    res.append(i)
print(len(res))
print(*res[::-1])

