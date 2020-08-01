from sys import stdin

n, m = list(map(int, stdin.readline().split()))
d = {}
for _ in range(m):
    a, b = stdin.readline().split()
    d[a] = b if len(b) < len(a) else a
s = stdin.readline().split()
res = []
for t in s:
    res.append(d[t])
print(" ".join(res))
