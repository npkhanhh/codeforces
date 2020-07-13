from sys import stdin
import math

for _ in range(int(stdin.readline())):
    n, m = list(map(int, stdin.readline().split()))
    print(math.ceil(n * m / 2))
