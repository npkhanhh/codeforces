x, y, z = list(map(int, input().split()))
a, b, c = list(map(int, input().split()))

res = 'YES'
if a >= x:
    a -= x
else:
    res = 'NO'
if a + b >= y:
    c += a + b - y
else:
    res = 'NO'
if c < z:
    res = 'NO'
print(res)
