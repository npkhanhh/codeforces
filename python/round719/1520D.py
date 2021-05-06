from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    d = {}
    for idx, val in enumerate(a):
        diff = val - idx
        if diff not in d:
            d[diff] = 1
        else:
            d[diff] += 1
    res = 0
    for val in d.values():
        res += (val*(val-1))//2
    print(res)

