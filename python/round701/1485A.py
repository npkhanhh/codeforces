from sys import stdin

for _ in range(int(stdin.readline())):
    a, b = list(map(int, stdin.readline().split()))
    offset = 0
    if b == 1:
        offset += 1
        b = 2
    res = 10**9
    for i in range(b, b+30):
        cur = offset + (i - b)
        t = a
        while t > 0:
            t //= i
            cur += 1
        if cur < res:
            res = cur
    print(res)
