from sys import stdin

n, k = list(map(int, stdin.readline().split()))
a = [[0]*n for _ in range(n)]
for i in range(n):
    a[i][i] = k
    print(*a[i])
