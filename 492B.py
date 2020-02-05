n, l = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))
res = 0
t = 0
for i in range(1, n):
    if a[i] - a[i-1] > t:
        t = a[i] - a[i-1]
res = t/2
if a[0] > res:
    res = a[0]
if l - a[-1] > res:
    res = l - a[-1]
print(res)

