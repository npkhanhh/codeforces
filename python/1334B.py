from sys import stdin

for _ in range(int(input())):
    n, x = list(map(int, stdin.readline().split()))
    a = sorted(map(int, stdin.readline().split()), reverse=True)
    a.append(0)
    t = 0
    res = n
    for idx, val in enumerate(a):
        t += val
        tt = t / (idx + 1)
        if tt < x:
            res = idx
            break
    print(res)


