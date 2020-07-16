from sys import stdin

for _ in range(int(stdin.readline())):
    x, y, n = list(map(int, stdin.readline().split()))
    t = n // x
    res = t * x + y
    if res > n:
        res -= x
    print(res)

