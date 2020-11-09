n, k = list(map(int, input().split()))

a = list(map(int, input().split()))
res = []
d = {}
for idx, val in enumerate(a):
    if val not in d:
        d[val] = 1
        res.append(idx+1)
        if len(res) == k:
            break
if len(res) == k:
    print('YES')
    print(*res)
else:
    print('NO')

