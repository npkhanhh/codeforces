from sys import stdin
from collections import Counter

for _ in range(int(stdin.readline())):
    t = int(stdin.readline())
    a = sorted(map(int, stdin.readline().split()))
    d = {}
    res = 1
    for i in range(1, t):
        if a[i] <= a[i-1]:
            a[i] += 1
    print(len(Counter(a)))
