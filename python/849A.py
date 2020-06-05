n = int(input())
a = list(map(int, input().split()))
res = 'Yes'
if n % 2 == 0:
    res = 'No'
if a[0] % 2 == 0 or a[-1] % 2 == 0:
    res = 'No'
print(res)
