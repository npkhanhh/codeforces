n = int(input())

for _ in range(n):
    a, b, c, r = list(map(int, input().split()))
    a1 = min(a,b)
    b1 = max(a,b)
    res = b1 - a1
    if a1 > c + r and b1 > c + r:
        print(res)
        continue
    if a1 < c - r and b1 < c - r:
        print(res)
        continue
    if b1 > c - r or a1 < c + r:
        res -= min(b1, c+r) - max(a1, c-r)
    print(res)