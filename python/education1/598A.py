from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    t = 1
    res = 0
    while True:
        res += t
        t *= 2
        if t > n:
            break
    res = n * (n + 1) // 2 - 2 * res
    print(res)

