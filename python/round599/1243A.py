from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = sorted(map(int, stdin.readline().split()))
    res = 0
    for idx, val in enumerate(a):
        res = max(min(val, n-idx), res)
    print(res)
