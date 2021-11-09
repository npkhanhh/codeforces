from sys import stdin
from math import gcd

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    a = list(set(a))
    s = set()
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            s.add(abs(a[i]-a[j]))
    res = -1
    if len(s):
        res = s.pop()
        while len(s):
            res = gcd(res, s.pop())
    print(res)





