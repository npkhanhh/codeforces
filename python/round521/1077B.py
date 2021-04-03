n = int(input())
a = list(map(int, input().split()))

res = 0
cur = 0
for i in range(n):
    if a[i] == 1:
        if cur == 0:
            cur += 1
        if cur == 2:
            res += 1
            cur = 0
    else:
        if cur != 1:
            cur = 0
        else:
            cur += 1
print(res)
