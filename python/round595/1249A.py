from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = sorted(map(int, stdin.readline().split()))
    res = 1
    for i in range(n - 1):
        if a[i + 1] - a[i] == 1:
            res = 2
            break
    print(res)
