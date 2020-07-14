n = int(input())
res = 0
while n > 0:
    n, b = divmod(n, 2)
    res += b
print(res)
