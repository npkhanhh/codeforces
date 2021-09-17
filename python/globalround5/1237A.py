import math
from sys import stdin

positive = True
negative = False

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n >= 0:
        if n % 2 == 0:
            print(n//2)
        elif positive:
            print(int(math.ceil(n/2)))
            positive = False
        else:
            print(int(math.floor(n/2)))
            positive = True
    else:
        if n % 2 == 0:
            print(n//2)
        elif negative:
            print(int(math.ceil(n/2)))
            negative = False
        else:
            print(int(math.floor(n/2)))
            negative = True


