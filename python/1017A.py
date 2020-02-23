res = 1
n = int(input())
thomas = sum(list(map(int, input().split())))
for _ in range(n-1):
    t = sum(list(map(int, input().split())))
    if t > thomas:
        res += 1
print(res)
