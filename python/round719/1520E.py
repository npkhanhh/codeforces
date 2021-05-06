from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    s = stdin.readline().strip()
    a = []
    for idx, val in enumerate(s):
        if val == '*':
            a.append(idx)
    if len(a) <= 1:
        print(0)
    else:
        nn = len(a)
        res = 0, 0
        mid1 = nn // 2
        mid1_idx = a[mid1]
        for idx, val in enumerate(a):
            t = abs(mid1 - idx)
            if idx < mid1:
                res += abs((mid1_idx - t) - val)
            elif idx > mid1:
                res += abs(val - (mid1_idx + t))

        print(res)
