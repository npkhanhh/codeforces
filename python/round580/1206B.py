n = int(input())
a = list(map(int, input().split()))
res = 0
neg = 0
z = 0
for i in a:
    if i < 0:
        res += -1 - i
        neg += 1
    elif i > 0:
        res += i - 1
    else:
        res += 1
        z += 1
if neg % 2 == 1 and z == 0:
    res += 2
print(res)
