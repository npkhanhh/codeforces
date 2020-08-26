n = int(input())
a = sorted(map(int, input().split()))
res = False
for i in range(n - 2):
    if a[i] + a[i + 1] > a[i + 2]:
        res = True
if res:
    print('YES')
else:
    print('NO')
