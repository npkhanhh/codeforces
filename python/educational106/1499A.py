from sys import stdin

for _ in range(int(stdin.readline())):
    n, k1, k2 = list(map(int, stdin.readline().split()))
    w, b = list(map(int, stdin.readline().split()))

    res = 'YES'
    if k1+k2 < w*2:
        res = 'NO'
    if (n-k1) + (n-k2) < b*2:
        res = 'NO'
    if n*2 < w*2 + b*2:
        res = 'NO'

    print(res)
