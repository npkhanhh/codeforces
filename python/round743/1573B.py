from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    p = [0]*(2*n+1)
    for i in range(n):
        p[a[i]] = i+1
        p[b[i]] = i+1
    ans = 2*n+1
    l = 2*n+1
    for i in range(2*n, 0, -1):
        if i % 2 == 0:
            l = min(l, p[i])
        else:
            ans = min(ans, p[i]+l-2)
    print(ans)


