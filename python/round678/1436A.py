from sys import stdin

for _ in range(int(stdin.readline())):
    n, m = list(map(int, stdin.readline().split()))
    a = sum(list(map(int, stdin.readline().split())))
    if a == m:
        print('YES')
    else:
        print('NO')
