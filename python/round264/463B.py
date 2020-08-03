n = int(input())
a = list(map(int, input().split()))
res = a[0]
t = 0
for i in range(n-1):
    t += a[i] - a[i+1]
    if t < 0:
        res += abs(t)
        t = 0
print(res)
