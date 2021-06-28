n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

left = 0
right = n - 1
res1 = 0
res2 = 0
while left < n and a[left] <= k:
    left += 1
    res1 += 1
while right >= 0 and a[right] <= k:
    right -= 1
    res2 += 1
if res1 == n:
    print(res1)
else:
    print(res1 + res2)
