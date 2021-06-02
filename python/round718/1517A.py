from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a, b = divmod(n, 2050)
    if b != 0:
        print(-1)
    else:
        res = 0
        while a > 0:
            res += a % 10
            a //= 10
        print(res)
