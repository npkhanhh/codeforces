n = int(input())
a = sorted(map(int, input().split()))

res = n // 2
if n % 2 == 0:
    res -= 1
for i in range(0, n-1,2):
    a[i], a[i+1] = a[i+1], a[i]
print(res)
print(*a)
