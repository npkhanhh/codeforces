a = list(map(int, input().split()))
s = set(a)
x1, y1, x2, y2 = a
lx = abs(x2-x1)
ly = abs(y2-y1)
if lx != ly and lx != 0 and ly != 0:
    print(-1)
else:
    length = max(lx, ly)
    x = min(x1, x2)
    y = min(y1, y2)
    res = []

    for i in [x, x+length]:
        for j in [y, y+length]:
            if (i == x1 and j == y1) or (i == x2 and j == y2):
                continue
            res += [i, j]
    print(*res)
