import math


def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n - r)


def cal_plus(s):
    res = 0
    for c in s:
        if c == '+':
            res += 1
    return res


s1 = input().strip()
s2 = input().strip()

f1 = cal_plus(s1)
f2 = cal_plus(s2)
d = f1 - f2
q = 0
for i in s2:
    if i == '?':
        q += 1
if d == q == 0:
    print(1)
elif q < d or d < 0:
    print(0)
else:
    print(nCr(q, d) / 2**q)
