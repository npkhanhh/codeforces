from sys import stdin

for _ in range(int(stdin.readline())):
    a, b, n, s = list(map(int, stdin.readline().split()))
    c, d = divmod(s, n)
    e = max((c - a)*n, 0)
    if e + d <= b:
        print('YES')
    else:
        print('NO')
