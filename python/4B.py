

d, st = list(map(int, input().split()))
t_min = t_max = 0
a = []
res = []
for _ in range(d):
    mi, ma = list(map(int, input().split()))
    a.append((mi, ma))
    res.append(mi)
    t_min += mi
    t_max += ma
if t_min <= st <= t_max:
    print('YES')
    for idx, value in enumerate(a):
        if value[1] - value[0] < (st - sum(res)):
            res[idx] = value[1]
        else:
            res[idx] += st - sum(res)
            break
    print(*res)
else:
    print('NO')


