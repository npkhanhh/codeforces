from sys import stdin

for _ in range(int(stdin.readline())):
    a = list(map(int, stdin.readline().split()))
    ma = max(a)
    c = 0
    for i in a:
        if i == ma:
            c += 1
    offset = 1 if c > 1 else 0
    res = []
    for i in a:
        if i == max(a):
            res.append(offset)
        else:
            res.append(ma - i + 1)
    print(*res)

