from sys import stdin

for _ in range(int(stdin.readline())):
    a, b = sorted(map(int, stdin.readline().split()))
    d = b - a
    t = min(a, d)
    a -= t
    b -= 2*t
    res = t
    if a > 0:
        x, y = divmod(a, 3)
        res += 2*x
        if y >= 2:
            res += 1

    print(res)
