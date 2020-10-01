d = {}
res = ''
t = 0
for _ in range(int(input())):
    s = input()
    if s not in d:
        d[s] = 1
    else:
        d[s] += 1
    if d[s] > t:
        res = s
        t = d[s]
print(res)

