from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    res = min(a) + k
    for i in a:
        if res < i - k or res > i + k:
            res = -1
            break
    print(res)
