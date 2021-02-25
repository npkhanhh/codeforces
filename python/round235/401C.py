n, m = list(map(int, input().split()))
if m < n - 1 or n * 2 + 2 < m:
    print(-1)
else:
    res = ''
    if m > n:
        d = min(m - n, n)
        res += '110'*d
        n -= d
        m -= 2*d
    t = min(m, n)
    res += '10'*t
    m -= t
    n -= t
    if m > 0:
        res += '1' * m
    if n > 0:
        res = '0' + res
    print(res)
