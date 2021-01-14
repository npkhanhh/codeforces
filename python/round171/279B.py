n, t = list(map(int, input().split()))
a = list(map(int, input().split()))
res = 0
i = 0
j = 0
ts = 0
while i < n:
    if a[i] > t:
        i += 1
        continue
    if ts == 0:
        ts += a[i]
        res = max(1, res)
        j = i+1
    while j < n and ts + a[j] <= t:
        ts += a[j]
        j += 1
    res = max(j - i, res)
    if j == n:
        break
    ts -= a[i]
    i += 1
print(res)
