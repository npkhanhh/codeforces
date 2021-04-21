
n = int(input())
a = list(map(int, input().split()))
res = "Yes"
for i in range(n):
    while a[i] % 3 == 0:
        a[i] //= 3
    while a[i] % 2 == 0:
        a[i] //= 2
    if i > 0 and a[i] != a[i-1]:
        res = "No"
        break
print(res)
