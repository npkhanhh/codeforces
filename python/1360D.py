from sys import stdin
import math

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    res = n
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            if n // i <= k and i <= res:
                res = i
            elif i <= k and n // i <= res:
                res = n // i
    print(res)

