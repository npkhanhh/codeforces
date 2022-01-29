from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    cur = 1
    i = n - cur - 1
    res = 0
    while i >= 0:
        if a[i] != a[i + 1]:
            cur *= 2
            res += 1
            i = n - cur - 1
            a[i+1] = a[-1]
        else:
            i -= 1
            cur += 1
    print(res)
