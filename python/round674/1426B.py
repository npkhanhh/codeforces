from sys import stdin

for _ in range(int(stdin.readline())):
    n, m = list(map(int, stdin.readline().split()))
    res = False
    for _ in range(n):
        a, b = list(map(int, stdin.readline().split()))
        x, y = list(map(int, stdin.readline().split()))
        if m % 2 == 0 and x == b:
            res = True
    print('YES' if res else 'NO')

