from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = sorted(map(int, stdin.readline().split()))
    offset = 0
    res = -10**10
    for idx, val in enumerate(a):
        res = max(res, val - offset)
        offset += val - offset
    print(res)

