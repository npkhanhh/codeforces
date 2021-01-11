n = int(input())
a = sorted(list(map(int, input().split())))
res = 1
s = a[0]
for i in a[1:]:
    if i >= s:
        res += 1
        s += i
print(res)
