from sys import stdin


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    total = 0
    cur = 0
    res = 'YES'
    for i in range(n):
        total += i
        cur += a[i]
        if cur < total:
            res = 'NO'
            break
    print(res)
