a, b = list(map(int, input().split()))

res = min(a, b)
print(res, (max(a, b)-res)//2)