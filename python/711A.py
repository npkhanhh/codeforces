a = []
res = 'NO'
for _ in range(int(input())):
    s = input()
    if 'OO' in s and res == 'NO':
        s = s.replace('OO', '++', 1)
        res = 'YES'
    a.append(s)
print(res)
if res == 'YES':
    for i in a:
        print(i)

