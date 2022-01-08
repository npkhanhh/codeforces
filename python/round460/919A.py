from sys import stdin

n, m = list(map(int, stdin.readline().split()))
res = 10000
for _ in range(n):
    a, b = list(map(int, stdin.readline().split()))
    res = min((a*m)/b, res)
print(res)



