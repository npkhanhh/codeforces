from sys import stdin
from collections import Counter


for _ in range(int(stdin.readline())):
    c = Counter(stdin.readline().strip())
    res = ""
    for key, val in c.items():
        res += val*key
    print(res)


