from sys import stdin
import math
I = stdin.readline

for _ in range(int(I())):
    n, m, k = list(map(int, I().split()))
    mj = min(m, n//k)
    rj = math.ceil((m - mj)/(k-1))
    print(mj-rj)
