from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

d = {}
prefixes = [0]*n
prefixes[0] = a[0]
d[a[0]] = 0
for idx, val in enumerate(a[1:], start=1):
    prefixes[idx] = val + prefixes[idx-1]
    d[prefixes[idx]] = idx

cur = 0
res = 0
for i in range(n-1, -1, -1):
    cur += a[i]
    if cur in d and i > d[cur]:
        res = cur
print(res)

