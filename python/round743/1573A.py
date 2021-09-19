from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, list(stdin.readline().strip())))
    res = 0
    for idx, val in enumerate(a):
        if val != 0:
            res += val + (idx != n-1)
    print(res)
