n = int(input())
s = input()
res = []
tail = n % 2 == 1
for i in range(n):
    if not tail:
        res.insert(0, s[i])
    else:
        res.append(s[i])
    tail = not tail
print(''.join(res))

