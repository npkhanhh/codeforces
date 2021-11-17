from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = sorted(map(int, stdin.readline().split()))
    b = sorted(map(int, stdin.readline().split()))
    res = 'YES'
    for i in range(n):
        if b[i] - a[i] > 1 or b[i] - a[i] < 0:
            res = 'NO'
            break
    print(res)
