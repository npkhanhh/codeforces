s = input()
res = len(s) // 2
if len(s) % 2 == 1:
    for c in s[1:]:
        if c == '1':
            res += 1
            break
print(res)

