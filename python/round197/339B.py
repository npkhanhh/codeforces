n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
res = 0
cur = 1
for i in a:
    if i < cur:
        res += n + i - cur
    else:
        res += i - cur
    cur = i
print(res)
