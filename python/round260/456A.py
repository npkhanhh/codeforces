a = []
n = int(int(input()))
for _ in range(n):
    a.append(list(map(int, input().split())))
a.sort(key=lambda x: x[0])
res = 'Poor Alex'
for i in range(n-1):
    if a[i][1] > a[i+1][1]:
        res = 'Happy Alex'
        break
print(res)



