n = int(input())
a = list(map(int, input().split()))
m = a[0]
mi = 0
dip = False
has_result = True
for i in range(1, n):
    if a[i] >= m and not dip:
        m = a[i]
        mi = i
    if a[i] < a[i-1]:
        if dip:
            has_result = False
            break
        else:
            dip = True

    if dip and a[i] > a[0]:
        has_result = False
        break
if has_result:
    print(n-1 - mi)
else:
    print(-1)
