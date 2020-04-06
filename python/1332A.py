for _ in range(int(input())):
    a, b, c, d = list(map(int, input().split()))
    x, y, x1, y1, x2, y2 = list(map(int, input().split()))
    u = x - (a - b)
    v = y - (c - d)
    res = 'NO'
    if x1 <= u <= x2 and y1 <= v <= y2 \
            and (((b > 0 or a > 0) and (x1 < x or x < x2)) or (a == 0 and b == 0)) \
            and (((c > 0 or d > 0) and (y1 < y or y < y2)) or (c == 0 and d == 0)):
        res = 'YES'
    print(res)
