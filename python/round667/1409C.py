from sys import stdin
import math

for _ in range(int(stdin.readline())):
    n, x, y = list(map(int, stdin.readline().split()))
    t = math.ceil((y - x) / (n - 1))
    gap = 1
    for i in range(t, y - x + 1):
        if (y - x) % i == 0:
            gap = i
            break
    res = list(range(y, max(0, y - (gap*(n - 1)) - 1), -gap))
    r = n - len(res)
    res += list(range(y + gap, y + (gap * r) + 1, gap))
    print(*res)
