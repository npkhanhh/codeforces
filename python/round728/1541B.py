from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    res = 0
    for i in range(n):
        for j in range(a[i]-i-2, n, a[i]):
            res += j > i and i+j+2 == a[i]*a[j]
    print(res)
