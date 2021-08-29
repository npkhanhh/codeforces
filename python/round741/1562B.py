from sys import stdin
from collections import Counter

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, list(stdin.readline().strip())))
    c = Counter(a)
    pair = -1
    for p in c.items():
        if p[1] >= 2:
            pair = p[0]
            break
    if 1 in c:
        print(1)
        print(1)
    elif 4 in c:
        print(1)
        print(4)
    elif 6 in c:
        print(1)
        print(6)
    elif 8 in c:
        print(1)
        print(8)
    elif 9 in c:
        print(1)
        print(9)
    elif pair != -1:
        print(2)
        print(pair*10+pair)
    elif a[0] != 2 and 2 in c:
        print(2)
        print(a[0]*10+2)
    elif a[0] != 5 and 5 in c:
        print(2)
        print(a[0]*10+5)
    elif a[0] == 5 and 7 in c:
        print(2)
        print(57)
    elif a[0] == 2 and 7 in c:
        print(2)
        print(27)





