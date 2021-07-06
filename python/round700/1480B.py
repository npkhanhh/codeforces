from sys import stdin
import math

for z in range(int(stdin.readline())):
    A, B, n = list(map(int, stdin.readline().split()))

    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    a = sorted([list(ele) for ele in zip(a, b)])
    for i in range(n):
        t = min(math.ceil(a[i][1]/A), math.ceil(B/a[i][0]))
        a[i][1] -= A * t
        B -= a[i][0] * t
        if B <= 0:
            break

    print('YES' if a[-1][1] <= 0 else 'NO')


# 879450 221893 2
# 152242 46952
# 963598 769221
