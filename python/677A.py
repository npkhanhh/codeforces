n, h = list(map(int, input().split()))
l = list(map(int, input().split()))

res = 0
for i in l:
    res += 2 if i > h else 1

print(res)
