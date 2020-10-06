from sys import stdin
import math

for _ in range(int(stdin.readline())):
    n, x = list(map(int, stdin.readline().split()))
    res = n - 2
    res = math.ceil(res / x)
    res += 1
    if n <= 2:
        res = 1
    print(res)

