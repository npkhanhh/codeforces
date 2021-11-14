from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, list(stdin.readline().strip())))
    b = sorted(a)
    res = []
    for i in range(n):
        if a[i] != b[i]:
            res.append(i+1)
    if len(res) == 0:
        print(0)
    else:
        print(1)
        print(len(res), *res)
