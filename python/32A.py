res = 0
n, d = list(map(int, input().split()))
a = list(map(int, input().split()))
for i in range(n-1):
    for j in range(i+1, n):
        if abs(a[j]-a[i]) <= d:
            res += 2
print(res)