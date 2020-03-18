input()
a = list(map(int, input().split()))

d = {}
count = 0
for i, v in enumerate(a):
    if v not in d:
        d[v] = (0, i)
        count += 1
    elif d[v]:
        progress, last_index = d[v]
        if progress == 0:
            d[v] = (i - last_index, i)
        elif i - last_index != progress:
            d[v] = False
            count -= 1
        else:
            d[v] = (progress, i)
print(count)
for key in sorted(d.keys()):
    if d[key]:
        print(*[key, d[key][0]])

