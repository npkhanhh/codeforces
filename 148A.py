k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

res = 0
for i in range(1, d+1):
    if i % k == 0:
        res += 1
    elif i % l == 0:
        res += 1
    elif i % m == 0:
        res += 1
    elif i % n == 0:
        res += 1
print(res)
