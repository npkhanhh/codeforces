import math

for _ in range(int(input())):
    a, b, c, d, k = list(map(int, input().split()))
    x = math.ceil(a/c)
    y = math.ceil(b/d)
    if x + y > k:
        print(-1)
    else:
        print(x, y)
