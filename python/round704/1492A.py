from sys import stdin

for _ in range(int(stdin.readline())):
    p, *a = list(map(int, stdin.readline().split()))
    res = 10**18
    for i in a:
        if p % i == 0:
            res = 0
            break
        res = min(res, i - (p % i))
    print(res)
