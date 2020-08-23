s = input()
res = 0
for idx, val in enumerate(s[::-1]):
    t = 1
    if val == '7':
        t = 2
    res += 2**idx * t
print(res)

