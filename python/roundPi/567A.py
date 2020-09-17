n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    mi = a[-1]
    ma = a[0]
    if i == 0:
        mi = a[1] - a[0]
    elif i == n - 1:
        mi = a[-1] - a[-2]
    else:
        mi = min(a[i + 1] - a[i], a[i] - a[i - 1])
    ma = max(a[i] - a[0], a[-1] - a[i])
    print(mi, ma)
