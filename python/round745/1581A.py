from math import factorial
from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    res = 1
    for i in range(1, 2 * n + 1):
        res *= i
        if i != 2*n:
            res %= 10 ** 9 + 7
    print((res // 2) % (10 ** 9 + 7))
