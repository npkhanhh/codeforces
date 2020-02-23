import math

n = int(input())

res = int(math.ceil(n/2))
if n % 2 == 1:
    res*= -1
print(res)
