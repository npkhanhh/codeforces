from sys import stdin

import math

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    res = 'NO'
    for i in a:
        if math.sqrt(i) % 1 > 10**-9:
            res = 'YES'
            break
    print(res)
