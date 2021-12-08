from sys import stdin

n, m = list(map(int, stdin.readline().split()))
a = [False]*m
for _ in range(n):
    b = list(map(int, stdin.readline().split()))
    for i in range(1, len(b)):
        a[b[i]-1] = True

print('YES' if all(a) else 'NO')
