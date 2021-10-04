from sys import stdin

for _ in range(int(stdin.readline())):
    n, h = list(map(int, stdin.readline().split()))
    a = sorted(map(int, stdin.readline().split()), reverse=True)
    b = a[0] + a[1]
    c, d = divmod(h, b)
    res = c * 2 + (d>0)
    if d > a[0]:
        res += 1
    print(res)
