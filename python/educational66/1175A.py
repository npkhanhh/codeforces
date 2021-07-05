from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    res = 0
    a, b = divmod(n, k)

    while n > 0:
        if n % k == 0:
            n //= k
            res += 1
        else:
            t = n % k
            n -= t
            res += t
    print(res)

