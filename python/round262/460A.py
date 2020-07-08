n, m = list(map(int, input().split()))
a, b = divmod(n, m)
while a > 0:
    n += a
    a, c = divmod(a, m)
    b += c
    if b >= m:
        a += 1
        b -= m
print(n)
