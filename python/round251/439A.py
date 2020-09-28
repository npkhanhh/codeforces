n, d = list(map(int, input().split()))
a = list(map(int, input().split()))
res = 0
t = 0
for i in a[:-1]:
    t += i + 10
    res += 2
t += a[-1]
if t > d:
    res = -1
else:
    res += (d - t) // 5
print(res)


