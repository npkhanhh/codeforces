import math
n, k = list(map(int, input().split()))
r = math.ceil(n*2 /k)
g = math.ceil(n*5 / k)
b = math.ceil(n*8 / k)
print(r+g+b)
