from sys import stdin

for _ in range(int(stdin.readline())):
    res = 0
    a, b = sorted(map(int, stdin.readline().split()))
    if b % a != 0:
        print(-1)
        continue
    t = b // a
    while t % 8 == 0:
        t //= 8
        res += 1
    while t % 4 == 0:
        t //= 4
        res += 1
    while t % 2 == 0:
        t //= 2
        res += 1
    if t > 1:
        print(-1)
    else:
        print(res)
