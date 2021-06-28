from sys import stdin
from math import gcd

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    for i in range(3):
        t = n + i
        s = sum(list(map(int, list(str(t)))))
        if gcd(t, s) > 1:
            print(t)
            break
