from sys import stdin
import math

for _ in range(int(input())):
    a, b, c, d = list(map(int, stdin.readline().split()))
    if b >= a:
        print(b)
    elif c <= d:
        print(-1)
    else:
        t = math.ceil((a - b) / (c - d))
        print(b+t*c)
