n, m, a, b = list(map(int, input().split()))
if b / m < a:
    c, d = divmod(n, m)
    res = c * b
    if d * a < b:
        res += d*a
    else:
        res += b
    print(res)
else:
    print(n*a)