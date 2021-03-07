from collections import Counter

k = int(input())
s = input()
d = Counter(s)
res = ''
for t in d:
    val = d[t]
    if val % k == 0:
        res += t * (val // k)
    else:
        res = '-1'
        break
if res != '-1':
    res *= k
print(res)
