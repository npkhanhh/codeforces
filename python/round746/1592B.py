from sys import stdin

for _ in range(int(stdin.readline())):
    n, x = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    b = sorted(a)
    end = x
    start = n - x
    res = 'YES'
    for i in range(start, end):
        if a[i] != b[i]:
            res = 'NO'
            break
    print(res)

