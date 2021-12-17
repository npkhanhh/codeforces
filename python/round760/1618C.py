from sys import stdin
from math import gcd

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    g1, g2 = 0, 0
    a = list(map(int, stdin.readline().split()))
    for i in range(0, n, 2):
        if g1 == 0:
            g1 = a[i]
        else:
            g1 = gcd(g1, a[i])
        if i + 1 < n:
            if g2 == 0:
                g2 = a[i+1]
            else:
                g2 = gcd(g2, a[i+1])
    res1, res2 = True, True
    for i in range(0, n, 2):
        if a[i] % g2 == 0:
            res2 = False
        if i + 1 < n and a[i+1] % g1 == 0:
            res1 = False
    if res1:
        print(g1)
    elif res2:
        print(g2)
    else:
        print(0)

