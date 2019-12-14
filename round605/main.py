import math
n = int(input())

for i in range(n):
    a, b, c = sorted(list(map(int, input().split())))
    t = math.floor((a + c) / 2)
    if t > a:
        a += 1
    elif t < a:
        a -= 1
    if t > b:
        b += 1
    elif t < b:
        b -= 1
    if t > c:
        c += 1
    elif t < c:
        c -= 1
    print((b - a) + (c - b) + (c - a))
