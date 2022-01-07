from sys import stdin

for _ in range(int(stdin.readline())):
    n, m, r, c = list(map(int, stdin.readline().split()))
    res = max(r-1, n-r) + max(c-1, m-c)
    print(res)
