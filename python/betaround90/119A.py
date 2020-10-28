import math

a, b, n = list(map(int, input().split()))
res = 1
while True:
    if res == 1:
        n -= math.gcd(n, a)
    else:
        n -= math.gcd(n, b)
    res = 1 - res
    if n == 0:
        break
print(res)

