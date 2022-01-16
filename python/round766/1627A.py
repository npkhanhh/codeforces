from sys import stdin

for _ in range(int(stdin.readline())):
    n, m, r, c = list(map(int, stdin.readline().split()))
    res = -1
    for i in range(n):
        s = stdin.readline().strip()
        for j in range(m):
            if s[j] == 'B' and res == -1:
                res = 2
            if s[j] == 'B' and i == r - 1 and j == c - 1:
                res = 0
            elif s[j] == 'B' and res == 2 and i == r -1:
                res = 1
            elif s[j] == 'B' and res == 2 and j == c - 1:
                res = 1
    print(res)


