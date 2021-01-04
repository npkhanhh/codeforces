import math

n, m = list(map(int, input().split()))

a = list(map(int, input().split()))
ma = 0
res = 0
for idx, val in enumerate(a):
    t = math.ceil(val / m)
    if t >= ma:
        ma = t
        res = idx + 1
print(res)


