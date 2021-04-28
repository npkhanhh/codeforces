from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    res = -1
    for i in range(n - 1, -1, -1):
        if i + a[i] < n:
            a[i] += a[i + a[i]]
        res = max(res, a[i])
    print(res)
