n, c = list(map(int, input().split()))
a = list(map(int, input().split()))
res = 1
for i in range(n - 1):
    if a[i + 1] - a[i] <= c:
        res += 1
    else:
        res = 1
print(res)
