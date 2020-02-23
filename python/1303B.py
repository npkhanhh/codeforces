import math

s = int(input())

for i in range(s):
    n, g, b = list(map(int, input().split()))
    if g >= b:
        print(n)
    else:
        r = math.ceil(n / 2)
        c, d = divmod(r, g)
        if d == 0:
            c -= 1
            d += g
        if (g + b) * c + d < n:
            print(n)
        else:
            print((g + b) * c + d)
