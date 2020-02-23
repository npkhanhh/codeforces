n = int(input())
a = list(map(int, input().split()))
res = []
for i in range(1, n):
    if a[i] == 1:
        res.append(a[i-1])
res.append(a[-1])
print(len(res))
print(*res)