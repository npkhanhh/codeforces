from sys import stdin

for _ in range(int(stdin.readline())):
    n, m = list(map(int, input().split()))
    low = m
    high = m
    res = 'YES'
    prev_t = 0
    for _ in range(n):
        t, l, h = list(map(int, input().split()))
        if res == 'NO':
            continue
        low -= t - prev_t
        high += t - prev_t
        prev_t = t
        if high < l or low > h:
            res = 'NO'
            continue
        else:
            a = sorted([low, high, l, h])
            low = a[1]
            high = a[2]
    print(res)



