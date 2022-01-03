n = int(input())
a = list(map(int, input().split()))
b = sorted(a, reverse=True)
m = [0]*2001
cur = 1
m[b[0]] = cur
for idx in range(1, n):
    if b[idx] != b[idx-1]:
        cur = idx + 1
        m[b[idx]] = cur
res = [0]*n
for i in range(n):
    res[i] = m[a[i]]
print(*res)
