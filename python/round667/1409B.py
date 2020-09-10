from sys import stdin

for _ in range(int(stdin.readline())):
    a, b, x, y, n = list(map(int, stdin.readline().split()))
    min_a = max(x, a - n)
    min_b = max(y, b - n)
    if min_a < min_b:
        t = a - min_a
        a = min_a
        n -= t
        b = max(y, b - n)
    else:
        t = b - min_b
        b = min_b
        n -= t
        a = max(x, a - n)
    print(a * b)
