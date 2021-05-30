from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = sorted(map(int, stdin.readline().split()))
    res = [0]*(2*n)
    for i in range(n):
        t = 2*i
        res[t] = a[i]
        res[t+1] = a[i+n]

    print(*res)

