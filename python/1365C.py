n = int(input())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))

a_t = [0] * (n + 1)
for idx, val in enumerate(a):
    if idx == 0:
        continue
    a_t[val] = idx

res = 0
d = {}
for idx, val in enumerate(b):
    if idx == 0:
        continue
    t = a_t[val] - idx
    if t < 0:
        t += n
    if t not in d:
        d[t] = 1
    else:
        d[t] += 1
    if d[t] > res:
        res = d[t]
print(res)
