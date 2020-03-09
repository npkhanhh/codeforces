n, a, x, b, y = list(map(int, input().split()))
res = 'NO'
while True:
    a += 1
    b -= 1
    if b == 0:
        b = n
    if a == n + 1:
        a = 1
    if a == b:
        res = 'YES'
        break
    if a == x or b == y:
        break
print(res)
