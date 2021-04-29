from sys import stdin

for _ in range(int(stdin.readline())):
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    c = min(a[2], b[1])
    res = c*2
    a[2] -= c
    b[1] -= c
    c = min(a[2], b[2])
    a[2] -= c
    b[2] -= c
    c = min(a[0], b[2])
    a[0] -= c
    b[2] -= c
    res -= b[2]*2
    print(res)

