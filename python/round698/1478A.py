from sys import stdin
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    res = 0
    cur = 1
    for i in range(1, n):
        if a[i] == a[i-1]:
            cur += 1
        else:
            if cur > res:
                res = cur
            cur = 1

    if cur > res:
        res = cur
    print(res)

