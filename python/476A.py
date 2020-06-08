import math
n, m = list(map(int, input().split()))
if n < m:
    print(-1)
else:
    t = int(math.ceil(n / 2))
    if t <= m:
        print(m)
    elif t % m == 0:
        print(t)
    else:
        print(t + (m - (t % m)))

