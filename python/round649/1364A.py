from sys import stdin

for _ in range(int(stdin.readline())):
    n, x = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    l = n + 2
    r = n + 2
    s = 0
    for idx, val in enumerate(a):
        if val % x != 0:
            if l == n + 2:
                l = idx + 1
            r = n - idx
        s += val
    res = n
    if s % x == 0:
        if l != n + 2 or r != n + 2:
            res -= min(l, r)
        else:
            res = -1
    print(res)


