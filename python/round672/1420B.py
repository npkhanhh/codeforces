from sys import stdin
import math


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    m = 0
    d = [0]*50
    for i in a:
        d[int(math.log(i, 2))] += 1
    res = 0
    for i in d:
        res += i*(i-1) // 2
    print(res)

