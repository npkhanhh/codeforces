n = int(input())
s = input()
d = {}
m = 0
res = ''
for i in range(n-1):
    t = s[i:i+2]
    if t not in d:
        d[t] = 1
    else:
        d[t] += 1
    if d[t] > m:
        m = d[t]
        res = t
print(res)
