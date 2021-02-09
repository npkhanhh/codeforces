s = input()
res = s[:-1]
for i, c in enumerate(s):
    if c == '0':
        res = s[:i] + s[i+1:]
        break
print(res)
