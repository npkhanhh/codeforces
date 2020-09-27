n, m = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))
res = 0
for i in range(m):
    if a[i] >= 0:
        break
    res += abs(a[i])
print(res)
