input()
s = input()
a = []
t = 0
for i in s:
    if i == 'B':
        t += 1
    else:
        if t > 0:
            a.append(t)
        t = 0
if t > 0:
    a.append(t)
print(len(a))
if len(a) > 0:
    print(*a)
