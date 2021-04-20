n = int(input())
a = sorted(map(int, input().split()))

res = 0
for i in range(1, n - 1):
    if a[0] < a[i] < a[-1]:
        res += 1
print(res)
