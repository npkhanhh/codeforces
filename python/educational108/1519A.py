from sys import stdin

for _ in range(int(stdin.readline())):
    r, b, d = list(map(int, stdin.readline().split()))
    m = min(r, b)
    if (d+1)*m < max(r, b):
        print('NO')
    else:
        print('YES')
