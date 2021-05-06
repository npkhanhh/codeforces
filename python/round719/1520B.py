from sys import stdin


def sol1(n):
    s = str(n)
    t = 1
    res = 0
    for i in range(0, len(s)):
        for j in range(1, 10):
            if n >= t * j:
                res += 1
        t = t * 10 + 1
    return res


def sol2(n):
    s = str(n)
    a = list(map(int, list(s)))
    res = 0
    if len(a) == 1:
        res = a[0]
    else:
        res = a[0] - 1
        res += 9 * (len(a) - 1)
        if a[1] >= a[0]:
            res += 1
    return res

i = 110
res1 = sol1(i)
res2 = sol2(i)
if i == 110:
    print(res2)
