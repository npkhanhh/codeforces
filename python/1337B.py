import math

for _ in range(int(input())):
    x, n, m = list(map(int, input().split()))
    while x > 20 and n > 0:
        x = x // 2 + 10
        n -= 1
    if math.ceil(x / 10) <= m:
        print('YES')
    else:
        print('NO')
