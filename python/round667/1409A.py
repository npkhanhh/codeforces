from sys import stdin
import math

for _ in range(int(stdin.readline())):
    a, b = list(map(int, stdin.readline().split()))

    res = math.ceil(abs(a - b) / 10)
    print(res)
