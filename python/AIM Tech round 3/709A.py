n, b, d = list(map(int, input().split()))
a = list(map(int, input().split()))
cur = 0
res = 0
for i in a:
    if i <= b:
        cur += i
        if cur > d:
            res += 1
            cur = 0
print(res)
