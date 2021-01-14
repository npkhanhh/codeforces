n, m = list(map(int, input().split()))

if n >= m:
    print(n-m)
else:
    res = 0
    while True:
        if m % 2 == 1:
            res += 1
            m += 1
        if n < m // 2:
            res += 1
            m //= 2
        elif n >= m // 2:
            res += n - m // 2 + 1
            break
    print(res)
