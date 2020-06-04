from sys import stdin

for _ in range(int(stdin.readline())):
    s = input()
    t = [-1] * 3
    res = len(s)
    for i, value in enumerate(s):
        t[int(value)-1] = i
        if min(t) > -1 and max(t) - min(t) + 1 < res:
            res = max(t) - min(t) + 1
    if min(t) == -1:
        res = 0
    print(res)

