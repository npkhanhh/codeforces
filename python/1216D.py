import math

n = int(input())
a = list(map(int, input().split()))
m = max(a)
z = m - a[0]
y = 0
for i in a[1:]:
    z = math.gcd(z, (m-i))
for i in a:
    y += (m - i) // z
print(*[y, z])



