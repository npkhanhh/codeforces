n = int(input())

a = list(map(int, input().split()))

m = abs(a[-1] - a[0])
res = [1, n]
for i in range(1, n):
    if abs(a[i-1] - a[i]) < m:
        m = abs(a[i-1] - a[i])
        res = [i, i+1]
print(*res)


