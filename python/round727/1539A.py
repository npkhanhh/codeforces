from sys import stdin
from queue import Queue

for _ in range(int(stdin.readline())):
    n, x, t = list(map(int, stdin.readline().split()))
    if t < x:
        print(0)
    else:
        a = t // x
        if a >= n:
            print(n*(n-1)//2)
        else:
            b = a*(a-1) // 2
            print(a*(n-a)+b)

