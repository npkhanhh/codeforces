n = int(input())
a = list(map(int, input().split()))

p = 0
res = 0
for i in a:
    if i < 0 and p == 0:
        res += 1
    else:
        p += i
print(res)
