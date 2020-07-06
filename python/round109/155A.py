n = int(input())
a = list(map(int, input().split()))
big = a[0]
small = a[0]
res = 0
for i in range(1, n):
    if a[i] > big:
        res += 1
        big = a[i]
    elif a[i] < small:
        res += 1
        small = a[i]
print(res)
