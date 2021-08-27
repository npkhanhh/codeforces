from sys import stdin
from collections import Counter

for _ in range(int(stdin.readline())):
    stdin.readline()
    a = Counter(list(map(int, stdin.readline().split())))
    res = 'NO'
    for pair in a.items():
        if pair[1] > 1:
            res = 'YES'
            break
    print(res)

