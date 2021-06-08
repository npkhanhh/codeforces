from sys import stdin

for _ in range(int(stdin.readline())):

    res = 'YES'
    a = list(map(int, stdin.readline().split()))
    if max(a[0], a[1]) < min(a[2], a[3]) or min(a[0], a[1]) > max(a[2], a[3]):
        res = 'NO'
    print(res)
