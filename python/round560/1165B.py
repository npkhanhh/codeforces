n = int(input())
a = sorted(map(int, input().split()))

res = 0
cur = 1
for i in a:
    if i >= cur:
        res += 1
        cur += 1
print(res)
