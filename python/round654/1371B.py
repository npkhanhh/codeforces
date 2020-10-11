from sys import stdin

for _ in range(int(stdin.readline())):
    n, r = list(map(int, stdin.readline().split()))
    res = 0
    if r >= n:
        res += 1
    t = min(r, n-1)
    res += t * (t + 1) // 2
    print(res)
