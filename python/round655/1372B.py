from sys import stdin


def smallest_divisor(n):
    for i in [2, 3, 5]:
        if n % i == 0:
            return i
    increments = [4, 2, 4, 2, 4, 6, 2, 6]
    d = 7
    inc = 0
    while d * d <= n:
        if n % d == 0:
            return d
        d += increments[inc]
        inc += 1
        if inc == 8:
            inc = 0
    return n


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    sm = smallest_divisor(n)
    t = n // sm
    print((sm-1)*t, t)
