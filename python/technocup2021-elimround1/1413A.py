from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    res = []
    for i in range(0, n, 2):
        res.append(a[i+1]*-1)
        res.append(a[i])
    print(*res)
