from sys import stdin

for _ in range(int(stdin.readline())):
    n, m = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    b = sorted(enumerate(a), key=lambda x: (x[1], -x[0]))
    c = [0]*m
    for i in range(m):
        c[b[i][0]] = i
    res = 0
    cur = [0]*m
    for i in range(m):
        s = c[i]
        for j in range(s):
            res += cur[j]
        cur[s] = 1
    print(res)


