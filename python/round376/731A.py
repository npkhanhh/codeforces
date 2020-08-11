s = input()

t = 97
res = 0
for i in s:
    tt = ord(i)
    a = tt
    if tt < t:
        t, tt = tt, t
    res += min(tt - t, t + 26 - tt)
    t = a
print(res)
