from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = [0] + list(map(int, stdin.readline().split()))
    res = [0]*n
    for i in range(1, n+1):
        t = 1
        cur = a[i]
        while cur != i:
            t+= 1
            cur = a[cur]
        res[i-1] = t
    print(*res)
