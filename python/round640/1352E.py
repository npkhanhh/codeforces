from sys import stdin


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    is_special = [0]*(n+1)
    for i in range(n):
        cur = a[i]
        for j in range(i+1, n):
            cur += a[j]
            if cur > n:
                break
            is_special[cur] = 1
    res = 0
    for i in a:
        res += is_special[i]
    print(res)

