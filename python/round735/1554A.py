from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    m = max(a)
    res = -1
    for i in range(n):
        if i > 0:
            res = max(res, a[i]*a[i-1])
        if i < n-1:
            res = max(res, a[i]*a[i+1])
    print(res)

