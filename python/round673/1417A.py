from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    t = min(a)
    res = 0
    met_min = False
    for i in a:
        if i == t and not met_min:
            met_min = True
            continue
        if i < k:
            c, d = divmod(k-i, t)
            res += c
    print(res)
