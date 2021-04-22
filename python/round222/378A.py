a, b = list(map(int, input().split()))

res = [0]*3
for i in range(1, 7):
    if abs(i-a) < abs(i-b):
        res[0] += 1
    if abs(i-a) == abs(i-b):
        res[1] += 1
    if abs(i-a) > abs(i-b):
        res[2] += 1
print(*res)
