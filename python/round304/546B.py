n = int(input())
a = sorted(map(int, input().split()))

cur = a[0] + 1
res = 0
for idx, val in enumerate(a[1:], start=1):
    if val <= cur:
        res += cur - val
        cur += 1
    else:
        cur = val + 1

print(res)
