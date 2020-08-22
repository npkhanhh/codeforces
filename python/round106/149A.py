k = int(input())
a = sorted(map(int, input().split()), reverse=True)
a.append(0)
if k == 0:
    print(0)
else:
    t = 0
    res = -1
    for idx, val in enumerate(a):
        t += val
        if t >= k:
            res = idx + 1
            break
    print(res)


