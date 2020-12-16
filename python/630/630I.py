import math

n = int(input())

space = 2 * n - 2

rs = space - n

res = 2 * 4 * 3 * pow(4, rs - 1)
if n > 3:
    res += 3 * 4 * 3 * pow(4, rs - 2) * (rs - 1)
print(res)
