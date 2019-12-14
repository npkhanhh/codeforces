x1, y1, x2, y2 = list(map(int, input().split()))
x3, y3, x4, y4 = list(map(int, input().split()))
x5, y5, x6, y6 = list(map(int, input().split()))

r = 'NO'
if x4 <= x5:
    if x1 <= x4 and x2 >= x5:
        r = 'YES'
if x6 <= x3:
    if x1 <= x6 and x2 >= x3:
        r = 'YES'
if y4 <= y5:
    if y1 <= y4 and y2 >= y5:
        r = 'YES'
if y6 <= y3:
    if y1 <= y6 and y2 >= y3:
        r = 'YES'
if x1 <= x3 and x1 <= x5:
    r = 'YES'
if x2 >= x4 and x2 >= x6:
    r = 'YES'
if y1 <= y3 and y1 <= y5:
    r = 'YES'
if y2 >= y4 and y2 >= y6:
    r = 'YES'
print(r)
