from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    m = max(a)
    res = -1
    for idx, val in enumerate(a):
        if val == m:
            if idx > 0 and val > a[idx - 1]:
                res = idx + 1
                break
            if idx < n - 1 and val > a[idx + 1]:
                res = idx + 1
                break
    print(res)
