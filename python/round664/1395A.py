from sys import stdin

for _ in range(int(stdin.readline())):
    r, g, b, w = list(map(int, stdin.readline().split()))
    res = 'No'
    if sum([r % 2, g % 2, b % 2, w % 2]) <= 1:
        res = 'Yes'
    elif r > 0 and g > 0 and b > 0:
        rr = r - 1
        gg = g - 1
        bb = b - 1
        ww = w + 3
        if sum([rr % 2, gg % 2, bb % 2, ww % 2]) <= 1:
            res = 'Yes'
    print(res)
