n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
s = sum(a[:k])
min_s = s
idx = 1
for i in range(n-k):
    s -= a[i]
    s += a[i+k]
    if s < min_s:
        min_s = s
        idx = i + 2
print(idx)


