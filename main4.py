import math


def lcm(a, b):
    return a * b // math.gcd(a, b)


n = int(input())

l = list(map(int, input().split()))
y = 0
m = z = max(l)
if n>2:
    for i in range(n-1):
        t = math.gcd(l[i], l[i+1])
        if t < z:
            z = math.gcd(z, t)

    for i in range(n):
        y += (m-l[i]) // z
else:
    y = 1
    z = max(l) - min(l)
print(*[y, z])



