from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    a = sorted(map(int, stdin.readline().split()))
    res = 0
    cur = 0
    for i in range(k-1, -1, -1):
        if cur < a[i]:
            res += 1
            cur += n - a[i]
        else:
            break
    print(res)
