a, b, c, d = list(map(int, input().split()))
a, b, c = sorted([a, b, c])
res = 0
if a > b - d:
    res += a - (b - d)
if c < b + d:
    res += b + d - c
print(res)
