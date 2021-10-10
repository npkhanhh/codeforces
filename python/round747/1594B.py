from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    t = str(bin(k))[2:]
    t = t[::-1]
    res = 0
    cur = 1
    for i in t:
        if i == '1':
            res += cur
            res %= 10**9+7
        cur *= n
        cur %= 10**9+7
    print(res)

