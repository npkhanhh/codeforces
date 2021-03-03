from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    res = 0
    for i in range(1, n):
        if a[i] < a[i-1]:
            res += a[i-1] - a[i]
    print(res)
