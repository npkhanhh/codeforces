n = int(input())
a = list(map(int, input().split()))
res = 1
for idx, value in enumerate(a):
    temp_res = 1
    t = idx + 1
    while t < n and a[t] <= a[t-1]:
        temp_res += 1
        t += 1
    t = idx - 1
    while t >= 0 and a[t] <= a[t+1]:
        temp_res += 1
        t -= 1
    if temp_res > res:
        res = temp_res
print(res)
