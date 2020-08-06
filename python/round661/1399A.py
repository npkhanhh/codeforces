from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = sorted(map(int, stdin.readline().split()))
    res = 'YES'
    for i in range(n - 1):
        if a[i + 1] - a[i] > 1:
            res = 'NO'
            break
    print(res)
