from sys import stdin
import math

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    if k < n:
        k = math.ceil(n / k) * k
    res, t = divmod(k, n)
    if t > 0:
        res += 1
    print(res)
