from sys import stdin

import math

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    res = 'NO'
    if n % 2 == 0:
        t = n // 2
        if math.sqrt(t) % 1 < 10**-9:
            res = 'YES'
    if n % 4 == 0:
        t = n // 4
        if math.sqrt(t) % 1 < 10**-9:
            res = 'YES'
    print(res)
