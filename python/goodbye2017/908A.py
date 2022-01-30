v = {'a', 'e', 'i', 'o', 'u'}
s = input().strip()
res = 0
for i in s:
    if i in v:
        res += 1
    elif i.isdigit() and int(i) % 2 == 1:
        res += 1
print(res)

