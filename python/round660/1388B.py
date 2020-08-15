from sys import stdin
import math

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    t = math.ceil(n/4)
    res = '9'*(n-t) + '8'*t
    print(res)
