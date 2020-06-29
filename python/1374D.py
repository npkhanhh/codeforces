from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    d = {}
    res = 0
    for i, v in enumerate(a):
        if v % k == 0:
            continue
        else:
            t = k - (v % k)
            if t not in d:
                d[t] = 0
            else:
                d[t] += 1
            if d[t]*k + t > res:
                res = d[t]*k + t
    if res == 0:
        print(res)
    else:
        print(res + 1)

