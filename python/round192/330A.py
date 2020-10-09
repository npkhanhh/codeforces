r, c = list(map(int, input().split()))
no_r = 0
a = []
res = 0
for _ in range(r):
    s = input()
    a.append(s)
    if 'S' not in s:
        no_r += 1
for i in range(c):
    has_s = False
    for j in range(r):
        if a[j][i] == 'S':
            has_s = True
            break
    if not has_s:
        res += r - no_r
res += no_r*c
print(res)
