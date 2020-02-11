import math

for _ in range(int(input())):
    n, d = list(map(int, input().split()))
    res = 'NO'
    cur = d
    for i in range(n+1):
        t = i + math.ceil(d/(i+1))
        if t <= n:
            res = 'YES'
            break
        if t > cur:
            break

    print(res)
