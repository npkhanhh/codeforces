from sys import stdin

n, m = list(map(int, stdin.readline().split()))
a = []
for _ in range(n):
    a.append(list(map(int, stdin.readline().split())))
a.sort(key=lambda x: x[0])
res = []
t = list(range(1, a[0][0]))

res += t
cur = a[0][1]
for seg in a[1:]:
    if seg[0] <= cur + 1:
        cur = max(cur, seg[1])
    else:
        res += list(range(cur + 1, seg[0]))
        cur = seg[1]
if cur < m:
    res += list(range(cur+1, m + 1))
print(len(res))
print(*res)
