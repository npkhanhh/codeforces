from sys import stdin
import math

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    res = 0
    for i in range(1, n):
        low = min(a[i], a[i-1])
        high = max(a[i], a[i-1])
        while low * 2 < high:
            res += 1
            low *= 2
    print(res)
