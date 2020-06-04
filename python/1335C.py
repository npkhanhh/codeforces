from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    d = {}
    m = 0
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
        if d[i] > m:
            m = d[i]
    u = len(d.keys())
    if m == u:
        print(m-1)
    else:
        print(min(m, u))
