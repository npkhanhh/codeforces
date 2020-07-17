n = int(input())
j = 0
res = 0
for i in range(n, 0, -1):
    if j == 0:
        res += i
    else:
        res += i * j
    j += 1
print(res)
