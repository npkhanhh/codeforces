from sys import stdin

for _ in range(int(stdin.readline())):
    a, b, c, m = list(map(int, stdin.readline().split()))
    if a + b + c - 3 < m:
        print('NO')
        continue
    a, b, c = sorted([a, b, c])
    if c - 1 - (b+a) > m:
        print('NO')
        continue
    print('YES')
