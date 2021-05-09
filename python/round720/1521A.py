import math
from sys import stdin

for _ in range(int(stdin.readline())):
    a, b = list(map(int, stdin.readline().split()))
    if b == 1:
        print('NO')
    else:
        print('YES')
        m = a*b
        if b == 2:
            print(3*a, 5*a, 8*a)
        else:
            print(a, (b-1)*a, b*a)


