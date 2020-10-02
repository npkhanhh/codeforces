from sys import stdin
from collections import Counter

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    count = Counter(a)
    if count[0] < count[1]:
        res = count[1] - count[1] % 2
        print(res)
        print('1 ' * res)
    else:
        res = count[0]
        print(res)
        print('0 ' * res)
