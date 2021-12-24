from sys import stdin

for _ in range(int(stdin.readline())):
    w, h = list(map(int, stdin.readline().split()))
    res = 0
    for i in range(4):
        a = list(map(int, stdin.readline().split()))
        b = sorted(a[1:])
        t = h if i < 2 else w
        res = max(res, t*(b[-1]-b[0]))
    print(res)
