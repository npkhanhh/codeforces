n = input()
s1 = input()
s2 = input()
res = 0
for idx, val in enumerate(s1):
    i1 = int(val)
    i2 = int(s2[idx])
    res += min(abs(i1 - i2), abs(i1 - (10 + i2)), abs((10 + i1) - i2))
print(res)
