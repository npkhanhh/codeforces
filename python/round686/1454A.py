from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    res = []
    for i in range(n - 1):
        res.append(i + 2)
    res.append(1)
    print(*res)
