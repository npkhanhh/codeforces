n, k = list(map(int, input().split()))

a = sorted(map(int, input().split()))
res = -1
if k == 0 and a[0] > 1:
    res = a[0] - 1
elif k == n:
    res = a[-1]
elif a[k] - a[k-1] > 0:
    res = a[k-1]

print(res)


