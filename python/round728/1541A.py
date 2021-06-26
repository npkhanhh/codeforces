from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    res = []
    if n % 2 == 1:
        res = [3, 1, 2]
        for i in range(4, n+1, 2):
            res.extend([i+1, i])
    else:
        for i in range(1, n+1, 2):
            res.extend([i+1, i])
    print(*res)
