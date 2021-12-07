import math

n, m, z = list(map(int, input().split()))
print(z // ((n*m)//math.gcd(n, m)))
