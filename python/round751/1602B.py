from sys import stdin
from collections import Counter

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    t = [a]
    is_same = False
    while not is_same:
        b = []
        c = Counter(a)
        for i in a:
            b.append(c[i])
        is_same = True
        for i in range(n):
            if a[i] != b[i]:
                is_same = False
                break
        if not is_same:
            t.append(b)
            a = b
    for _ in range(int(stdin.readline())):
        x, k = list(map(int, stdin.readline().split()))
        if k >= len(t):
            print(t[-1][x-1])
        else:
            print(t[k][x-1])

