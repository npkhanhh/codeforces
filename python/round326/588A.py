from sys import stdin

n = int(stdin.readline())
res = 0
price = float('inf')
for _ in range(n):
    x, y = list(map(int, stdin.readline().split()))
    if y < price:
        price = y
    res += price * x

print(res)


