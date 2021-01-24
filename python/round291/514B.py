from sys import stdin
import math

n, x, y = list(map(int, stdin.readline().split()))
d = {}
for _ in range(n):
    xx, yy = list(map(int, stdin.readline().split()))
    xx -= x
    yy -= y
    if xx < 0 and yy < 0 or xx > 0 and yy < 0:
        xx = -xx
        yy = -yy

    if xx == 0:
        yy = 1
    elif yy == 0:
        xx = 1
    else:
        g = math.gcd(xx, yy)
        xx //= g
        yy //= g
    d[(xx, yy)] = 1
print(len(d))


