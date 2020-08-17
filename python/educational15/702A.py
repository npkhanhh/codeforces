n = int(input())
a = list(map(int, input().split()))
a.append(0)
res = 1
t = 1
for i in range(1, n+1):
    if a[i] <= a[i-1]:
        if t > res:
            res = t
        t = 1
    else:
        t += 1
print(res)
