k = int(input())
c = 'codeforces'
n = len(c)
t = int(k**(1/n))
s = t**10
a = [t]*n
i = 0
res = ''
while s < k:
    s /= t
    s *= t+1
    a[i] += 1
    i += 1
for idx, val in enumerate(c):
    res += val*a[idx]
print(res)

