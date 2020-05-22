from sys import stdin

for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, stdin.readline().split()))
    res = []
    c, d = divmod(n, 2)
    for i in range(c):
        res.append(a[i])
        res.append(a[n-i-1])
    if d > 0:
        res.append(a[c])
    print(*reversed(res))


