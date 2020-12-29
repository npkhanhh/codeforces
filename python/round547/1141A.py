n, m = list(map(int, input().split()))
if m % n != 0:
    print(-1)
else:
    res = 0
    t = m // n
    while t % 2 == 0:
        t //= 2
        res += 1
    while t % 3 == 0:
        t //= 3
        res += 1
    if t != 1:
        res = -1
    print(res)
