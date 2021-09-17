import math
from sys import stdin

flag = 1

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n % 2 == 0:
        print(n // 2)
    else:
        print(n // 2 + flag)
        flag = 1 - flag
