from sys import stdin

for _ in range(int(stdin.readline())):
    n, m, k = list(map(int, stdin.readline().split()))
    if k == n-1 + n*(m-1):
        print('YES')
    else:
        print('NO')

