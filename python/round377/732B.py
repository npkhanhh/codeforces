n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
if n == 1:
    print(0)
    print(*a)
else:
    f, s = 0, 0
    fa, sa = [], []
    for idx, val in enumerate(a):
        if idx == 0:
            sa.append(val)
            if a[0] + a[1] < k:
                t = k - a[0] - a[1]
                f += t
                fa.append(val+t)
            else:
                fa.append(val)
            continue
        if idx == 1:
            fa.append(val)
            if a[0] + a[1] < k:
                t = k - a[0] - a[1]
                s += t
                sa.append(val+t)
            else:
                sa.append(val)
            continue
        if fa[idx-1] + val < k:
            t = k - val - fa[idx-1]
            fa.append(val+t)
            f += t
        else:
            fa.append(val)
        if sa[idx-1] + val < k:
            t = k - val -sa[idx-1]
            sa.append(val+t)
            s += t
        else:
            sa.append(val)
    if f < s:
        print(f)
        print(*fa)
    else:
        print(s)
        print(*sa)

