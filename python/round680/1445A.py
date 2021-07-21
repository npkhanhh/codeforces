from sys import stdin

for _ in range(int(stdin.readline())):
    n, x = list(map(int, stdin.readline().split()))
    a = sorted(map(int, stdin.readline().split()))
    b = sorted(map(int, stdin.readline().split()), reverse=True)
    stdin.readline()
    res = True
    for i in range(n):
        if a[i] + b[i] > x:
            res = False
            break
    print('YES' if res else 'NO')
