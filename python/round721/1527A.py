from sys import stdin

import math

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    t = math.floor(math.log2(n))
    print(pow(2, t)-1)
