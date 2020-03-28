n = int(input())

l = list(map(int, input().split()))

b, w = 0, 0
black_prev = False
for i in l:
    j, k = divmod(i, 2)
    b += j
    w += j
    if black_prev:
        w += k
    else:
        b += k
    black_prev = not black_prev

print(min(b, w))
