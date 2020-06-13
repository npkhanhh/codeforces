n, k = list(map(int, input().split()))

a = list(map(int, input().split()))
res = 0
for i in a:
    if i <= 5 - k:
        res += 1

print(res//3)
