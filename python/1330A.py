from sys import stdin

for _ in range(int(stdin.readline())):
    n, x = list(map(int, stdin.readline().split()))
    a = sorted(map(int, stdin.readline().split()))
    v = min(a[0] - 1, x)
    x -= v
    res = v
    i = 0
    while i < n:
        if a[i] <= res + 1:
            res = a[i]
            i+=1
            continue
        if x == 0:
            break
        v = min(a[i] - res - 1, x)
        x -= v
        res += v
    res += x
    print(res)
