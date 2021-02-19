from sys import stdin

for _ in range(int(stdin.readline())):
    n, d = list(map(int, stdin.readline().split()))
    a = sorted(map(int, stdin.readline().split()))
    if a[0] + a[1] <= d or a[-1] <=d:
        print('YES')
    else:
        print('NO')
