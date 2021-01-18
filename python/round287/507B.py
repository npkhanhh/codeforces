import math

r, x, y, x2, y2 = list(map(int, input().split()))

d = math.dist((x, y), (x2, y2))

print(math.ceil(d / (2*r)))
