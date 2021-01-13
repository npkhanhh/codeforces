n, m = sorted(map(int, input().split()))
res = 0

if m > 2 * n:
    print(n)
else:
    t = m - n
    res = t
    n -= t
    res += (n * 2) // 3
    print(res)

