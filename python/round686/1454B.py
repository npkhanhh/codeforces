from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = sorted(enumerate(list(map(int, stdin.readline().split()))), key=lambda x: x[1])
    res = -1
    if n == 1:
        res = a[0][0] + 1
    else:
        for i in range(1, n - 1):
            if a[i][1] != a[i+1][1] and a[i][1] != a[i-1][1]:
                res = a[i][0] + 1
                break

        if a[0][1] != a[1][1]:
            res = a[0][0] + 1
        if res == -1 and a[-2][1] != a[-1][1]:
            res = a[-1][0] + 1
    print(res)
