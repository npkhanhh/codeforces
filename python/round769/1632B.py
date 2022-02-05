from sys import stdin
from math import log2

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = int(log2(n))
    t = pow(2, a)
    if t == n:
        t = pow(2, a-1)
    res = list(range(n-1, t-1, -1)) + list(range(t))
    print(*res)
