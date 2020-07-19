from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    d = {}
    res = []
    for i in list(map(int, stdin.readline().split())):
        if i not in d:
            d[i] = 1
            res.append(i)
    print(*res)
