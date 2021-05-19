import math
from sys import stdin


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n == 1:
        print('NO')
    else:
        t = math.ceil(pow(n, 1/3)) + 1
        res = 'NO'
        for i in range(1, t):
            a = n - i**3
            if a <= 0:
                break
            b = pow(a, 1/3)
            if abs(round(b) - b) < 10**-9:
                res = 'YES'
                break
        print(res)
