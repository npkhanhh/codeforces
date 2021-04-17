from sys import stdin
import math

for _ in range(int(stdin.readline())):
    n, x = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    res = [0, 0]
    total = 0
    for i in a:
        total += i
        res[1] += int(math.ceil(i/x))
    res[0] = int(math.ceil(total / x))
    print(*res)
