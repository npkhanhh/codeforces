from sys import stdin

for _ in range(int(stdin.readline())):
    n, l, r, k = list(map(int, stdin.readline().split()))
    a = sorted(map(int, stdin.readline().split()))
    res = 0
    for i in a:
        if l <= i <= r and i <= k:
            res += 1
            k -= i
    print(res)


